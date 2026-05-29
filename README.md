# AI-Code-Review-Quality-Analyzer

## Overview

AI Code Review & Quality Analyzer is a hybrid AI-powered system that analyzes Python code quality using Machine Learning, AST-based static code analysis, and Large Language Models (LLMs).

The system extracts software engineering metrics from source code, predicts code quality using trained ML models, and provides intelligent code review insights.

---

## Features

* AST-based feature extraction
* Static code quality analysis
* Machine Learning-based prediction
* Random Forest and XGBoost models
* Feature importance visualization
* Streamlit web application
* AI-generated review explanations (local Ollama version)
* Real-world GitHub dataset training
* Automated software quality assessment

---

## Tech Stack

### Frontend

* Streamlit

### Machine Learning

* Scikit-learn
* XGBoost
* Random Forest

### Data Processing

* Pandas
* NumPy

### Static Code Analysis

* AST
* Radon

### Visualization

* Matplotlib

### LLM Integration

* Ollama
* Llama3

---

## Project Architecture

```text
User Code
    │
    ▼
Feature Extraction
(AST + Static Analysis)
    │
    ▼
ML Model (XGBoost)
    │
    ▼
Quality Prediction
    │
    ▼
LLM Explanation (Local Version)
    │
    ▼
Streamlit Web Interface
```



## Dataset

The project uses the CodeSearchNet dataset containing real-world GitHub source code samples.

Dataset Features:

* Cyclomatic Complexity
* Maintainability Index
* Lines of Code
* Comment Density
* Function Count
* Class Count
* Import Count

Dataset Size:

* ~100,000 code samples

---

## Machine Learning Models

The following models were trained and evaluated:

* Random Forest Classifier
* XGBoost Classifier

### Achieved Performance

| Model         | Accuracy |
| ------------- | -------- |
| Random Forest | 99.45%   |
| XGBoost       | 99.50%   |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Aryannchoudhary/AI-Code-Review-Quality-Analyzer.git
```

### Navigate to Project Folder

```bash
cd AI-Code-Review-Quality-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Local LLM Setup (Optional)

Install Ollama:

https://ollama.com/

Run TinyLlama:

```bash
ollama run tinyllama
```

The local version supports AI-generated code review explanations.

---

## Future Scope

* Multi-language support
* IDE integration
* Security vulnerability detection
* Transformer-based code analysis
* Real-time code review
* CI/CD integration
* Automated refactoring suggestions

---

## Project Type

Final Year AI/ML Project
Hybrid AI System
Software Engineering Analytics

---

## Author

Aryan Choudhary

