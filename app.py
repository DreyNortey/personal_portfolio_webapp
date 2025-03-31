import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Configure mail settings
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
mail = Mail(app)

# Define cloud projects
cloud_projects = [
    {
        'id': 1,
        'title': 'AWS EC2 Project: Automated Infrastructure Deployment & Scaling with Terraform and Python',
        'description': 'Developed an automated infrastructure deployment solution using Terraform and Python scripts to provision, configure, and scale EC2 instances based on predefined parameters and real-time metrics.',
        'technologies': ['AWS EC2', 'Terraform', 'Python', 'CloudWatch', 'Auto Scaling'],
        'github': 'https://github.com/yourusername/aws-ec2-terraform-automation'
    },
    {
        'id': 2,
        'title': 'Automated S3 Data Lifecycle Management with Python (Boto3) & Terraform',
        'description': 'Created a comprehensive data lifecycle management system for S3 buckets that automatically handles data classification, retention policies, and archiving/deletion based on business rules.',
        'technologies': ['AWS S3', 'Python Boto3', 'Terraform', 'AWS Lambda', 'CloudWatch Events'],
        'github': 'https://github.com/yourusername/s3-lifecycle-automation'
    },
    {
        'id': 3,
        'title': 'Highly Available and Secure AWS VPC for a Scalable Web Application',
        'description': 'Designed and implemented a multi-AZ VPC architecture with proper security controls, network segmentation, and HA configurations to support a scalable web application.',
        'technologies': ['AWS VPC', 'Security Groups', 'NACLs', 'Load Balancing', 'Auto Scaling', 'NAT Gateway'],
        'github': 'https://github.com/yourusername/secure-ha-vpc'
    },
    {
        'id': 4,
        'title': 'Automated Microsoft 365 User Management System (Python & Microsoft Graph API)',
        'description': 'Developed a system that automates the provisioning, deprovisioning, and management of Microsoft 365 users, groups, and licenses through Python scripts and the Microsoft Graph API.',
        'technologies': ['Python', 'Microsoft Graph API', 'Azure AD', 'Microsoft 365', 'REST APIs'],
        'github': 'https://github.com/yourusername/m365-user-automation'
    }
]

# Define skills
skills = {
    'IT Support': ['Hardware Troubleshooting', 'Software Installation & Configuration', 'Network Diagnosis', 'User Support'],
    'Cloud Technologies': ['AWS', 'Azure', 'IaaS', 'PaaS', 'SaaS'],
    'Networking': ['TCP/IP', 'Subnetting', 'Routing', 'VPNs', 'Firewalls'],
    'Programming': ['Python', 'Bash Scripting', 'PowerShell'],
    'Infrastructure as Code': ['Terraform', 'CloudFormation'],
    'Operating Systems': ['Windows Server', 'Linux (Ubuntu, CentOS)', 'macOS'],
    'Security': ['Identity Management', 'Access Controls', 'Encryption', 'Security Best Practices'],
    'Automation': ['CI/CD Pipelines', 'Jenkins', 'GitHub Actions']
}

# Define certifications
certifications = [
    {
        'name': 'AWS Certified Solutions Architect - Associate',
        'issuer': 'Amazon Web Services',
        'date': 'June 2023',
        'verification_url': 'https://www.credly.com/badges/aws-certified-solutions-architect-associate'
    },
    {
        'name': 'Microsoft Certified: Azure Fundamentals (AZ-900)',
        'issuer': 'Microsoft',
        'date': 'March 2023',
        'verification_url': 'https://www.credly.com/badges/microsoft-certified-azure-fundamentals'
    },
    {
        'name': 'CompTIA Network+',
        'issuer': 'CompTIA',
        'date': 'January 2022',
        'verification_url': 'https://www.credly.com/badges/comptia-network-ce'
    },
    {
        'name': 'CompTIA A+',
        'issuer': 'CompTIA',
        'date': 'May 2021',
        'verification_url': 'https://www.credly.com/badges/comptia-a-ce'
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                           projects=cloud_projects, 
                           skills=skills, 
                           certifications=certifications)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Simple validation
        if not name or not email or not message:
            flash('Please fill out all fields', 'error')
            return redirect(url_for('index', _anchor='contact'))
        
        try:
            # Create message
            msg = Message(
                subject=f'Portfolio Contact from {name}',
                recipients=[app.config['MAIL_DEFAULT_SENDER']],
                body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                sender=email
            )
            
            # Send email if mail is configured
            if app.config['MAIL_USERNAME'] and app.config['MAIL_PASSWORD']:
                mail.send(msg)
                flash('Your message has been sent. Thank you!', 'success')
            else:
                # Log the message if mail isn't configured
                app.logger.info(f"Contact form submission: {name} ({email}) - {message}")
                flash('Your message has been received. Thank you!', 'success')
                
        except Exception as e:
            app.logger.error(f"Error sending email: {str(e)}")
            flash('There was an error sending your message. Please try again later.', 'error')
            
        return redirect(url_for('index', _anchor='contact'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
