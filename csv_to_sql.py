import pandas as pd
import os

from models_sqlarchemy import *
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:kpy680126@localhost:3306/CctvProject')
Base.metadata.create_all(engine)

# 3 - create a new session
Session = sessionmaker(bind=engine)
session = Session()


data_dir = ['seoul_dobong.csv', 'seoul_gangseo.csv', 'seoul_yangcheon.csv']

for file_path in data_dir:
    data = pd.read_csv('data_file/{}'.format(file_path), keep_default_na=False, encoding="cp949", header=None)

    for index in range(1, len(data)):
        cctv = Cctv(
            road_address=data.loc[index][1],
            address=data.loc[index][2],
            num_camera=int(data.loc[index][4]),
            direction=data.loc[index][6],
            days_to_keep=int(data.loc[index][7]),
            latitude=data.loc[index][10],
            longitude=data.loc[index][11],
            data_date=data.loc[index][12]
        )
        if data.loc[index][1] is not '':
            cctv.city_id = session.query(City).filter(City.city_name == (data.loc[index][1]).split(" ")[1])[0].id
        elif data.loc[index][1] is '' and data.loc[index][2] is not '':
            cctv.city_id = session.query(City).filter(City.city_name == (data.loc[index][2]).split(" ")[1])[0].id
        else:
            cctv.city_id = None

        if data.loc[index][0] is '':
            cctv.cityholl_id = None
        else:
            cctv.cityholl_id = (session.query(Cityholl).filter(Cityholl.cityholl_name == (data.loc[index][0]).split(" ")[1]))[0].id
        if data.loc[index][3] is '':
            cctv.purpose_id = None
        else:
            cctv.purpose_id = (session.query(Purpose).filter(Purpose.set_purpose == data.loc[index][3]))[0].id
        if data.loc[index][9] is '':
            cctv.phone_number_id = None
        else:
            cctv.phone_number_id = (session.query(PhoneNumber).filter(PhoneNumber.number == data.loc[index][9]))[0].id

        session.add(cctv)
        session.commit()

    session.close()
    print("{} DB CREATE".format(file_path))
