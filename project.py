import os, re, logging, time
from collections import deque
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token('5917426187:AAEI7WL8HNeJGs0Az37mYOTRK9DaWHMPXxc').build()

## Main Function, reads file and uses regex to match only Suricata alerts with priority higher than 3
def alert(n=1):
  ## Return the last n lines of a file
  with open('data-sample.log') as f:
      ## Regex to check for alert with priority higher than 3
      d = deque(f, n)
      regex = str(re.search("Priority: [2-9]", d[0]))
      if (regex == "None"):
        return False
      else:
        return d.pop()
  
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  while True:
    if (alert() == False):
      #time.wait
      pass
    else:
      msg = alert()
      time.sleep(5)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(msg))



if __name__ == '__main__':
  start_handler = CommandHandler('start', start)
  application.add_handler(start_handler)
  application.run_polling()
    