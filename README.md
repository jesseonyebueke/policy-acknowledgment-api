# Policy Acknowledgment API

## Overview
This project is a RESTful API built with Django and Django REST Framework for managing policy acknowledgments. It was developed as a technical project for SEN310 at the Federal University of Technology, Owerri.

## Features
- Exposes the current policy via `GET /api/current-policy/`
- Accepts policy acknowledgments via `POST /api/acknowledge/`
- Automated timestamping and data validation
- Comprehensive audit test suite ensuring system integrity

## Prerequisites
- Python 3.8 or higher
- `pip` (Python package installer)

## Installation & Setup

1. **Download the repository** to your local machine and open your terminal.
2. **Navigate to the project root directory** (where `manage.py` is located):
   ```bash
   cd policyproject
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```
6. The API will now be running at `http://127.0.0.1:8000/`. You can interact with the endpoints at:
   - `GET http://127.0.0.1:8000/api/current-policy/`
   - `POST http://127.0.0.1:8000/api/acknowledge/`

## Running Audit Tests
To execute the automated test suite, run the following command in your terminal:
```bash
python manage.py test policy
```
This will run the 4 test cases ensuring the API logic and validation remain intact.

## Author
**Onyebueke Jesse Chibuikem**  
Reg No: 20231370432 | Serial No: 193 | Topic No: 98
