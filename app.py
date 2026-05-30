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

st.title("🤖 AI Code Review & Quality Analyzer")

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

            # Get Python Files
            files = get_python_files(
                owner,
                repo
            )

            if len(files) == 0:
                st.error(
                    "No Python files found."
                )

            else:

                st.success(
                    f"Found {len(files)} Python files"
                )

                all_features = []

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

                if len(all_features) == 0:

                    st.error(
                        "Feature extraction failed for repository."
                    )

                else:

                    repo_df = pd.DataFrame(
                        all_features
                    )

                    # Average Metrics
                    avg_metrics = repo_df.mean()

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

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )