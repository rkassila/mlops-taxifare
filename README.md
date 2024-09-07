# Taxifare Prediction API

Build, deploy, and manage a machine learning model to predict taxi fares using FastAPI, Docker, MLflow, and Prefect.

## Project Overview

This project creates a prediction API for a taxi fare model using FastAPI. It leverages Docker for containerization, MLflow for model tracking and management, and Prefect for orchestrating the workflow. The API is deployed on Google Cloud Run for production use.

### Key Features

- **FastAPI**: Expose the taxi fare prediction model via HTTP endpoints.
- **MLflow**: Track and manage the machine learning lifecycle.
- **Prefect**: Automate and orchestrate the model training and deployment pipeline.
- **Docker**: Containerize the API for consistent and scalable deployment.
- **Google Cloud Run**: Deploy the Docker container to make the API publicly accessible.

### Setup

1. **Install Dependencies**: Clone the repo, set up a virtual environment, and install dependencies.
2. **Run API Locally**: Use Uvicorn to test the API on your machine.
3. **Model Management**: Utilize MLflow to track and manage model versions.
4. **Workflow Orchestration**: Use Prefect to automate the model lifecycle.
5. **Dockerize**: Build and run the Docker image locally.
6. **Deploy to Cloud**: Push the image to Google Cloud Run for production deployment.
