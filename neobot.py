from functions.bot import adclick, login, done, adprize


class NeoBot:
    def __init__(self):
        import os
        from threading import Thread

        def test():
            os.system(
                '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" -remote-debugging-port=9014')
        Thread(target=test).start()

    def login(self):
        login.login_functions(self)

    def adclick(self):
        adclick.adclick_functions(self)

    def adprize(self):
        adprize.adprize_functions(self)

    def done(self):
        done.done_functions(self)
