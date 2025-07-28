# End-to-End Text Summarization NLP Project

This repository hosts a complete, end-to-end NLP project designed to summarize long-form text. The project is engineered with a modular architecture and follows modern MLOps best practices. It features a sophisticated pipeline for data ingestion, validation, transformation, model training, and evaluation. The final summarization model is served via a Flask web application and is containerized with Docker for seamless deployment.

-----

## 📜 About the Project

This project serves as a comprehensive showcase of the entire lifecycle of an NLP model, from initial data handling to deployment as a live web service. The primary objective is to generate concise and coherent summaries from lengthy text documents. The project is designed for reproducibility, scalability, and easy extension.

The core of this project is a machine learning pipeline that automates the following key stages:

  * **Data Ingestion**: Fetches and loads the dataset from its source.
  * **Data Validation**: Verifies the integrity and format of the input data against a predefined schema.
  * **Data Transformation**: Cleans and preprocesses the text data to make it suitable for the model.
  * **Model Training**: Fine-tunes a pre-trained Transformer model (e.g., PEGASUS from Google) on the text summarization task.
  * **Model Evaluation**: Assesses the performance of the trained model using NLP metrics like ROUGE scores.

-----

## ✨ Features

  * **Modular Project Structure**: The codebase is logically organized into distinct modules, promoting maintainability and ease of collaboration.
  * **Automated NLP Pipeline**: A fully automated pipeline manages every step of the workflow, from data acquisition to model evaluation.
  * **Configuration-Driven**: The entire pipeline is controlled through external configuration files (`config.yaml`, `params.yaml`, `schema.yaml`), allowing for easy adjustments without altering the source code.
  * **Experiment Tracking with MLflow**: Integrates seamlessly with MLflow to log experiments, track parameters, compare metrics (like ROUGE scores), and version models.
  * **Interactive Web Application**: A user-friendly web interface built with Flask allows users to input their text and receive a generated summary in real-time.
  * **Containerization with Docker**: The application is containerized using Docker, which guarantees portability and simplifies deployment across various environments.
  * **Jupyter Notebooks for Research**: Includes detailed Jupyter notebooks that document the research, experimentation, and development process for each pipeline stage.

-----

## 🚀 Getting Started

### Prerequisites

  * Python 3.8+
  * MLflow
  * DVC (for data versioning)
  * Docker

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/rohan-thoma/Text-Summarization-NLP-Project.git
    cd Text-Summarization-NLP-Project
    ```
2.  **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

-----

## 🏃‍♀️ Usage

### Running the ML Pipeline

To execute the complete NLP training pipeline, run the `main.py` script from the project's root directory:

```sh
python main.py
```

This command will trigger all stages of the pipeline in sequence: data ingestion, validation, transformation, model training, and evaluation.

### Running the Web Application

To start the Flask web application for text summarization:

```sh
python app.py
```

The application will be available at `http://localhost:8080`. You can use the web interface to paste your text and get a summarized version.

-----

## 🤖 CI/CD Workflow

This project is equipped with a Continuous Integration/Continuous Deployment (CI/CD) pipeline using **GitHub Actions**. The workflow is defined in the `.github/workflows/main.yaml` file and automates the development lifecycle to ensure code quality and deployment readiness.

The CI/CD pipeline consists of two main jobs:

1.  **`build-and-test`**:

      * **Trigger**: This job runs automatically on every `push` and `pull_request` event to the `main` branch.
      * **Actions**:
          * Checks out the repository's code.
          * Sets up a Python 3.8 environment.
          * Installs all necessary dependencies from `requirements.txt`.
          * Runs the test suite to validate the code and ensure that new changes do not break existing functionality.

2.  **`build-and-publish`**:

      * **Trigger**: This job runs only after the `build-and-test` job completes successfully.
      * **Actions**:
          * Logs in to Docker Hub using `DOCKER_USERNAME` and `DOCKER_PASSWORD` stored as repository secrets.
          * Builds the Docker image of the Flask application using the `Dockerfile`.
          * Pushes the newly built image to Docker Hub, making it available for deployment. The image is tagged for easy identification.

This automated workflow ensures that every change is thoroughly tested and that a fresh, deployable Docker image is published only when all checks pass, promoting a reliable and efficient development process.

-----

## 📁 Project Structure

```
.
├── .github/workflows/main.yaml
├── artifacts/
├── config/
│   └── config.yaml
├── research/
├── src/
│   └── textSummarizer/
│       ├── __init__.py
│       ├── components/
│       ├── config/
│       ├── constants/
│       ├── entity/
│       ├── pipeline/
│       └── utils/
├── templates/
│   └── index.html
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── main.py
├── params.yaml
├── README.md
├── requirements.txt
├── schema.yaml
└── setup.py
```

-----
## 📃 Workflow structure followed

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

-----
## 🛠️ Technologies Used

  * **Python**: Core programming language.
  * **Hugging Face Transformers**: For accessing state-of-the-art pre-trained NLP models.
  * **PyTorch** / **TensorFlow**: As the backend for model training.
  * **Pandas**: For data manipulation.
  * **NLTK** & **spaCy**: For text preprocessing tasks.
  * **MLflow**: For experiment tracking and model management.
  * **Flask**: For building the interactive web application.
  * **Docker**: For containerizing the application.
  * **GitHub Actions**: For the CI/CD pipeline.
  * **DVC**: For data versioning.
  * **Jupyter Notebook**: For research and experimentation.

