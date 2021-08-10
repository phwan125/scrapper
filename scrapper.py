import requests
from bs4 import BeautifulSoup

target = "watch"
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
    print(last_num)
else:
    print("sorry.. no result")


