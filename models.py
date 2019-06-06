
# telegram
import telegram
from telegram.ext import Updater, CommandHandler

# sqlalchemy
from models_sqlarchemy import *


class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = secrets["admin_id"]
        self.name = name

    def sendMessage(self, text, parse_mode=None):
        self.core.sendMessage(chat_id=self.id, text=text, parse_mode=parse_mode, disable_web_page_preview=False)

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
        self.sendMessage('''명령어 목록\n- * 부분에는 구의 이름이 들어갑니다(dobong, gangseo, yangcheon)\n \
            /cctv_*: 전체에 대한 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_life: 생활방범 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
            /cctv_*_child: 어린이보호 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_traffic: 교통단속 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
            /cctv_*_disaster: 재난재해 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_car: 차량방범 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
            /cctv_*_garbage: 쓰레기단속 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_else: 기타 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
            /stop: 챗봇의 사용을 정지합니다.\n''')
        
        self.updater.start_polling()
        self.updater.idle()
