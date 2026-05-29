from datasets import load_dataset
import pandas as pd

print("Downloading dataset...")

ds = load_dataset(
    "code-search-net/code_search_net",
    "python",
    split="train[:100000]"
)

print("Dataset downloaded!")

codes = []

for item in ds:

    code = item["whole_func_string"]

    codes.append({
        "code": code
    })

df = pd.DataFrame(codes)

# Save CSV
df.to_csv(
    "data/raw/python_codes.csv",
    index=False
)

print("Dataset saved successfully!")
print(df.head())
print(df.shape)