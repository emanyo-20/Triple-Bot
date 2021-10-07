

import base64
import time
import io
from typing import Dict, Any, BinaryIO
import requests
import json
"""

num = nin
#num = 20020218161010000129
#num = 19980805457010000225
url = 'https://ors.brela.go.tz/um/load/load_nida/'
                                         
headers: Dict[str, str] = {'Content-Type': 'application/json', 'Content-Length': '0'}


data = requests.post(url + str(num), headers=headers)
parse: Dict[str, Dict[str, Dict[str, Any]]] = data.json()
results = parse['obj']['result']


#pure = json.loads(results)


no: str = results['NIN'] 
name1: str =  results['FIRSTNAME']
name2: str = results['MIDDLENAME']
name3: str = results['SURNAME']
sex: str = results['SEX']
date: str = results['DATEOFBIRTH']
r_region: str = results['RESIDENTREGION']
r_district: str = results['RESIDENTDISTRICT']
r_ward: str = results['RESIDENTWARD']
r_village: str = results['RESIDENTVILLAGE']
r_street: str = results['RESIDENTSTREET']
r_postcode: str = results['RESIDENTPOSTCODE']
p_region: str = results['PERMANENTREGION']
pDistrict: str = results['PERMANENTDISTRICT']
pWard: str = results['PERMANENTWARD']
pVillage: str = results['PERMANENTVILLAGE']
pStreet: str = results['PERMANENTSTREET']
bCountry: str = results['BIRTHCOUNTRY']
bRegion: str = results['BIRTHREGION']
bDistrict: str = results['BIRTHDISTRICT']
bWard: str = results['BIRTHWARD']
nation: str = results['NATIONALITY']
mStatus: str = results['MARITALSTATUS']
work: str = results['OCCUPATION']
pSchool: str = results['PRIMARYSCHOOLEDUCATION'] 
pSDistrict: str = results['PRIMARYSCHOOLDISTRICT']
pYear: str = results['PRIMARYSCHOOLYEAR']
phone: str = results['PHONENUMBER']





ID NUMBER: {str(no)}\n
FIRST NAME: {str(name1)}\n
MIDDLE NAME: {str(name2)}\n
LAST NAME: {str(name3)}\n
SEX: {str(sex)}\n
BIRTH DATE: {str(date)}\n
OCCUPATION: {str(work)}\n
NATIONALITY: {str(nation)}\n
MARITAL STATUS: {str(mStatus)}\n
RESIDENT REGION: {str(r_region)}\n
RESIDENT DISTRICT: {str(r_district)}\n
RESIDENT WARD: {str(r_ward)}\n
RESIDENT VILLAGE: {str(r_village)}\n
RESIDENT STREET: {str(r_street)}\n
RESIDENT POSTCODE: {str(r_postcode)}\n
PERMANENT REGION: {str(p_region)}\n
PERMANENT DISTRICT: {str(pDistrict)}\n
PERMANENT WARD: {str(pWard)}\n
PERMANENT VILLAGE: {str(pVillage)}\n
PERMANENT STREET: {str(pStreet)}\n
BIRTH COUNTRY: {str(bCountry)}\n
BIRTH REGION:  {str(bRegion)}\n
BIRTH DISTRICT: {str(bDistrict)}\n
BIRTH WARD: {str(bWard)}\n
PRIMARY SCHOOL: {str(pSchool)}\n
PRIMARY SCHOOL DISTRICT: {str(pSDistrict)}\n
PRIMARY SCHOOL YEAR: {str(pYear)}\n
PHONENUMBER: {str(phone)}\n


file = open("nida.txt", "w+")
file.write(x)
file.close()
print (type(x))


"""




import telebot
from telebot import types

API_KEY = '1398820843:AAFfB-4EySHzmSuI9CZGKtwPIxWaTlPEwzw'



bot = telebot.TeleBot(API_KEY)

'''
@bot.message_handler(commands=['start'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Please describe your problem.')
  bot.register_next_step_handler(sent, hello)

def hello(message):
#    open('problem.txt', 'w').write(message.chat.id + ' | ' + message.text + '||')
    bot.send_message(message.chat.id, 'Thank you!')
    bot.send_message(message.chat.id + ' | ' + results)
                               
                                                              
bot.polling()
 '''




import telebot
from telebot import types


user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None




start = '''
    Hello Welcome To My Bot, With this Bot You can Get users Info With Their Nationa Identity Number
use /nida Or /nin to fetch info
    '''

@bot.message_handler(commands=['start', 'help',])
def hi_sender(message):
    bot.send_message(message.chat.id, start)

