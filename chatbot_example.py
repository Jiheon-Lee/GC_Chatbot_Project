import telegram

chii_token = '853959315:AAHQ-GjInWw5uCe14SVvEv8eX3p0LKVf3Mk'
chii = telegram.Bot(token = chii_token)
updates = chii .getUpdates()
for u in updates:
    print(u.message.chat['id'])
    print(u.message.text)



# chii_token = '853959315:AAHQ-GjInWw5uCe14SVvEv8eX3p0LKVf3Mk'
# bot = telegram.Bot(token = chii_token)
#
# sid = 827056718
# sent = bot.sendMessage(sid, u'디비 클래스 좋아')
# print(sent)
