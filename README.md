# FIP Matrix App

A Streamlit-based interactive application for visualizing FAIR convergence data from nanopublications.

## 🔁 Data Synchronization

This app automatically fetches the latest `new_matrix.csv` from the [peta-pico/dsw-nanopub-api](https://github.com/peta-pico/dsw-nanopub-api) repository every hour using GitHub Actions.  
The CSV is saved in the `data/` directory and used live in the app.

## 📦 Structure

```
.
├── main.py                  # Streamlit app
├── utils.py                 # Data logic
├── config.py                # Color / value mappings
├── data/
│   └── new_matrix.csv       # Auto-updated data file
├── Dockerfile
├── docker-compose.yml
├── docker-compose.override.yml.template
└── .github/workflows/
    └── sync_fip_matrix.yml  # Data sync workflow
```

## 🐳 Run with Docker (recommended)

Requires Docker and Docker Compose.

```bash
docker compose up -d
```

The app is then available at http://localhost:8501.

To override defaults (port, environment variables, bind mounts), copy the
template and edit the copy — Compose merges it automatically:

```bash
cp docker-compose.override.yml.template docker-compose.override.yml
```

Stop and remove the container with:

```bash
docker compose down
```

## 🚀 Run locally (without Docker)

```bash
pip install -r requirements.txt
streamlit run main.py
```
