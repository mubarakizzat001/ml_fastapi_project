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
- [License](#-license)

---

## 🔍 Overview

**Risk Flag ML Model** is an end-to-end machine learning project that predicts whether a given record carries a financial/operational risk (`Risk_Flag = 1`) or not (`Risk_Flag = 0`).

The project follows a clean, layered ML workflow:

1. **EDA & Experimentation** — Exploratory data analysis inside a Jupyter notebook
2. **Training** — A full Scikit-learn `Pipeline` handles preprocessing + Logistic Regression training
3. **Persistence** — Trained model is serialized with `joblib`
4. **Serving** — FastAPI exposes the trained model as a REST API via a dedicated `service` layer

> ⚡ Preprocessing + model inference are wrapped in a single Scikit-learn `Pipeline` — no manual data transformation is needed at inference time.

---

## 📁 Project Structure

```
ml-fastapi-project/
│
├── main.py                          # FastAPI entry point — defines all API routes
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
│
├── service/                         # Service layer (business logic)
│   ├── __init__.py
│   ├── BaseModel.py                 # Loads the trained model from disk (joblib)
│   └── ModelService.py              # Handles prediction logic (predict + probability)
│
└── ml_model_package/
    ├── data/
    │   ├── Training Data.csv        # Raw training dataset
    │   └── Test Data.csv            # Raw test dataset
    │
    ├── models/
    │   └── risk_flag_model.joblib   # Serialized trained model (Scikit-learn Pipeline)
    │
    └── notebooks/
        └── research_and_development.ipynb   # Full ML workflow: EDA → Training → Evaluation → Export
```

---

## 🛠 Tech Stack

| Layer | Tool | Version |
|---|---|---|
| API Framework | FastAPI | 0.135.3 |
| API Docs UI | Scalar FastAPI | 1.8.2 |
| ML Library | Scikit-learn | 1.8.0 |
| Data Processing | Pandas | 3.0.2 |
| Numerical Computing | NumPy | 2.4.4 |
| Model Persistence | Joblib | 1.5.3 |
| Data Validation | Pydantic Settings | 2.13.1 |
| Visualization (notebook) | Matplotlib + Seaborn | 3.10 / 0.13 |
| Statistical Analysis | SciPy | 1.17.1 |

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

### Step 1 — Train the model (run the notebook)

Open the notebook and run all cells:

```bash
jupyter notebook ml_model_package/notebooks/research_and_development.ipynb
```

This will:
- Load `Training Data.csv`
- Perform EDA (missing values, distributions, correlations)
- Build and train a Scikit-learn pipeline (preprocessing + Logistic Regression)
- Evaluate performance (Classification Report, Confusion Matrix, ROC AUC)
- Serialize the trained model to `ml_model_package/models/risk_flag_model.joblib`

> ⚠️ The API **will not start** if `risk_flag_model.joblib` doesn't exist. You must run the notebook first.

### Step 2 — Start the FastAPI server

```bash
fastapi dev main.py
```

The server will start on `http://127.0.0.1:8000`.

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

The entire preprocessing + model is wrapped in a single Scikit-learn `Pipeline`, so you can call `.predict()` directly on raw input DataFrames — no manual transformation needed.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — returns welcome message |
| `POST` | `/predict` | Run risk prediction on input features |
| `GET` | `/scalar` | Scalar interactive API documentation UI |

### Example: POST `/predict`

**Request body:**
```json
{
  "feature_1": value,
  "feature_2": value,
  "...": "..."
}
```

**Response:**
```json
{
  "Prediction:": 1,
  "Probability:": 0.87
}
```

### Interactive API Documentation

Once the server is running, explore the full docs at:

```
http://127.0.0.1:8000/docs      ← Swagger UI
http://127.0.0.1:8000/redoc     ← ReDoc
http://127.0.0.1:8000/scalar    ← Scalar (modern API docs)
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
Made with ❤️ by <a href="https://github.com/mubarakizzat001">Mubarak</a>
</div>