<div align="center">

# 🤖 Risk Flag ML Model

### A Machine Learning pipeline for binary risk classification, built with Scikit-learn & served via FastAPI

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Model Details](#-model-details)
- [API Endpoints](#-api-endpoints)
- [Contributing](#-contributing)

---

## 🔍 Overview

**Risk Flag ML Model** is an end-to-end machine learning project that predicts whether a given record carries a financial/operational risk (`Risk_Flag = 1`) or not (`Risk_Flag = 0`).

The project follows a clean ML workflow:

1. **EDA & Experimentation** — Exploratory data analysis inside a Jupyter notebook
2. **Training** — A full Scikit-learn `Pipeline` handles preprocessing + Logistic Regression training
3. **Persistence** — Trained model is serialized with `joblib`
4. **Serving** — FastAPI exposes the trained model as a REST API

> ⚡ The entire preprocessing + model inference is wrapped in a single Scikit-learn `Pipeline`, so no data transformation is needed at inference time.

---

## 📁 Project Structure

```
ml-fastapi-project/
│
├── main.py                          # Entry point — loads model & runs test inference
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
│
└── ml_model_package/
    ├── data/
    │   ├── Training Data.csv        # Raw training dataset
    │   └── Test Data.csv            # Raw test dataset
    │
    ├── models/
    │   └── risk_flag_model.joblib   # Serialized trained model (pipeline)
    │
    └── notebooks/
        └── research_and_development.ipynb   # Full ML workflow: EDA → Training → Evaluation → Export
```

---

## 🛠 Tech Stack

| Layer | Tool | Version |
|---|---|---|
| API Framework | FastAPI | 0.135.3 |
| ML Library | Scikit-learn | 1.8.0 |
| Data Processing | Pandas | 3.0.2 |
| Numerical Computing | NumPy | 2.4.4 |
| Model Persistence | Joblib | 1.5.3 |
| Data Validation | Pydantic Settings | 2.13.1 |
| Visualization | Matplotlib + Seaborn | Latest |

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10+**
- `pip` or a virtual environment manager

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ml-fastapi-project.git
cd ml-fastapi-project
```

### 2. Create & activate a virtual environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
# Edit .env as needed
```

---

## 💡 Usage

### Option A — Train the model (run the notebook)

Open the notebook and run all cells:

```bash
jupyter notebook ml_model_package/notebooks/research_and_development.ipynb
```

This will:
- Load `Training Data.csv`
- Perform quick EDA (missing values, distributions, correlations)
- Build and train a Scikit-learn pipeline (preprocessing + Logistic Regression)
- Evaluate performance (Classification Report, Confusion Matrix, ROC AUC)
- Serialize the trained model to `ml_model_package/models/risk_flag_model.joblib`

### Option B — Run a quick inference test

After training the model, run:

```bash
python main.py
```

This will load the saved model, pick one sample from `Test Data.csv`, and print:
- Sample input features
- Predicted label (`0` or `1`)
- Predicted probability

### Option C — Start the FastAPI server

```bash
fastapi dev main.py
```

Visit the interactive docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | Logistic Regression |
| Class Weighting | `balanced` (handles class imbalance) |
| Numeric Preprocessing | Median Imputation → Standard Scaling |
| Categorical Preprocessing | Most-Frequent Imputation → One-Hot Encoding |
| Train/Test Split | 80% / 20% (stratified) |
| Random State | 42 |
| Serialization | `joblib` |

The entire preprocessing + model is wrapped in a single Scikit-learn `Pipeline`, meaning you can call `.predict()` directly on raw input DataFrames without any manual transformation.

---

## 🌐 API Endpoints

> API route definitions are in `main.py` / FastAPI router.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/predict` | Run risk prediction on input features |

Once the server is running, explore the full interactive API documentation at:

```
http://127.0.0.1:8000/docs      ← Swagger UI
http://127.0.0.1:8000/redoc     ← ReDoc
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'feat: add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ by <a href="https://github.com/your-username">Mubarak</a>
</div>
