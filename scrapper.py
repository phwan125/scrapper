import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_last_page, extract_indeed_jobs

url = "https://www.indeed.com/jobs?q=python&limit=50"

last_indeed_page = extract_indeed_last_page("python")

indeed_jobs_results = extract_indeed_jobs(last_indeed_page)

print(indeed_jobs_results)