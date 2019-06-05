import folium

from connect_database import connect_database
from models import *

chii = CctvBot()


def proc_cctv_yangcheon(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_life(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=1).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_child(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=2).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_traffic(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=3).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_disaster(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=4).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_car(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=5).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_garbage(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=6).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_yangcheon_else(bot, update):
    session = connect_database()
    yangcheon = session.query(Cctv).filter_by(city_id=1, purpose_id=7).all()
    if yangcheon:
        map_1 = folium.Map(location=[yangcheon[1].latitude, yangcheon[1].longitude], zoom_start=14)
        for i in range(len(yangcheon)):
            if yangcheon[i].road_address != '':
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].road_address).add_to(map_1)
            else:
                folium.Marker([yangcheon[i].latitude, yangcheon[i].longitude], popup=yangcheon[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")
