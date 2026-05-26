from extract import extract_data
from transform import transform_data


def run_pipeline():
    print("Starting pipeline...")

    extract_data()

    transform_data()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()