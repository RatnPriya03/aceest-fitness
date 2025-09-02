# ACEest_Fitness and Gym Application

## Project Overview
This is a foundational Flask web application for the ACEest_Fitness and Gym startup, developed as part of a DevOps assignment. It demonstrates core DevOps principles including version control, automated testing, containerization, and CI/CD.

## Local Setup
1. Clone the repository:
   `git clone <your_repository_url>`
2. Navigate to the project directory.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run the application:
   `python app.py`

## Running Tests
Ensure you have the required dependencies installed and then run the following command:
`pytest`

## GitHub Actions Pipeline
This project uses GitHub Actions for a CI/CD pipeline.
- The workflow is triggered automatically on every push to the `main` branch.
- It builds a Docker image of the application.
- It runs the Pytest unit tests within the built Docker image to ensure the application's functionality.