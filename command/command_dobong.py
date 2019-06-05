import folium

from connect_database import connect_database
from models import *

chii = CctvBot()


def proc_cctv_dobong(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)
        map_1.save('templates/map1.html')
        chii.sendMessage("<a href='http://13.124.61.113:5000/map1'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_life(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=1).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map2.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map2'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_child(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=2).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map3.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map3'>MAP Link</a>", parse_mode="HTML")
    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_traffic(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=3).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map4.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map4'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_disaster(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=4).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map5.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map5'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_car(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=5).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map6.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map6'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_garbage(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=6).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map7.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map7'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")


def proc_cctv_dobong_else(bot, update):
    session = connect_database()
    dobong = session.query(Cctv).filter_by(city_id=1, purpose_id=7).all()
    if dobong:
        map_1 = folium.Map(location=[dobong[1].latitude, dobong[1].longitude], zoom_start=14)
        for i in range(len(dobong)):
            if dobong[i].road_address != '':
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].road_address).add_to(map_1)
            else:
                folium.Marker([dobong[i].latitude, dobong[i].longitude], popup=dobong[i].address).add_to(map_1)

        map_1.save('templates/map8.html')

        chii.sendMessage("<a href='http://13.124.61.113:5000/map8'>MAP Link</a>", parse_mode="HTML")

    else:
        chii.sendMessage("해당되는 데이터가 없습니다. 다른 명령어를 입력 해 주세요!!")
