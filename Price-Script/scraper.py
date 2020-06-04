import requests
from bs4 import BeautifulSoup
import smtplib
import time
from helpers import sTimes

URL = 'https://tonaton.com/en/ad/range-rover-velar-p250-percent-acc-free-2019-for-sale-accra'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.ehlo()

    server.login('paa100193@gmail.com', 'Stevie93!!!')

    subject = 'Price reduced'
    body = 'Check ' + URL
    msg = f'Subject: {subject} \n\n {body} '
    server.sendmail('paa100193@gmail.com', 'stevefmanso@gmail.com', msg)

    if(server.sendmail):
        print('Success!')
    else:
        print('Something went wront')

    server.quit()


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("h1", {"class": "title--3s1R8"}).get_text()
    price = soup.find("div", {"class": "amount--3NTpl"}).get_text()
    convPrice = float(''.join(filter(str.isdigit, price)))
    fixedPrice = float(465000)

   # if (convPrice < fixedPrice):
   # send_mail()

    print()
    print('vehicle' + title)
    print('Current Price: '+str(convPrice))
    print('Expected Price: '+str(fixedPrice))


for sTime in sTimes:
    print(sTime)

while(True):
    check_price()
    time.sleep(sTimes[0])
