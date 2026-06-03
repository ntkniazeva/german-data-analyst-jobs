# Data Analyst Jobs in Germany

## Project Overview

This project analyzes Data Analyst job postings in Germany using data collected from the Adzuna API.

The goal is to understand:
- how many Data Analyst vacancies are available,
- where they are located,
- which companies hire the most analysts,
- what salary information is available.

## Key Findings

Out of 4000+ data-related job postings, about 200 are Data Analyst positions.

Junior postitions are relatively rare (11%).
 
Most vacancies are concentrated in major cities like Berlin, Hamburg, Cologne, etc.

... are currently hiring the most data analyst.

Salary transparency is limited.

Most reported average salaries are concentrated between €55,000 and €80,000 per year.

## Visualisation 

![Top Cities](visuals/top_cities_by vacancies.png)

## Power BI Dashboard

Interactive Power BI dashboard is available in:

`dashboard/dashboard.pbix `

## Data Source

Source: Adzuna API

Data collection date: June 3, 2026

Records: 4,323 job postings

Key fields:
- title
- company
- location
- description
- salary_min
- salary_max

## Data Preparation

### Filtering

For data collection from the Adzuna API, the keyword **"data"** was used in job titles.

To focus the analysis on Data Analyst positions, the collected dataset was filtered using the following keywords:

- data analyst
- daten analyst
- datenanalyst

The following postings were excluded:

- Weiterbildung
- Bildungsgutschein

### Cleaning

The dataset required preprocessing of the `location` and `company` fields.

These fields were retrieved from the API as JSON objects and stored as strings in the dataset. To extract city and company names, the strings were converted back to dictionaries using Python's `ast` library.

The resulting `city` field contained a mixture of locations. The following cleaning steps were performed:

- removed the value `Deutschland`
- removed federal states
- consolidated major city districts into their corresponding cities (e.g., Mitte → Berlin, Altstadt-Lehel → Munich)

## Project Structure

```text
german-data-jobs-analysis/
├── dashboard/
│   ├── dashboard.pbix
│   ├── key_metrics.csv
│   ├── top_cities.csv
│   └── top_companies.csv
├── data/
│   └── jobs_snapshot.csv
├── notebooks/
│   └── job_analysis.ipynb
├── src/
│   └── collect_data.py
├── visuals/
│   ├── salary_distribution.png
│   ├── top_cities_by_salary.png
│   ├── top_cities_by_vacancies.png
│   ├── top_companies_by_salary.png
│   └── top_companies_by_vacancies.png
├── .gitignore
├── README.md
└── requirements.txt
```

## Tools

- Python
- pandas
- Adzuna API
- Power BI
- GitHub

## Setup

### API Credentials

Get APP_ID and APP_KEY by registering for a free developer account on the Adzuna website.

To run this project, create a `.env` file in the project root directory and add your Adzuna API credentials:

```env
APP_ID = 'your_app_id'
APP_KEY = 'your_app_key'
```

### Install Dependencies

`pip install -r requirements.txt`

### Run Data Collection

`python -m src.collect_data`

### Run Analysis

Open and run:

`notebooks/job_analysis.ipynb`

