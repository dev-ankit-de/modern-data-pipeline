import requests
import json
from pathlib import Path

RAW_DATA_PATH = "data/raw/products.json"


def extract_data():
    url = "https://dummyjson.com/products"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    Path("data/raw").mkdir(parents=True, exist_ok=True)

    with open(RAW_DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Raw data saved to {RAW_DATA_PATH}")


if __name__ == "__main__":
    extract_data()