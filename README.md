# Cloud Resume Challenge - Backend

This repository contains the backend infrastructure and API code for my Cloud Resume Challenge implementation using Google Cloud Platform (GCP).

## Features
- Serverless API using Cloud Functions
- Visitor counter using Firestore
- Infrastructure as Code using Terraform
- Automated testing and deployment
- Comprehensive documentation

## Directory Structure
```
cloud-resume-backend/
├── main.py              # Cloud Function code
├── requirements.txt     # Python dependencies
├── tests/              # Python unit tests
├── infrastructure/     # Terraform configurations
├── docs/              # Project documentation
└── cloudbuild.yaml     # Cloud Build configuration
```

## Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   python -m pytest
   ```

3. Deploy infrastructure:
   ```bash
   cd infrastructure
   terraform init
   terraform apply
   ```

## Related Repositories
- Frontend website: [cloud-resume-frontend](https://github.com/mikedominic92/cloud-resume-frontend)

## Technologies Used
- Python
- Google Cloud Functions
- Cloud Firestore
- Terraform
- Cloud Build
- pytest
