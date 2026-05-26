import json
import pandas as pd
from pathlib import Path

RAW_DATA_PATH = "data/raw/products.json"
CURATED_DATA_PATH = "data/curated/products.csv"


def transform_data():
    with open(RAW_DATA_PATH, "r") as file:
        raw_data = json.load(file)

    products = raw_data["products"]

    df = pd.DataFrame(products)

    curated_df = df[
        [
            "id",
            "title",
            "category",
            "price",
            "rating",
            "stock"
        ]
    ]

    Path("data/curated").mkdir(parents=True, exist_ok=True)

    curated_df.to_csv(CURATED_DATA_PATH, index=False)

    print(f"Curated data saved to {CURATED_DATA_PATH}")


if __name__ == "__main__":
    transform_data()