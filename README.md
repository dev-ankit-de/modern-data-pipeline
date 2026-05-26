# Simple Data Pipeline

A simple Dockerized data engineering pipeline that:

1. Extracts data from a public API
2. Stores raw JSON data
3. Transforms the data
4. Saves curated CSV output

## Tech Stack

- Python
- Docker
- Pandas
- GitHub Actions (future)
- Airflow/dbt ready

## Run Locally

```bash
docker compose up --build