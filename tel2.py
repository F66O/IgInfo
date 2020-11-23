from telebot import TeleBot
import  requests
import time
r=requests.Session()
bot = TeleBot("810863369:AAHo_ve5b4_nD9-hnL2uLe1699drXmFZMrw")
@bot.message_handler(commands=["start"])
def send_welcome(message):
		bot.reply_to(message, text="welcome bot created By @GGVVGG\n(Just send user)")

@bot.message_handler(func=lambda m:True)
def Send_info(message2):
	user = message2.text
	try:
		infos = r.get("https://www.instagram.com/{}/?__a=1".format(user)).json()
		userid = str(infos['logging_page_id'])
		hid = userid.split('_')[1]
		bot.send_message(message2.chat.id,text="id : "+hid)
		time.sleep(0.5)
		bio = str(infos['graphql']['user'].get('biography'))
		bot.send_message(message2.chat.id,text=bio)
		time.sleep(0.5)
		link = str(infos['graphql']['user'].get('external_url'))
		bot.send_message(message2.chat.id, text=link)
		time.sleep(0.5)
		followes = str(infos['graphql']['user'].get('edge_followed_by').get('count'))
		bot.send_message(message2.chat.id, text="followers : "+followes)
		fullname = str(infos['graphql']['user'].get('full_name'))
		bot.send_message(message2.chat.id,text=fullname)
		local = str(infos['graphql']['user'].get('is_business_account'))
		bot.send_message(message2.chat.id,text="is bussiness : "+local)
		joined = str(infos['graphql']['user'].get('is_joined_recently'))
		bot.send_message(message2.chat.id,text="is new : "+joined)
		pic = str(infos['graphql']['user'].get('profile_pic_url'))
		bot.send_photo(message2.chat.id,photo=pic)
		private = str(infos['graphql']['user'].get('is_private'))
		bot.send_message(message2.chat.id,text="is private : "+private)
	except:
		pass
bot.polling(True)
