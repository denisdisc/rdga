from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
DRIVER_PATH = '/MAIN/Coding/Utils/chromedriver'
URL_PART_1 = 'https://discgolfmetrix.com/?u=competitions&view=&competition_name=&period=&date1=2020-01-01&date2=2020-12-31&my_country=&registration_open=&registration_date1=&registration_date2=&country_code=RU&my_club=&club_type=&club_id=&close_to_me=&area=&city=&course_id=&type=&division=&my=&view=&sort_name=&sort_order=&my_all=&from='
URL_PART_2 = '&to='
URL_EVENT = 'https://discgolfmetrix.com/'

REMEMBER_COOKIE_DURATION = timedelta(days=90)

SECRET_KEY = 'awkdy4iqwrut4qifuyqrtqcuyft4dl'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# https://edgc2020.com/
# export FLASK_APP=webapp && export FLASK_ENV=development && flask run
