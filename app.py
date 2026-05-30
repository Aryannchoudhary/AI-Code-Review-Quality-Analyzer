import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Project Modules
from llm.groq_explainer import explain_code_quality
from suggestions import generate_suggestions
from feature_engineering.feature_extractor import extract_features

from github_integration.github_fetcher import (
    get_python_files,
    get_file_content,
    parse_repo_url
)

from utils.report_generator import (
    generate_pdf_report
)

# Load Trained XGBoost Model
model = joblib.load("models/xgboost.pkl")


# Label Mapping
label_map = {
    0: "Average",
    1: "Good",
    2: "Poor"
}


# Streamlit Page Config
st.set_page_config(
    page_title="AI Code Review & Quality Analyzer",
    layout="wide"
)

st.title(" AI Code Review & Quality Analyzer")

st.write(
    "Analyze Python Code or GitHub Repositories using XGBoost + LLM"
)


# Create Tabs
tab1, tab2 = st.tabs(
    [" Code Analysis", " GitHub Repository"]
)


# TAB 1 - USER CODE ANALYSIS
with tab1:

    st.subheader("Python Code Analysis")

    code_input = st.text_area(
        "Paste Python Code",
        height=300
    )

    if st.button("Analyze Code"):

        if code_input.strip() == "":
            st.warning("Please enter code.")

        else:

            # Extract Features
            features = extract_features(code_input)

            if features is None:
                st.error("Feature extraction failed.")

            else:

                feature_df = pd.DataFrame([features])

                # Prediction
                prediction = model.predict(
                    feature_df
                )[0]

                prediction_label = label_map[prediction]

                # Show Prediction
                st.subheader("Prediction")

                st.success(
                    f"Code Quality: {prediction_label}"
                )

                # Suggestions
                st.subheader(
                    "AI Suggestions for Improvement"
                )

                suggestions = generate_suggestions(
                    features
                )

                for suggestion in suggestions:
                    st.write(
                        f"• {suggestion}"
                    )

                # Metrics
                st.subheader(
                    "Extracted Metrics"
                )

                st.dataframe(
                    feature_df
                )

                # Chart
                st.subheader(
                    "Code Metrics Visualization"
                )

                metrics_df = pd.DataFrame({
                    "Metric": feature_df.columns,
                    "Value": feature_df.iloc[0].values
                })

                fig = px.bar(
                    metrics_df,
                    x="Metric",
                    y="Value",
                    title="Extracted Code Metrics"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

                # LLM Explanation
                st.subheader(
                    "AI Explanation"
                )

                with st.spinner(
                    "Generating explanation..."
                ):

                    explanation = explain_code_quality(
                        code_input,
                        prediction_label,
                        features
                    )

                st.write(
                    explanation
                )


# TAB 2 - GITHUB REPOSITORY ANALYSIS
with tab2:

    st.subheader(
        "GitHub Repository Analysis"
    )

    repo_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/user/repository"
    )

    if st.button(
        "Analyze Repository"
    ):

        try:

            # Parse URL
            owner, repo = parse_repo_url(
                repo_url
            )

            st.write("Owner:", owner)
            st.write("Repo:", repo)


            # Get Python Files
            files = get_python_files(
                owner,
                repo
            )

            st.write("Files Found:", len(files))
            st.write(files)

            if len(files) == 0:
                st.error(
                    "No Python files found."
                )

            else:

                st.success(
                    f"Found {len(files)} Python files"
                )

                all_features = []
                file_results= []

                # Analyze first 20 files
                for file_url in files[:20]:

                    code = get_file_content(
                        file_url
                    )

                    if code:

                        features = extract_features(
                            code
                        )

                        if features:
                            all_features.append(
                                features
                            )

                            feature_df = pd.DataFrame(
                                [features]
                            )

                            file_prediction = model.predict(
                                feature_df
                            )[0]

                            file_label = label_map[
                                file_prediction 
                            ]

                            file_results.append({
                                "File": file_url.split("/")[-1],
                                "Quality": file_label,
                                "Maintainability": round(
                                    features.get(
                                        "maintainability", 0
                                        ), 2
                                    ),
                                "Complexity": round(
                                    features.get(
                                        "avg_complexity", 0
                                        ), 2
                                    ),
                            })



                if len(all_features) == 0:

                    st.error(
                        "Feature extraction failed for repository."
                    )

                else:
                    
                    file_df = pd.DataFrame(
                        file_results
                    )

                    st.subheader(
                        "File-Level Analysis"
                    )

                    st.dataframe(
                        file_df,
                        use_container_width=True
                    )

                    repo_df = pd.DataFrame(
                        all_features
                    )

                    
                    # Average Metrics
                    avg_metrics = repo_df.mean()

                    
                    # Repository Health Score Calculation
                    maintainability = avg_metrics.get(
                        "maintainability", 0
                    )

                    complexity = avg_metrics.get(
                        "avg_complexity", 0
                    )

                    comments = avg_metrics.get(
                        "comments", 0
                    )

                    function_count = avg_metrics.get(
                        "function_count", 0
                    )

                    complexity_score = max(
                        0,
                        100 - (complexity * 10)
                    )

                    comments_score = min(
                        100,
                        comments * 10
                    )

                    function_score = min(
                        100,
                        function_count * 20
                    )

                    health_score = round(

                        maintainability * 0.50 +

                        complexity_score * 0.25 +

                        comments_score * 0.15 +

                        function_score * 0.10

                    )

                    avg_df = pd.DataFrame(
                        [avg_metrics]
                    )

                    # Prediction
                    prediction = model.predict(
                        avg_df
                    )[0]

                    prediction_label = label_map[
                        prediction
                    ]
                   
                        
                    # Repository Health Score UI
                    st.metric(
                        "Health Score",
                        f"{health_score}/100"
                    )

                    st.progress(
                        health_score / 100
                    )

                    if health_score >= 85:

                        st.success(
                            "Excellent Repository Health"
                        )

                    elif health_score >= 70:

                        st.info(
                            "Good Repository Health"
                        )

                    elif health_score >= 50:

                        st.warning(
                            "Moderate Repository Health"
                        )

                    else:

                        st.error(
                            "Poor Repository Health"
                        )
                    st.subheader(
                        "Repository Prediction"
                    )

                    st.success(
                        f"Repository Quality: {prediction_label}"
                    )

                    # Metrics
                    st.subheader(
                        "Repository Metrics"
                    )

                    st.dataframe(
                        avg_df
                    )

                    # Chart
                    metrics_df = pd.DataFrame({
                        "Metric": avg_df.columns,
                        "Value": avg_df.iloc[0].values
                    })

                    fig = px.bar(
                        metrics_df,
                        x="Metric",
                        y="Value",
                        title="Repository Metrics"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )

                    # AI Review
                    st.subheader(
                        "AI Repository Review"
                    )

                    with st.spinner(
                        "Generating repository review..."
                    ):

                        explanation = explain_code_quality(
                            "Repository Analysis",
                            prediction_label,
                            avg_metrics.to_dict()
                        )

                    st.write(
                        explanation
                    )

                    pdf_file = generate_pdf_report(

                        repo_url,
                        prediction_label,
                        health_score,
                        explanation
                    )

                    with open(
                        pdf_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label=" Download PDF Report",
                            data=file,
                            file_name=pdf_file,
                            mime="application/pdf"
                        )
                        

        except Exception as e:

            st.error(
                f"Error analyzing repository: {e}"
            )