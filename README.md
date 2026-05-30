#  AI Code Review & Quality Analyzer

An AI-powered system that analyzes Python source code, predicts code quality using Machine Learning, and provides intelligent improvement suggestions using Large Language Models (Groq LLM).

##  Features

###  Code Quality Analysis

* Analyze Python code instantly
* Predict code quality levels:

  *  Good
  *  Average
  *  Poor

### AI-Powered Code Review

* Generates detailed code review explanations
* Identifies maintainability issues
* Highlights complexity concerns
* Suggests code improvements

###  Explainable AI Dashboard

* Displays extracted code metrics
* Feature importance visualization
* Interactive charts and graphs
* Quality prediction confidence

###  Cloud-Based LLM Integration

* Groq API integration
* Fast AI explanations
* No local LLM setup required

###  Streamlit Web Application

* User-friendly interface
* Real-time code analysis
* Interactive visualizations

---

##  Project Architecture

```text
User Input Python Code
            │
            ▼
Feature Extraction Engine
            │
            ▼
Extracted Metrics
(LOC, Complexity, Maintainability, Comments, Functions, Classes)
            │
            ▼
XGBoost Model
            │
            ▼
Quality Prediction
(Good / Average / Poor)
            │
            ▼
Groq LLM
            │
            ▼
AI Explanation & Suggestions
            │
            ▼
Streamlit Dashboard
```

---

##  Extracted Features

The system analyzes:

* Lines of Code (LOC)
* Logical Lines of Code (LLOC)
* Source Lines of Code (SLOC)
* Cyclomatic Complexity
* Maintainability Index
* Number of Functions
* Number of Classes
* Import Statements
* Comments Count

---

##  Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* XGBoost
* Pandas
* NumPy

### AI & LLM

* Groq API
* Llama Models

### Frontend

* Streamlit

### Visualization

* Matplotlib
* Plotly

---

##  Project Structure

```text
AI-Code-Review-Quality-Analyzer/
│
├── app.py
├── models/
│   └── xgboost.pkl
│
├── feature_engineering/
│   └── feature_extractor.py
│
├── llm/
│   └── groq_explainer.py
│
├── data/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Aryannchoudhary/AI-Code-Review-Quality-Analyzer.git
cd AI-Code-Review-Quality-Analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create Streamlit Secrets or Environment Variable:

```toml
GROQ_API_KEY="your_api_key"
```

### Run Application

```bash
streamlit run app.py
```

---

##  Sample Output

### Prediction

```text
Code Quality: Good
```

### AI Explanation

```text
The code demonstrates good maintainability and low complexity.
Consider adding more comments and error handling to improve readability.
```

---

##  Future Scope

* Rule-Based Code Suggestion Engine
* Multi-Language Support
* Security Vulnerability Detection
* Code Smell Detection
* CI/CD Integration
* GitHub Pull Request Review Automation
* Advanced AI Refactoring Suggestions
* Transformer-Based Quality Prediction

---

##  Author

Aryan

### GitHub

https://github.com/Aryannchoudhary

---

##  If you found this project useful, please give it a star!
