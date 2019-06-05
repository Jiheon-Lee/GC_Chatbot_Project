from command.command_dobong import *
from command.command_gangseo import *
from command.command_yancheon import *


def proc_stop(bot, update):
    chii.sendMessage("사용해 주셔서 감사합니다.")


def proc_help(bot, update):
    chii.sendMessage('''명령어 목록\n- * 부분에는 구의 이름이 들어갑니다(dobong, gangseo, yangcheon)\n \
    /cctv_*: 전체에 대한 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_life: 생활방범 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
    /cctv_*_child: 어린이보호 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_traffic: 교통단속 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
    /cctv_*_disaster: 재난재해 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_car: 차량방범 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
    /cctv_*_garbage: 쓰레기단속 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n/cctv_*_else: 기타 cctv가 담겨져있는 맵의 링크를 보여줍니다.\n \
    /stop: 챗봇의 사용을 정지합니다.\n''')


chii = CctvBot()
chii.add_handler('stop', proc_stop)
chii.add_handler('help', proc_help)

# dobong command
chii.add_handler('cctv_dobong', proc_cctv_dobong)
chii.add_handler('cctv_dobong_life', proc_cctv_dobong_life)
chii.add_handler('cctv_dobong_child', proc_cctv_dobong_child)
chii.add_handler('cctv_dobong_traffic', proc_cctv_dobong_traffic)
chii.add_handler('cctv_dobong_disaster', proc_cctv_dobong_disaster)
chii.add_handler('cctv_dobong_car', proc_cctv_dobong_car)
chii.add_handler('cctv_dobong_garbage', proc_cctv_dobong_garbage)
chii.add_handler('cctv_dobong_else', proc_cctv_dobong_else)

# gangseo command
chii.add_handler('cctv_gangseo', proc_cctv_gangseo)
chii.add_handler('cctv_gangseo_life', proc_cctv_gangseo_life)
chii.add_handler('cctv_gangseo_child', proc_cctv_gangseo_child)
chii.add_handler('cctv_gangseo_traffic', proc_cctv_gangseo_traffic)
chii.add_handler('cctv_gangseo_disaster', proc_cctv_gangseo_disaster)
chii.add_handler('cctv_gangseo_car', proc_cctv_gangseo_car)
chii.add_handler('cctv_gangseo_garbage', proc_cctv_gangseo_garbage)
chii.add_handler('cctv_gangseo_else', proc_cctv_gangseo_else)

# yancheon command
chii.add_handler('cctv_yangcheon', proc_cctv_yangcheon)
chii.add_handler('cctv_yangcheon_life', proc_cctv_yangcheon_life)
chii.add_handler('cctv_yangcheon_child', proc_cctv_yangcheon_child)
chii.add_handler('cctv_yangcheon_traffic', proc_cctv_yangcheon_traffic)
chii.add_handler('cctv_yangcheon_disaster', proc_cctv_yangcheon_disaster)
chii.add_handler('cctv_yangcheon_car', proc_cctv_yangcheon_car)
chii.add_handler('cctv_yangcheon_garbage', proc_cctv_yangcheon_garbage)
chii.add_handler('cctv_yangcheon_else', proc_cctv_yangcheon_else)

chii.start()
