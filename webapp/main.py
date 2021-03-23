from selenium import webdriver
from flask import current_app
import re

from webapp.db import db
from webapp.events.models import Events


driver_path = current_app.config['DRIVER_PATH']
driver = webdriver.Chrome(driver_path)

def save_events(title, url):
    event_data = Events(title=title, url=url)
    db.session.add(event_data)
    db.session.commit()

def collectlinks():
    for page in range(1, 25):
        a, b = 1, 20
        c = 20*page
        a += c
        b += c
        part_1 = current_app.config['URL_PART_1']
        part_2 = current_app.config['URL_PART_2']
        pars_page = f'{part_1}{a}{part_2}{b}'
        driver.get(pars_page)
        competitions = driver.find_elements_by_xpath("//div[@class='row small-up-1 medium-up-2 large-up-3 small-collapse medium-uncollapse']//a")
        for i in competitions:
            data = i.text
            name = data.split('\n')
            serch_round = re.search(r'→', name[0])
            if serch_round is None:
                if re.search(r'Тренировка|Training|Small competition|Малое соревнование', name[0]) is None:
                    print(name[0])
                    url = i.get_attribute('href')
                    title = name[0]
                    save_events(title, url)        
    driver.close()

#def event_data():
#    part_1 = current_app.config['URL_EVENT']
#    part_2 = '1588755'
#    pars_page = f'{part_1}{part_2}'
#    driver.get(pars_page)
