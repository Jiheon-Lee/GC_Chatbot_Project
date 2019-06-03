import sys
from models import *


def connect_database():
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(
        secrets['RDS_USER_ID'],
        secrets['RDS_USER_PASSWORD'],
        secrets['RDS_USER_URL'],
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
    sound = firecracker()
    chii.sendMessage(sound)
    chii.sendMessage('르르..')


def proc_stop(bot, update):
    chii.sendMessage("사용해 주셔서 감사합니다.")


def proc_study(bot, update):
    chii.sendMessage('{}야...공부좀하자....'.format(update.message['chat']['last_name']))


def firecracker():
    return '팡팡!'


def cctv(bot, update):
    chii.sendMessage("")


chii = CctvBot()
chii.add_handler('restart', proc_restart)
chii.add_handler('start', proc_start)
chii.add_handler('rolling', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.add_handler('study', proc_study)
chii.start()
