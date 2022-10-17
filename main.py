from time import sleep
from modules.neobot import NeoBot

bot = NeoBot()
sleep(1)
bot.login()
bot.adclick()
sleep(10)
bot.adprize()
sleep(10)
bot.done()
