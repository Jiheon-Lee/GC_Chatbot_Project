import os
import sys
import boto3

import folium
from models import *

from s3_connect import *


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
MAP_DIR = os.path.join(ROOT_DIR, 'map_data')
MAP_FILE = os.path.join(MAP_DIR, 'map1.html')


def connect_database():
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
        secrets['LOCAL_USER_ID'],
        secrets['LOCAL_USER_PASSWORD'],
        secrets['LOCAL_USER_URL'],
        secrets['RDS_PORT'],
        secrets['RDS_DATABASE']
    ))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    return session


def proc_start(bot, update):
    chii.sendMessage("데이터베이스에 접속중입니다.")
    session = connect_database()
    chii.sendMessage("데이터베이스 접속 성공")
    cctv = session.query(Cctv).all()
    chii.sendMessage(cctv[0].address)


def proc_restart(bot, update):
    chii.sendMessage("재접속중.....")
    connect_database()
    chii.sendMessage("데이터베이스 접속 성공")


def proc_rolling(bot, update):
    chii.sendMessage('데구르르..')
    chii.sendMessage('르르..')


def proc_stop(bot, update):
    chii.sendMessage("사용해 주셔서 감사합니다.")


def proc_help(bot, update):
    chii.sendMessage("명령어 목록\n"
                     "/start: 데이터베이스를 연결합니다.\n"
                     "/restart: 데이터베이스를 재 연결합니다.\n"
                     "/stop: 챗봇의 사용을 정지합니다.\n"
                     )

def proc_study(bot, update):
    chii.sendMessage('{}야...공부좀하자....'.format(update.message['chat']['last_name']))


def proc_cctv_dobong(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1).all()
    map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
    for i in range(len(dobong)):
        folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

    map_1.save('templates/map1.html')

    chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")


def proc_cctv_gangseo(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=2).all()
    map = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
    for i in range(len(gangseo)):
        folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map)
    map.save('templates/map1.html')

    chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

def proc_cctv_yangcheon(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=3).all()
    map = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
    for i in range(len(yangcheon)):
        folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map)
    map.save('templates/map1.html')

    chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")


chii = CctvBot()
chii.add_handler('restart', proc_restart)
chii.add_handler('start', proc_start)
chii.add_handler('rolling', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.add_handler('study', proc_study)
chii.add_handler('help', proc_help)
chii.add_handler('cctv_dobong', proc_cctv_dobong)
chii.add_handler('cctv_gangseo', proc_cctv_gangseo)
chii.add_handler('cctv_yancheon', proc_cctv_yangcheon)
chii.start()
