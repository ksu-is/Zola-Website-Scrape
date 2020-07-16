from bs4 import BeautifulSoup
import request
import csv
from datetime import datetime


page = requests.get('https://www.zola.com/wedding/manage/guests/all')

soup = BeautifulSoup(page.content, 'html.parser')
guestlist = soup.find(id='class="main-content table guest-table guests-list__main"')
#print guestlist
print (guestlist)

items = guestlist.find_all(class_='class=class="tooltip-span"')
#print (items[0])

print (items[0].find(class_='class="primary-guest-name"').get_text())
print (items[0].find(class_='class="contact-info guests-list__column"').get_text())


zola_guestlist_csv = open ('friesz_wedding October 24, 2020'+'.csv','w')
csv_writer = csv.writer(zola_guestlist_csv)

csv_writer.writerow(['Guest Name', "Number of Guest","Email & Mobile","Mailing Address"])

#print(soup.prettify())
