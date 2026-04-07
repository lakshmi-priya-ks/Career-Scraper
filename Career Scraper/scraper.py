import requests
from bs4 import BeautifulSoup
import pandas as pd

jobs = []

for page in range(1, 4):
    url = f"https://internshala.com/jobs/page-{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    job_cards = soup.find_all("div", class_="individual_internship")

    for job in job_cards:
        try:
            title = job.find("a", class_="job-title-href").text.strip()
        except:
            title = "N/A"

        try:
            company = job.find("p", class_="company-name").text.strip()
        except:
            company = "N/A"

        try:
            location = job.find("a", class_="location_link").text.strip()
        except:
            location = "N/A"

        try:
            salary = job.find("span", class_="stipend").text.strip()
        except:
            salary = "N/A"

        try:
            link = "https://internshala.com" + job.find("a", class_="job-title-href")["href"]
        except:
            link = "N/A"

        jobs.append({
            "Job Title": title,
            "Company": company,
            "Location": location,
            "Salary": salary,
            "Job Link": link
        })

df = pd.DataFrame(jobs)
df.to_excel("jobs.xlsx", index=False)

print("✅ Scraping completed. Data saved to jobs.xlsx")
