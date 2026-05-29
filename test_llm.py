from llm.ollama_explainer import explain_code_quality

sample_code = """

def test(x):

    if x > 0:
        if x > 10:
            if x > 100:
                print(x)

"""

prediction = "Poor"

features = {
    "complexity": 8,
    "maintainability": 40
}

result = explain_code_quality(
    sample_code,
    prediction,
    features
)

print(result)