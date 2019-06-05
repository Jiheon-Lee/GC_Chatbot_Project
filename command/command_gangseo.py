import folium

from connect_database import connect_database
from models import *

chii = CctvBot()


def proc_cctv_gangseo(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_life(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=1).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_child(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=2).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_traffic(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=3).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_disaster(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=4).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_car(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=5).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_garbage(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=6).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_gangseo_else(bot, update):
    session = connect_database()
    gangseo = session.query(Cctv).filter_by(city_id=1, purpose_id=7).all()
    if gangseo:
        map_1 = folium.Map(location=[gangseo[1].latitude, gangseo[1].longitude], zoom_start=14)
        for i in range(len(gangseo)):
            if gangseo[i].road_address != '':
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].road_address).add_to(map_1)
            else:
                folium.Marker([gangseo[i].latitude, gangseo[i].longitude], popup=gangseo[i].address).add_to(map_1)

        map_1.save('templates/map1.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")
