import os
import json

# telegram
import telegram
from telegram.ext import Updater, CommandHandler

# sqlalchemy
from models_sqlarchemy import *

Base = declarative_base()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_DIR = os.path.join(ROOT_DIR, '.secrets')

secrets = json.load(open(os.path.join(SECRET_DIR, "secrets.json")))


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = secrets["admin_id"]
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id=self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()


class CctvBot(TelegramBot):
    def __init__(self):
        self.token = secrets["telegram_access_token"]
        TelegramBot.__init__(self, '텔레그램', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage("데이터베이스에 접속중입니다.")
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
        self.sendMessage("데이터베이스 접속 성공")

        cctv = session.query(Cctv).first()

        self.sendMessage(cctv.city_id)

        self.updater.start_polling()
        self.updater.idle()
