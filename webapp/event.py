import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import flash

from webapp.db import db
from webapp.events.models import Events


BASE = 'https://discgolfmetrix.com/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36', 'accept': '*/*'}

def get_html(url, params=None):
    try:
        r = requests.get(url, headers=HEADERS, params=params)
        return r
    except(requests.RequestException, ValueError):
        return False

def get_content(html, url, category):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('div', class_='main-title').text
    location = soup.find('ul', class_='main-header-meta').find('a').text
    dates = soup.find('ul', class_='main-header-meta').find('li').text
    i = dates.split(' ')
    #print(f'Начало: {i[5]}, окончание: {i[7]}')
    start_date = i[5]
    status = 0
    try:
        start_date = datetime.strptime(start_date, '%m/%d/%y')
        if datetime.now() < start_date:
            status = 'upcoming'
        else:
            status = 'past'
    except ValueError:
        print("Исправить запись даты события")
    notes = soup.find('ul', class_='main-header-meta').text.split('Comment: ')
    note = notes[-1]
    all_info = soup.find_all('p')
    text = []
    for i in all_info:
        text.append(i.text)
    info = ' '.join(text)
    save_event(title, url, category, status, start_date, location, note, info)
    flash('Событие успешно добавлено в базу')

def save_event(title, url, category, status, start_date, location, note, info):
    event_event = Events(title=title, url=url, category=category, status=status, start_date=start_date, location=location, note=note, info=info)
    db.session.add(event_event)
    db.session.commit()

def event_data(url, category):
    html = get_html(url)
    if html.status_code == 200:
        get_content(html.text, url, category)
        print(3)
    else:
        print("Error")
