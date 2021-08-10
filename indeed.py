import requests
from bs4 import BeautifulSoup

LIMIT = 5
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_last_page(target):
    url = f"https://www.indeed.com/jobs?q={target}&limit=50"
    indeed_results = requests.get(url)
    indeed_html = indeed_results.text
    indeed_soup = BeautifulSoup(indeed_html, 'html.parser')

    count = indeed_soup.find('div', {"id":"searchCountPages"})
    if count:
        count_str = count.string
        index_of = count_str.index("of")
        index_jobs = count_str.index("jobs")
        count_result = count_str[index_of+3: index_jobs].replace(",","")
        print(count_result)
        
        url_last = url + "&start=" + count_result
        last_page = requests.get(url_last)
        last_page_html = last_page.text
        last_page_soup = BeautifulSoup(last_page_html, 'html.parser')

        last_num = last_page_soup.find('ul', {"class":"pagination-list"}).find('b').string
        last_num = int(last_num)
        print(last_num)
        return last_num
    else:
        print("sorry.. no result")


def extract_indeed_jobs_detail(container):
    title =  container.find("h2",{"class":"jobTitle"}).find('span',title=True).string
    company_list =  container.find("span",{"class":"companyName"})
    location = container.select_one("pre > div").text
    print(location)
    if company_list.find('a'):
        company = company_list.find('a').string   
    else:
        company = company_list.string
    return{
        "title":title,
        "company":company,
        "location":location
    }

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(0,2):
        url = f"{URL}&start={page*LIMIT}"
        indeed_results = requests.get(url)
        indeed_html = indeed_results.text
        indeed_soup = BeautifulSoup(indeed_html, 'html.parser')
        containers = indeed_soup.find_all('a',{"class":"result"})
        for container in containers:
            result = extract_indeed_jobs_detail(container)
            jobs.append(result)
    return(jobs)