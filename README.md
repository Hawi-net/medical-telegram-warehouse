# Medical Telegram Data Warehouse

## Project Overview

This project builds an end-to-end data pipeline for collecting, storing, and transforming Telegram data from Ethiopian medical-related channels. The pipeline extracts raw messages and images, stores them in a data lake, loads the data into PostgreSQL, and transforms it into a dimensional data warehouse using dbt.

## Project Structure

```text
medical-telegram-warehouse/
├── data/
│   ├── raw/
│   │   ├── telegram_messages/
│   │   └── images/
├── logs/
├── src/
│   ├── scraper.py
│   └── load_to_postgres.py
├── medical_warehouse/
│   ├── models/
│   │   ├── staging/
│   │   └── marts/
│   ├── tests/
│   ├── dbt_project.yml
│   └── profiles.yml
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Task 1 – Data Scraping

* Connected to the Telegram API using Telethon.
* Scraped public Ethiopian medical Telegram channels.
* Extracted message ID, date, text, views, forwards, and media information.
* Downloaded images for messages containing photos.
* Stored raw JSON files in the data lake.

## Task 2 – Data Warehouse

* Loaded raw JSON data into PostgreSQL.
* Built a dbt project for data transformation.
* Created a staging model (`stg_telegram_messages`).
* Designed a star schema with:

  * `dim_channels`
  * `dim_dates`
  * `fct_messages`
* Added dbt tests (`unique`, `not_null`, and `relationships`).
* Implemented a custom data quality test.
* Generated dbt documentation.

## Technologies Used

* Python
* Telethon
* PostgreSQL
* Docker
* dbt
* Git & GitHub

## How to Run

1. Install the required Python packages.
2. Configure the `.env` file with your Telegram API credentials.
3. Start PostgreSQL using Docker.
4. Run the scraper to collect Telegram data.
5. Load the raw data into PostgreSQL.
6. Execute dbt models:

```bash
dbt run --profiles-dir .
dbt test --profiles-dir .
dbt docs generate --profiles-dir .
```

## Project Status

* Task 1: Completed
* Task 2: Completed
