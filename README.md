# Data Analyst Jobs in Germany

This project analyzes Data Analyst job postings in Germany using data collected from the Adzuna API.

The goal is to understand:
- how many Data Analyst vacancies are available,
- where they are located,
- which companies hire the most analysts,
- what salary information is available,
- which cities appear most often.

## Tools

- Python
- pandas
- Adzuna API
- Power BI
- GitHub

## Project Structure

```text
german-data-jobs-analysis/
├── data/
│   └── jobs_snapshot_27-05-2026.csv
├── dashboard/
│   ├── dashboard.pbix
│   ├── key_metrics.csv
│   ├── top_cities.csv
│   └── top_companies.csv
├── visuals/
│   ├── salary_distribution.png
│   ├── top_cities_by_vacancies.png
│   ├── top_companies_by_vacancies.png
│   ├── top_cities_by_salary.png
│   └── top_companies_by_salary.png
├── notebooks/
│   └── job_analysis.ipynb
├── src/
│   └── collect_data.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Dashboard

The Power BI dashboard includes KPI cards, city distribution, salary availability, and a map of job postings in Germany.
