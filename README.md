# Network Security Threat Detection

This project is a machine learning-powered application designed to detect and classify network security threats. It provides a RESTful API for training a model and predicting network intrusions based on real-time data.

## 🚀 Features

- **Threat Detection**: Utilizes a machine learning model to identify and classify various types of network security threats.
- **Model Training**: The application supports an API endpoint for triggering the model training pipeline, allowing for continuous improvement of the detection model.
- **Real-time Prediction**: Offers a prediction endpoint that can analyze network data in real time and return a classification of whether the traffic is malicious or benign.
- **Scalable Architecture**: Built with a modular and scalable architecture, making it easy to extend and deploy in various environments.

## ⚙️ Project Structure

The project is organized into the following directories:

- `networksecurity/`: Contains the core source code for the project, including:
  - `components/`: Houses the main components of the machine learning pipeline, such as data ingestion, validation, and transformation.
  - `pipeline/`: Defines the training and prediction pipelines, orchestrating the flow of data and model execution.
  - `entity/`: Contains the entity and configuration objects used throughout the project.
- `templates/`: Includes HTML templates for displaying prediction results.
- `app.py`: The main entry point for the FastAPI application, defining the API endpoints for training and prediction.
- `main.py`: A script for running the machine learning pipeline directly.
- `requirements.txt`: Lists the project's dependencies.
- `setup.py`: The setup script for packaging and distributing the project.
- `Dockerfile`: A file for containerizing the application for easy deployment.

## 🛠️ Technologies Used

- **Python**: The primary programming language for the project.
- **FastAPI**: A modern, high-performance web framework for building APIs.
- **scikit-learn**: A machine learning library for building and training the threat detection model.
- **pandas**: A data manipulation and analysis library.
- **MongoDB**: Used as the database for storing and retrieving network data.
- **Docker**: For containerizing the application for consistent and reliable deployment.

## 📦 Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/network-security-project.git
   cd network-security-project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

To start the application, run the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

This will start the FastAPI server, and you can access the API documentation at http://localhost:8000/docs.

### Training the Model

To train the threat detection model, send a GET request to the `/train` endpoint:

```bash
curl -X GET http://localhost:8000/train
```

### Making Predictions

To make a prediction, send a POST request to the `/predict` endpoint with the network data in a CSV file:

```bash
curl -X POST -F "file=@/path/to/your/data.csv" http://localhost:8000/predict
```
