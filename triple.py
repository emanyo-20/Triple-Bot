#!/bin/python 
#######################################
#                                     #
#          The3HaT NIDA BOT           #
#                                     #
#######################################

token = 'wzwEPlTaWxIPwtKGZC9IuSmzHSyE4-BfFAA:3480288931'
 

import logging, telegram
import requests, subprocess as shell
from uuid import uuid4
import json, base64, io, re
from base64 import b64decode as triple
from PIL import Image
from telegram.ext import*
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from typing import Dict, Any, BinaryIO

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
token = token[::-1]
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=token)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    text = '''
    Hello Welcome To My Bot, With this Bot You can Get users Info With Their Nationa Identity Number
use /nida 183683XXXXXX to fetch info
    '''
    update.message.reply_text(text)

'''
def get_nida(update: Update, context: CallbackContext) -> None:
      url = "https://kabanga.ga/spy/spy/?phoneNumber="
      try:
       error = context.args[0]
      except:
       update.message.reply_text('Enter number to scan eg: /get 0755234576')
      nida = str(error)
      valid = nida.isdigit()
      if valid:
        if len(nida) != 10:
          update.message.reply_text('Enter Valid Phone Number')
        else:
          r = requests.get(url+nida)
          if 4 in [r.status_code]:
            update.message.reply_text('Sorry We Cant Gather Any Data At the Moment')
          else:
             for nin in r.content.split():
                if nin.isdigit() == True:
                  if len(nin) == 20:
                     nidA = nin
                     update.message.reply_text(f'Your NIN: {nidA}')
      else:
        update.message.reply_text('Phone number cant cantain letters, must be like this 0755442936')
'''

def info_cmd(update: Update, context: CallbackContext) -> None:
 try:
   if not context.args[0]:
    update.message.reply_text('Provide NIN you want to scan')
    update.message.reply_text('example /info 19992356xxxxxx')
   else:
    number = str(context.args[0]) # take NIN
    number = number.replace('-', '') # replace - with ''
    number = number.strip() # strip/remove any space

    if not number:
      update.message.reply_text('Provide NIN you want to scan')
      update.message.reply_text('example /info 19992356xxxxxx')
    else:
      if number.isdigit() == False:
        update.message.reply_text('NIN must be a number')
      elif len(number) < 20:
        update.message.reply_text('NIN is wrong (incomplete)')
      else:
        headers = {'Content-Type': 'application/json', 'Content-Length': '0'}
        url = "https://ors.brela.go.tz/um/load/load_nida/"
        try:
          response: Any = requests.post(url+str(number), headers=headers)
          if response.status_code == 404:
            update.message.reply_text('NIDA is current offline we cant get any information for you')
          elif response.status_code in [200, 201, 202, 203, 204]:
            response: Dict[str, Dict[str, Dict[str, Any]]] = response.json()
#            reposnse = response.json()
            print(response)
            #update.message.reply_text(str(response.content)) ####
            results = response['obj']['result']
            #saving passport
            pass_decode = base64.b64decode(results['PHOTO'])
            pass_img = Image.open(io.BytesIO(pass_decode))
            pass_img.save(results['FIRSTNAME']+"-"+results['SURNAME']+".jpg")
            #saving signature
            sign_decode = base64.b64decode(results['SIGNATURE'])
            sign_img = Image.open(io.BytesIO(sign_decode))
            sign_img.save("sign-"+results['FIRSTNAME']+"-"+results['SURNAME']+".jpg")
            # DONE with Images
            passport = results['FIRSTNAME']+'-'+results['SURNAME']+'.jpg'
            signature = 'sign-'+results['FIRSTNAME']+'-'+results['SURNAME']+'.jpg'
            # Full Information
            nida_info = f"""
NIN : {results['NIN']}
FIRST-NAME : {results['FIRSTNAME']}
MIDDLE-NAME : {results['MIDDLENAME']}
SUR-NAME : {results['SURNAME']}
SEX : {results['SEX']}
BIRTHDAY : {results['DATEOFBIRTH']}
RESIDENT-REGION : {results['RESIDENTREGION']}
RESIDENT-DISTRICT : {results['RESIDENTDISTRICT']}
RESIDENT-WARD : {results['RESIDENTWARD']}
RESIDENT-VILLAGE : {results['RESIDENTVILLAGE']}
RESIDENT-STREET : {results['RESIDENTSTREET']}
RESIDENT-POSTCODE : {results['RESIDENTPOSTCODE']}
PERMANENT-REGION : {results['PERMANENTREGION']}
PERMANENT-DISTRICT : {results['PERMANENTDISTRICT']}
PERMANENT-WARD : {results['PERMANENTWARD']}
PERMANENT-VILLAGE : {results['PERMANENTVILLAGE']}
PERMANENT-STREET : {results['PERMANENTSTREET']}
BIRTH-COUNTRY : {results['BIRTHCOUNTRY']}
BIRTH-REGION : {results['BIRTHREGION']}
BIRTH-DISTRICT : {results['BIRTHDISTRICT']}
BIRTH-WARD : {results['BIRTHWARD']}
MARITAL-STATUS : {results['MARITALSTATUS']}
NATION : {results['NATIONALITY']}
WORK : {results['OCCUPATION']}
PRIMARY-SCHOOL : {results['PRIMARYSCHOOLEDUCATION']}
PRIMARY-SCHOOL-YEAR : {results['PRIMARYSCHOOLYEAR']}
PRIMARY-SCHOOL-DISTRICT : {results['PRIMARYSCHOOLDISTRICT']}
            """
            update.message.reply_text(nida_info)
            '''send media'''
            bot.send_photo(chat_id=update.message.chat_id, photo=open(passport, 'rb'))
            bot.send_photo(chat_id=update.message.chat_id, photo=open(signature, 'rb'))
            '''clear media'''
            shell.call(f'rm -rf {passport} {signature}', shell=True)
          else:
            update.message.reply_text('ERROR OCCURED')
        except Exception as Error:
            update.message.reply_text(Error)
 except:
  update.message.reply_text('Provide NIN you want to scan')
  update.message.reply_text('example /nida 19992356XXXXXX')

def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    query = update.inline_query.query

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"*{escape_markdown(query)}*", parse_mode=ParseMode.MARKDOWN
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"_{escape_markdown(query)}_", parse_mode=ParseMode.MARKDOWN
            ),
        ),
    ]

    update.inline_query.answer(results)


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("nida", info_cmd))
    # dispatcher.add_handler(CommandHandler("get", get_nida))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



#f __name__ == '__main__':
main()
