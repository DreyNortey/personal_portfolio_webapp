# Andrews Nortey's Portfolio Website

A minimal, responsive personal portfolio website built with Flask to showcase my skills, projects, and experience as an IT Support professional transitioning to Cloud Computing.

## Features

- Responsive design that works on mobile, tablet, and desktop devices
- Clean, modern UI with intuitive navigation
- Sections for About, Skills, Cloud Projects, Certifications, and Contact
- Functional contact form with email integration
- Gallery of cloud projects with custom SVG illustrations

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Email Integration**: Flask-Mail
- **Responsive Design**: Custom CSS with responsive breakpoints
- **Deployment**: Replit

## Project Structure

```
portfolio-website/
├── app.py                  # Main Flask application logic
├── main.py                 # Entry point for the web server
├── static/                 # Static assets
│   ├── css/                # CSS stylesheets
│   ├── js/                 # JavaScript files
│   ├── images/             # Project images and SVGs
│   └── resume/             # Resume PDF
├── templates/              # HTML templates
│   ├── base.html           # Base template with common elements
│   └── index.html          # Main content template
└── README.md               # Project documentation
```

## Cloud Projects Showcased

1. **AWS EC2 Project**: Virtual server deployment and management
2. **S3 Data Lifecycle Management**: Data storage and lifecycle policies
3. **AWS VPC**: Custom virtual private cloud configuration
4. **Microsoft 365 User Management**: User administration and access control

## Professional Certifications

- AWS Certified Solutions Architect - Associate
- AWS Certified Cloud Practitioner
- Microsoft Certified: Azure Fundamentals (AZ-900)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/DreyNortey/personal_portfolio_webapp.git
   cd personal_portfolio_webapp
   ```

2. Install the required packages:
   ```
   pip install flask flask-mail flask-sqlalchemy gunicorn email-validator
   ```

3. Run the application:
   ```
   python main.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Contact

For inquiries or collaboration opportunities, feel free to use the contact form on the website or connect with me directly through GitHub.

## License

This project is open source and available under the [MIT License](LICENSE).