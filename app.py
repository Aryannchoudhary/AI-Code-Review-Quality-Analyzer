import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

from llm.groq_explainer import explain_code_quality
from suggestions import generate_suggestions
from feature_engineering.feature_extractor import extract_features
# from llm.ollama_explainer import explain_code_quality


# Load Model

model = joblib.load(
    "models/xgboost.pkl"
)


# Label Mapping

label_map = {
    0: "Average",
    1: "Good",
    2: "Poor"
}


# Streamlit UI

st.set_page_config(
    page_title="AI Code Review & Quality Analyzer",
    layout="wide"
)

st.title(" AI Code Review & Quality Analyzer")

st.write(
    "Analyze Python code using ML + LLM"
)


# Code Input
code_input = st.text_area(
    "Paste Python Code",
    height=300
)


# Analyze Button
if st.button("Analyze Code"):

    if code_input.strip() == "":
        st.warning("Please enter code.")
    else:

        
        # Feature Extraction
        features = extract_features(
            code_input
        )

        if features is None:
            st.error(
                "Feature extraction failed."
            )

        else:

            feature_df = pd.DataFrame(
                [features]
            ) 

            
            # Prediction
            prediction = model.predict(
                feature_df
            )[0]


            st.subheader("AI Suggestions for Improvement")
            suggestions = generate_suggestions(features)
            
            for s in suggestions:
                st.write("•", s)


            prediction_label = label_map[
                prediction
            ]

            
            # Display Prediction
            
            st.subheader(
                "Prediction"
            )

            st.success(
                f"Code Quality: {prediction_label}"
            )

            
            # Display Metrics
            st.subheader(
                "Extracted Metrics"
            )

            st.dataframe(feature_df)


            # Metrics Bar Chart

            st.subheader("Code Metrics Visualization")
            metrics_df=pd.DataFrame({
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

            
            # LLM Explanation for local version
            # st.subheader(
            #     "AI Explanation"
            # )

            # with st.spinner(
            #     "Generating explanation..."
            # ):


            #  groq explanation for deployment version
            st.subheader("AI Explanation")
            with st.spinner("Generating explanation..."):


                explanation = explain_code_quality(
                    code_input,
                    prediction_label,
                    features
                )

            st.write(explanation)


            # AI Explanation for deployment version

            # st.subheader(

            #     "AI Explanation "
            # )
            # st.info(
            #     "LLM explanations are available in the local version using Ollama."
            # )
            