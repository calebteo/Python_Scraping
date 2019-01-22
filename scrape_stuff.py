
import requests
from bs4 import BeautifulSoup

result = requests.get('https://scss.tcd.ie/internships/')
print('Status of request:' + str(result.status_code))

page = BeautifulSoup(result.content, 'lxml')

f = open("internship.htm", "w+")
f.write(str(page))
print ("Written to file")
