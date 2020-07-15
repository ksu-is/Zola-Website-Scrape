from bs4 import BeautifulSoup
import request
import csv
from datetime import datetime


source = request.get('https://www.zola.com/wedding/manage/guests/all').text 

soup = BeautifulSoup( source, 'lxml')

zola_guestlist_csv = open ('friesz_wedding October 24, 2020'+'.csv','w')
csv_writer = csv.writer(zola_guestlist_csv)

csv_writer.writerow(['Guest Name', "Number of Guest","Email & Mobile","Mailing Address"])
