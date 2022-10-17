from functions.bot import adclick, login, done, adprize


class NeoBot:
    def __init__(self):
        try:
            from selenium import webdriver
            from webdriver_manager.chrome import ChromeDriverManager
        except ModuleNotFoundError:
            import sys
            import subprocess
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', ' pip'])
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'r.txt'])
            from selenium import webdriver
            from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        login.login_functions(self)

    def adclick(self):
        adclick.adclick_functions(self)

    def adprize(self):
        adprize.adprize_functions(self)

    def done(self):
        done.done_functions(self)
