import os
from pathlib import Path
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")


params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 50,
    "title_only": 'data',
}


jobs = []  #a list of all vacancies
page = 1

while True:
    url = f"https://api.adzuna.com/v1/api/jobs/de/search/{page}"
    response = requests.get(url, params=params, timeout=30)

    print(f"Page {page}, status code: {response.status_code}")
    print(response.text[:500])

    response_dict = response.json()
    response_job_posts = response_dict["results"]
    if len(response_job_posts) == 0:
        break
    jobs.extend(response_job_posts)
    print(f"Page {page} downloaded.")
    page += 1

data = pd.DataFrame(jobs)

result_path = Path("data/jobs_snapshot.csv")
result_path.parent.mkdir(parents=True, exist_ok=True)

data.to_csv(result_path, index=False)
print(f"Saved {len(data)} jobs to {result_path}")
