from bs4 import BeautifulSoup    
import requests
from csv import writer

url = 'https://www.brightermonday.co.ke/jobs'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
jobs = soup.find_all('div', class_='flex items-center')

with open("jobs_application.csv", 'w', encoding="utf-8-sig", newline="") as f:
    thewriter = writer(f)
    header = ['Job Title']
    thewriter.writerow(header)
    
    for job in jobs:
        title_element = job.find('p', class_="text-lg font-medium break-words text-link-500")
        if title_element:
            title = title_element.text.strip()
            info = [title]
            print(title)  # Print only the text content
            thewriter.writerow(info)
