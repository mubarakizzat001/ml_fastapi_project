# 💳 ML Finance Risk API

A production-ready **FastAPI** backend that predicts loan risk using a trained **Machine Learning** model. The API accepts user financial data, runs it through an ML classifier, stores the prediction in a **PostgreSQL** database, and returns the result with probability scores.

---

## 🚀 Features

- 🤖 **ML-Powered Predictions** — Classifies loan risk using a pre-trained scikit-learn model
- 📊 **Probability Scores** — Returns confidence probability alongside the binary prediction
- 🗄️ **Async PostgreSQL** — Fully async database operations via SQLAlchemy + asyncpg
- ✅ **Data Validation** — Strict input validation with Pydantic schemas
- 📖 **Scalar API Docs** — Beautiful interactive API documentation at `/scalar`
- ⚡ **FastAPI** — High-performance async web framework

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI 0.135 |
| Database | PostgreSQL (async via asyncpg) |
| ORM | SQLModel + SQLAlchemy 2.0 |
| ML | scikit-learn, pandas, numpy |
| Validation | Pydantic v2 + pydantic-settings |
| API Docs | Scalar FastAPI |

---

## 📁 Project Structure

```
ml-fastapi-project/
├── src/
│   ├── main.py                        # App entry point, lifespan, Scalar docs
│   ├── config.py                      # Database settings from .env
│   ├── requirements.txt
│   ├── .env                           # Environment variables (not committed)
│   │
│   ├── api/
│   │   ├── __init__.py                # Exports schemas, enums, router
│   │   ├── dependencies.py            # Service dependency injection
│   │   ├── router/
│   │   │   └── FinanceAppRouter.py    # CRUD endpoints
│   │   └── schemas/
│   │       ├── FinanceAppSchema.py    # Request/Response Pydantic models
│   │       └── enum/
│   │           └── FinanceAppEnum.py  # maritalstatus, HouseOwnership enums
│   │
│   ├── database/
│   │   ├── model.py                   # FinanceApp SQLModel table
│   │   └── seesion.py                 # Async engine, session factory
│   │
│   ├── service/
│   │   ├── FinanceappService.py       # Business logic (CRUD + ML integration)
│   │   └── ModelService.py            # ML model loading and prediction
│   │
│   └── ml_model_package/
│       ├── data/                      # Training datasets
│       ├── models/                    # Saved model files (.joblib)
│       └── notebooks/                 # Jupyter notebooks for model training
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites

- Python 3.11+
- PostgreSQL running locally

### 2. Clone the repository

```bash
git clone <your-repo-url>
cd ml-fastapi-project
```

### 3. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

### 4. Install dependencies

```bash
cd src
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file inside `src/` based on the example:

```bash
cp .env.example .env
```

Edit `.env` with your PostgreSQL credentials:

```env
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run the development server

```bash
cd src
fastapi dev
```

> The API will be available at: `http://localhost:8000`

---

## 📖 API Documentation

| URL | Description |
|---|---|
| `http://localhost:8000/scalar` | Scalar interactive API docs (recommended) |
| `http://localhost:8000/docs` | Swagger UI |
| `http://localhost:8000/redoc` | ReDoc |

---

## 🔌 API Endpoints

### Base URL: `/financeapp`

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/financeapp/` | Create a prediction & save to DB |
| `GET` | `/financeapp/{id}` | Get a single record by ID |
| `GET` | `/financeapp/?limit=100&offset=0` | Get all records (paginated) |
| `PATCH` | `/financeapp/{id}` | Update a record |
| `DELETE` | `/financeapp/{id}` | Delete a record |

---

### 📥 POST `/financeapp/` — Create Prediction

**Request Body:**

```json
{
  "Income": 50000.0,
  "Age": 35,
  "Experience": 10,
  "marital_status": "Married",
  "House_Ownership": "rented",
  "Car_Ownership": "yes",
  "Profession": "Engineer",
  "CITY": "Cairo",
  "STATE": "Cairo",
  "CURRENT_JOB_YRS": 5,
  "CURRENT_HOUSE_YRS": 3
}
```

**Field Constraints:**

| Field | Type | Constraints |
|---|---|---|
| `Income` | float | `> 0` |
| `Age` | int | `18 – 100` |
| `Experience` | int | — |
| `marital_status` | enum | `"Married"` \| `"Single"` |
| `House_Ownership` | enum | `"rented"` \| `"owned"` \| `"norent_noown"` |
| `Car_Ownership` | str | — |
| `Profession` | str | — |
| `CITY` | str | — |
| `STATE` | str | — |
| `CURRENT_JOB_YRS` | int | — |
| `CURRENT_HOUSE_YRS` | int | — |

**Response (201 Created):**

```json
{
  "Id": 1,
  "prediction": 1,
  "probability": 0.59
}
```

> `prediction`: `1` = High Risk, `0` = Low Risk  
> `probability`: confidence score of the positive class (0.0 – 1.0)

---

## 🗄️ Database Model

Table: `financeapp`

| Column | Type | Description |
|---|---|---|
| `Id` | int (PK) | Auto-increment primary key |
| `Income` | float | Annual income |
| `Age` | int | Applicant age |
| `Experience` | int | Years of experience |
| `marital_status` | enum | Married / Single |
| `House_Ownership` | enum | rented / owned / norent_noown |
| `Car_Ownership` | varchar | Car ownership status |
| `Profession` | varchar | Job title |
| `CITY` | varchar | Current city |
| `STATE` | varchar | Current state |
| `CURRENT_JOB_YRS` | int | Years at current job |
| `CURRENT_HOUSE_YRS` | int | Years at current house |
| `prediction` | int | ML model output (0 or 1) |
| `probability` | float | Prediction confidence score |
| `created_at` | timestamp | Record creation time (UTC) |
| `updated_at` | timestamp | Last update time (UTC) |

---

## 🤖 ML Model

- Loaded at startup via `ModelService`
- Uses `model.predict()` for binary classification
- Uses `model.predict_proba()` for probability scores (if supported by the model)
- Model files stored in `ml_model_package/models/`

---

## 🔒 Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DB_USER` | PostgreSQL username | `app_user` |
| `DB_PASSWORD` | PostgreSQL password | `secret` |
| `DB_NAME` | Database name | `ml_api_db` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |