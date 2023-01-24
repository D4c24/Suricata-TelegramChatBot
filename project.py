import os, re, telegram

##HTTP API from telegrambot - BotFather
chat_id = '902953144'
api_key = '5917426187:AAEI7WL8HNeJGs0Az37mYOTRK9DaWHMPXxc'

##Function to send messages to telegram
def bot(msg):
  bot = telegram.Bot(token=api_key)
  bot.send_message(chat_id=chat_id, text=str(msg))

## Main Function, reads file and uses regex to match only Suricata alerts with priority higher than 3
def run():
  file = open('data-sample.log', 'r')
  lines = file.readlines()

  count = 0

  for line in lines:
    count += 1
    regex = str(re.search("Priority: [3-9]", line))
    if (regex == "None"):
      pass
    else:
      #msg = 'Suricata-Alert: ' + str(count) + ' - ' + line
      msg = 'test pepito'
      bot(msg)
      #print('line: ' + str(count) + ' - ' + line)

if __name__ == '__main__':
  run()
