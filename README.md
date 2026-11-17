# 🌱 AgriWise AI — Smart Crop Recommendation System

**Smarter Farming. Better Decisions.**

AgriWise AI is a machine learning-based crop recommendation web application that suggests suitable crops based on soil nutrient values and environmental conditions.

It uses a **Random Forest Classifier** to analyze input parameters and recommend the most suitable crop.

## 🚀 Features

- 🌾 Crop recommendations based on soil and climate conditions
- 🧪 Soil nutrient analysis (Nitrogen, Phosphorus, Potassium)
- 🌡️ Temperature and humidity inputs
- 🌧️ Rainfall and soil pH analysis
- 📊 Model performance and analytics
- 📱 Responsive Streamlit interface
- 🤖 Machine learning powered predictions

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Number of estimators:** 100
- **Dataset size:** 2,200 records
- **Input features:** 7
- **Target classes:** 22 crop types
- **Train-test split:** 80:20
- **Evaluation:** Accuracy and classification metrics

### Input Features

| Feature | Description |
|---|---|
| N | Nitrogen content |
| P | Phosphorus content |
| K | Potassium content |
| Temperature | Environmental temperature |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall measurement |

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Joblib

## 📂 Project Structure

```text
crop-recommendation-system/
│
├── app.py
├── crop_model.pkl
├── feature_names.pkl
├── evaluation_metrics.json
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shaluei/crop-recommendation-system.git
```

### 2. Navigate into the project

```bash
cd crop-recommendation-system
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

The model uses the Crop Recommendation Dataset containing 2,200 records and 22 crop categories.

Dataset source: [Kaggle — Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

## 🎯 Project Objective

The objective of AgriWise AI is to demonstrate how machine learning can analyze soil and environmental parameters to support crop selection decisions.

## ⚠️ Disclaimer

AgriWise AI is an educational machine learning prototype. Its predictions are based on the dataset used for training and should not be treated as guaranteed agricultural advice. Actual crop suitability also depends on local conditions and expert assessment.

## 👨‍💻 Author

**Shamil**

- GitHub: [@shaluei](https://github.com/shaluei)

---

⭐ If you find this project interesting, consider giving the repository a star!
