from time import sleep
from modules.neobot import NeoBot

bot = NeoBot()
sleep(1)
bot.login()
print(4)
bot.adclick()
print(3)
bot.adprize()
print(2)
bot.done()
