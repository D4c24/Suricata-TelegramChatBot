import re, logging, time
from collections import deque
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

application = ApplicationBuilder().token('TOKEN').build()

## Main Function, reads file and uses regex to match only Suricata alerts with priority higher than 3
def alert(n=1):
  ## Return the last n lines of a file
  with open('data-sample.log') as f:
      ## Create a deque object to store last line in fast.log file.
      d = deque(f, n)
      ## Regex to check for alert with priority higher than 3
      regex = str(re.search("Priority: [2-9]", d[0]))
      if (regex == "None"):
        return False
      else:
        return d[0]

## Function to send messages to Telegram.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  msg1 = 'texto'
  while True:
    msg = alert()
    if (msg == False):
      time.sleep(5)
    else:
      if (msg1 == msg):
        time.sleep(5)
      else:
        msg1 = msg
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(msg))
        time.sleep(5)
    

if __name__ == '__main__':
  start_handler = CommandHandler('start', start)
  application.add_handler(start_handler)
  application.run_polling()
    