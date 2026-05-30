#  AI Code Review & Quality Analyzer

An AI-powered tool that analyzes Python code and GitHub repositories using Machine Learning + Feature Engineering + LLM-based explanations.

It provides:
- Code quality prediction
- File-wise repository analysis
- Repository health score
- AI-generated suggestions
- PDF report download

---

##  Features

###  Code Analysis (Single File)
- Paste Python code
- Predict code quality (Good / Average / Poor)
- Extract code metrics
- AI-generated improvement suggestions
- Visual metrics dashboard

---

###  GitHub Repository Analysis
- Analyze complete GitHub repositories
- Automatically fetch `.py` and `.ipynb` files
- Extract features from each file
- File-wise quality prediction
- Repository-level insights

---

###  File-wise Analysis
- Quality prediction per file
- Maintainability score
- Complexity score
- Visual table of all files

---

### Repository Health Score
- Overall repository health (0–100)
- Based on:
  - Maintainability
  - Complexity
  - Comments
  - Function usage
- Health status indicator:
  - Excellent / Good / Moderate / Poor

---

### AI Repository Review
- LLM-powered explanation using Groq/OpenAI
- Strengths & weaknesses analysis
- Improvement recommendations

---

###  PDF Report Generation
- Download full analysis report
- Includes:
  - Repository summary
  - File-wise analysis table
  - Metrics table
  - Health score
  - AI review

---

##  Tech Stack

- Python
- Streamlit
- Scikit-learn
- XGBoost
- Pandas
- Plotly
- ReportLab (PDF generation)
- GitHub API
- LLM (Groq / OpenAI)

---

##  Project Structure
AI-Code-Review-Quality-Analyzer/
│
├── app.py
├── models/
├── github_integration/
│ └── github_fetcher.py
├── feature_engineering/
├── llm/
├── utils/
│ └── report_generator.py
├── suggestions.py
└── requirements.txt



---

## Installation

```bash
git clone https://github.com/your-username/AI-Code-Review-Quality-Analyzer.git
cd AI-Code-Review-Quality-Analyzer
pip install -r requirements.txt


## Run application

streamlit run app.py


## Requirements
streamlit
pandas
scikit-learn
xgboost
plotly
requests
reportlab
joblib


## Output Example
Code Quality: Good
Repository Health Score: 87/100
File-wise Analysis: Table view
PDF Report: Downloadable


## Future Improvements
    Security vulnerability detection (Bandit)
    GitHub commit history analysis
    Multi-language support (JS, Java)
    AI code auto-fixing suggestions
    Team collaboration dashboard



## Author
Aryan 
AI/ML Developer | Python | Streamlit | LLM Apps

If you like this project

Give it a star ⭐ and share it!