# Apa ni NIN handler'
@bot.message_handler(commands=['nin', 'nida'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am NIN Bot 
press any key to continue:
""")
    bot.register_next_step_handler(msg, process_nin_step)

def process_nin_step(message):
    try:
#        chat_id = message.chat.id
#        markup = types.ReplyKeyboardMarkup()
 #       markup.add('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        msg = bot.reply_to(message, 'Enter Your NIN: \nExample: /183683XXXXXX')                                                        
        bot.register_next_step_handler(msg, process_res_step)
    except Exception as e:
        bot.reply_to(message,'sorrry Something went Wrong Please Check Your NIN Number And Try Again🙏')


def process_res_step(message):
    try:
        chat_id = message.chat.id
#        user = user_dict[chat_id] 
        global nin 
        nin = message.text
        num = nin
#num = 20020218161010000129
       #num = 19980805457010000225
        url = 'https://ors.brela.go.tz/um/load/load_nida/'
        headers: Dict[str, str] = {'Content-Type': 'application/json', 'Content-Length': '0'}
        data = requests.post(url + str(num), headers=headers)
        parse: Dict[str, Dict[str, Dict[str, Any]]] = data.json()
        results = parse['obj']['result']
#pure = json.loads(results)
        no: str = results['NIN']
        name1: str =  results['FIRSTNAME']
        name2: str = results['MIDDLENAME']
        name3: str = results['SURNAME']
        sex: str = results['SEX']
        date: str = results['DATEOFBIRTH']
        r_region: str = results['RESIDENTREGION']
        r_district: str = results['RESIDENTDISTRICT']
        r_ward: str = results['RESIDENTWARD']
        r_village: str = results['RESIDENTVILLAGE']
        r_street: str = results['RESIDENTSTREET']
        r_postcode: str = results['RESIDENTPOSTCODE']
        p_region: str = results['PERMANENTREGION']
        pDistrict: str = results['PERMANENTDISTRICT']
        pWard: str = results['PERMANENTWARD']
        pVillage: str = results['PERMANENTVILLAGE']
        pStreet: str = results['PERMANENTSTREET']
        bCountry: str = results['BIRTHCOUNTRY']
        bRegion: str = results['BIRTHREGION']
        bDistrict: str = results['BIRTHDISTRICT']
        bWard: str = results['BIRTHWARD']
        nation: str = results['NATIONALITY']
        mStatus: str = results['MARITALSTATUS']
        work: str = results['OCCUPATION']
        pSchool: str = results['PRIMARYSCHOOLEDUCATION']
        pSDistrict: str = results['PRIMARYSCHOOLDISTRICT']
        pYear: str = results['PRIMARYSCHOOLYEAR']
        phone: str = results['PHONENUMBER']
        profi: int = results['PHOTO']
        sign: int = results['SIGNATURE']


        x = f"""


▒█▄░▒█ ▀█▀ ▒█▄░▒█ 
▒█▒█▒█ ▒█░ ▒█▒█▒█ 
▒█░░▀█ ▄█▄ ▒█░░▀█

THIS IS YOUR NATIONAL ID INFO.👇👇

ID NUMBER: {str(no)}\n
FIRST NAME: {str(name1)}\n
MIDDLE NAME: {str(name2)}\n
LAST NAME: {str(name3)}\n
SEX: {str(sex)}\n
BIRTH DATE: {str(date)}\n
OCCUPATION: {str(work)}\n
NATIONALITY: {str(nation)}\n
MARITAL STATUS: {str(mStatus)}\n
RESIDENT REGION: {str(r_region)}\n
RESIDENT DISTRICT: {str(r_district)}\n
RESIDENT WARD: {str(r_ward)}\n
RESIDENT VILLAGE: {str(r_village)}\n
RESIDENT STREET: {str(r_street)}\n
RESIDENT POSTCODE: {str(r_postcode)}\n
PERMANENT REGION: {str(p_region)}\n
PERMANENT DISTRICT: {str(pDistrict)}\n
PERMANENT WARD: {str(pWard)}\n
PERMANENT VILLAGE: {str(pVillage)}\n
PERMANENT STREET: {str(pStreet)}\n
BIRTH COUNTRY: {str(bCountry)}\n
BIRTH REGION:  {str(bRegion)}\n
BIRTH DISTRICT: {str(bDistrict)}\n
BIRTH WARD: {str(bWard)}\n
PRIMARY SCHOOL: {str(pSchool)}\n
PRIMARY SCHOOL DISTRICT: {str(pSDistrict)}\n
PRIMARY SCHOOL YEAR: {str(pYear)}\n
PHONENUMBER: {str(phone)}\n

Pic and other info will be updated soon!

   🅽🅸🅳🅰  🅱🅾🆃
"""

        file = open("nida.txt", "w+")
        file.write(x)
        file.close()
        nidaa = open("nida.txt", "rb").read()
        bot.send_message(chat_id, nidaa)
        bot.send_message(chat_id, '\n To See Your NIN Photo And Signature Use Command /photo Or /picha')
    except Exception as e:
        bot.reply_to(message,'Hmmh! Something Went Wrong Check Your NIN Number And Try Again🙏')


#NEXT CODE TO FETCH PICTURE



user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None





# Apa ni NIN handler ya picha '
@bot.message_handler(commands=['picha', 'photo'])
def send2_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am NIN Bot
press any key to continue see Your NIN Photo and Sign:
""")
    bot.register_next_step_handler(msg, process_nin2_step)

def process_nin2_step(message):
    try:
#        chat_id = message.chat.id
#        markup = types.ReplyKeyboardMarkup()
 #       markup.add('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        msg = bot.reply_to(message, 'Please Re-Send Your NIN: \nExample: /183683XXXXXX')
        bot.register_next_step_handler(msg, process_res2_step)
    except Exception as e:
        bot.reply_to(message,'sorrry Something went Wrong Please Check Your NIN Number And Try Again🙏')


def process_res2_step(message):
    try:
        chat_id = message.chat.id
#        user = user_dict[chat_id]
        global nin
        nin = message.text
        num = nin
#num = 20020218161010000129
       #num = 19980805457010000225
        url = 'https://ors.brela.go.tz/um/load/load_nida/'
        headers: Dict[str, str] = {'Content-Type': 'application/json', 'Content-Length': '0'}
        data = requests.post(url + str(num), headers=headers)
        parse: Dict[str, Dict[str, Dict[str, Any]]] = data.json()
        results = parse['obj']['result']
#pure = json.loads(results)
        no: str = results['NIN']
        name1: str =  results['FIRSTNAME']
        name2: str = results['MIDDLENAME']
        name3: str = results['SURNAME']
        sex: str = results['SEX']
        date: str = results['DATEOFBIRTH']
        r_region: str = results['RESIDENTREGION']
        r_district: str = results['RESIDENTDISTRICT']
        r_ward: str = results['RESIDENTWARD']
        r_village: str = results['RESIDENTVILLAGE']
        r_street: str = results['RESIDENTSTREET']
        r_postcode: str = results['RESIDENTPOSTCODE']
        p_region: str = results['PERMANENTREGION']
        pDistrict: str = results['PERMANENTDISTRICT']
        pWard: str = results['PERMANENTWARD']
        pVillage: str = results['PERMANENTVILLAGE']
        pStreet: str = results['PERMANENTSTREET']
        bCountry: str = results['BIRTHCOUNTRY']
        bRegion: str = results['BIRTHREGION']
        bDistrict: str = results['BIRTHDISTRICT']
        bWard: str = results['BIRTHWARD']
        nation: str = results['NATIONALITY']
        mStatus: str = results['MARITALSTATUS']
        work: str = results['OCCUPATION']
        pSchool: str = results['PRIMARYSCHOOLEDUCATION']
        pSDistrict: str = results['PRIMARYSCHOOLDISTRICT']
        pYear: str = results['PRIMARYSCHOOLYEAR']
        phone: str = results['PHONENUMBER']
        profi: int = results['PHOTO']
        sign: int = results['SIGNATURE']
        file = profi
        file2 = sign
        byte = file
        decode1 = open('profile.png', 'wb')
        decode1.write(base64.b64decode((byte)))
        decode1.close()
        byte2 = file2
        decode1 = open('sign.png', 'wb')
        decode1.write(base64.b64decode((byte2)))
        decode1.close()
        chat_id = message.chat.id
        photo = open('./profile.png', 'rb')
        bot.send_photo(chat_id, photo, caption="Photo Of Your NIN ID Card")
        sign = open('./sign.png', 'rb')
        bot.send_photo(chat_id, sign, caption="Sign Of Your NIN ID Card")
    except Exception as e:
        bot.reply_to(message,'Hmmh! Something Went wrong Please Check Your NIN And Try  Again Latter')
    
#             bot.reply_to(message,'Hmmh! Something Went Wrong Try Again🙏')



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

while True:
   try:
     bot.polling()
   except Exception:
     time.sleep (10)
bot.polling(none_stop=False, interval=0, timeout=20)


