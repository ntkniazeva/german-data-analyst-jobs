# Data Analyst Jobs in Germany

## Project Overview

This project analyzes Data Analyst job postings in Germany using data collected from the Adzuna API.

The goal is to understand:
- how many Data Analyst vacancies are available,
- where they are located,
- which companies hire the most analysts,
- what salary information is available,
- which cities appear most often.

## Key Findings

Most vacancies are concentrated in 
Junior postitions are relatively rare.
Salary transparency is limited
Most reported average salaries are concentrated between €55,000 and €80,000 per year
Among vacancies containing salary information, the highest reported salaries were observed in the following companies
If salary is the main criterion, focus on these cities and employers. the highest average salaries

## Dashboard Preview

![Top Cities](visuals/top_cities_by vacancies.png)

## Data

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

## Dashboard

The Power BI dashboard is available in:

`dashboard/dashboard.pbix `

The Power BI dashboard includes KPI cards, city distribution, salary availability, and a map of job postings in Germany.



Location data contained a mixture of cities, districts, federal states, and administrative regions. Major districts of Berlin, Munich, Hamburg, Cologne, Frankfurt, and Düsseldorf were consolidated into their corresponding cities to improve analytical accuracy.
