from telebot import TeleBot
import  requests
import time
import secrets
import uuid,random,string

session = requests.Session()
cke = secrets.token_hex(8)*2
#...
uud4 = uuid.uuid4()
#...
uud1 = uuid.uuid1()
xx = string.ascii_lowercase+string.digits
bot = TeleBot("1478396284:AAEtHCurxAOPh_yfy4ZLZryF_nDnxopSt3o")
@bot.message_handler(commands=["start"])
def send_welcome(message):
		bot.reply_to(message, text="welcome bot created By @GGVVGG\n(Just send user)")

@bot.message_handler(func=lambda m:True)
def Send_info(message2):
    user = message2.text
    try:
        url2 = 'https://i.instagram.com/api/v1/accounts/create/'
        headers = {
        'Host':'i.instagram.com',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language':'en-US',
        'User-Agent':'Instagram 35.0.0.20.96 Android (28/9; 480dpi; 1080x2137; HUAWEI; JKM-LX1; HWJKM-H; kirin810; en_US; 216815344)',
        'X-Pigeon-Session-Id':str(uud1),
        'X-IG-Device-ID':str(uud4),
        'X-IG-App-Locale': 'en_US',
        'X-IG-Device-Locale': 'en_US',
        'X-IG-Mapped-Locale': 'en_US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw8='
    }
        data = {
            'device_id':uud1,
        'email': str(''.join(random.choice(xx)for i in range(12))+'@gmail.com'),
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format("Hello1010weq"),
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'username': user,
        'first_name': 'SUPER STRNG V1',
        'client_id': uud1,
        'seamless_login_enabled': 0,
        'opt_into_one_tap': 'false'
        }
        req2 = session.post(url2,headers=headers,data=data)#,
        if ("username_held_by_others") in req2.text:
            bot.send_message(message2.chat.id, text="خاصيه تحمل هنه 14 يوم")
        elif ("username_is_taken") in req2.text:
            bot.send_message(message2.chat.id, text="انقل حبي موفق ماكو خاصيه")
        else:
            bot.send_message(message2.chat.id, text="Error Try Again")
    except Exception as e:
        print(e)
        pass
bot.polling(True)
