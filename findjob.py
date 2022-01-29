import requests
from bs4 import BeautifulSoup
website_url ="https://infopark.in/companies/job-search"
res = requests.get(website_url)
soup = BeautifulSoup(res.text,'lxml')
jobs = soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs:
    title_element = job.find("a")
    title = title_element.text
    link = title_element["href"]
    company_name = job.find("div",{"class":"jobs-comp-name"}).text
    lastdate = job.find("div",{"class":"job-date"}).text
    
   
    print (title)
    print (link)
    print (company_name)
    print (lastdate)
    print ("---------------------------------")
    