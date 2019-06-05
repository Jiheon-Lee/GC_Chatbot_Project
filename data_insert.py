from models_sqlarchemy import *
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
    secrets['RDS_USER_ID'],
    secrets['RDS_USER_PASSWORD'],
    secrets['RDS_USER_URL'],
    secrets['RDS_PORT'],
    secrets['RDS_DATABASE']
))
Base.metadata.create_all(engine)

# 3 - create a new session
Session = sessionmaker(bind=engine)
session = Session()

# purpose
life_purpose = Purpose("생활방범")
chird_purpose = Purpose("어린이보호")
traffic_purpose = Purpose("교통단속")
car_purpose = Purpose("차량방범")
disaster_purpose = Purpose("재난재해")
garbage_purpose = Purpose("쓰레기단속")
some_purpose = Purpose("기타")

#city
dobong_city = City("도봉구")
gangseo_city = City("강서구")
yangcheon_city = City("양천구")

#cityholl
dobong_cityholl = Cityholl("도봉구청")
gangseo_cityholl = Cityholl("강서구청")
yangcheon_cityholl = Cityholl("양천구청")

#phone number
dobong_phone_number = PhoneNumber("02-2091-4273")
gangseo_phone_number = PhoneNumber("02-2600-1884")
yangcheon_phone_number = PhoneNumber("02-2620-4793")


session.add(life_purpose)
session.add(chird_purpose)
session.add(traffic_purpose)
session.add(disaster_purpose)
session.add(car_purpose)
session.add(garbage_purpose)
session.add(some_purpose)
session.add(dobong_city)
session.add(gangseo_city)
session.add(yangcheon_city)
session.add(dobong_cityholl)
session.add(gangseo_cityholl)
session.add(yangcheon_cityholl)
session.add(dobong_phone_number)
session.add(gangseo_phone_number)
session.add(yangcheon_phone_number)

session.commit()
session.close()




