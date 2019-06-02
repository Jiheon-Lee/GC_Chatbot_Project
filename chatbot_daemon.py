import sys
from models import *


def proc_restart(bot, update):
    chii.sendMessage('다시 재 시작 합니다!!')
    chii.start()


def proc_rolling(bot, update):
    chii.sendMessage('데구르르..')
    sound = firecracker()
    chii.sendMessage(sound)
    chii.sendMessage('르르..')


def proc_stop(bot, update):
    chii.sendMessage('치이 봇이 잠듭니다.')
    chii.stop()


def proc_study(bot, update):
    chii.sendMessage('{}야...공부좀하자....'.format(update.message['chat']['last_name']))


def firecracker():
    return '팡팡!'


chii = CctvBot()
chii.add_handler('restart', proc_restart)
chii.add_handler('rolling', proc_rolling)
chii.add_handler('stop', proc_stop)
chii.add_handler('study', proc_study)
chii.start()
