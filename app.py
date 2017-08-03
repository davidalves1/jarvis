from twx.botapi import TelegramBot
from finder import Finder
import env

"""
Send a message to user
"""
def notify(title, link):
    bot = TelegramBot(env.TELEGRAM_API_TOKEN)
    user_id = int(env.USER_ID)

    bot.send_message(
        user_id, 
        "Senhor, existe uma nova chamada no Conab: \n\n%s \n\n%s" % (title, link)
    ).wait()

def main():
    finder = Finder()

    data = finder.conab()

    if data is not None:
        notify(data['title'], data['link'])

if __name__ == '__main__':
    main()