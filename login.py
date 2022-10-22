def login_functions(self):
    try:
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
    except ModuleNotFoundError:
        import sys
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', ' pip'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'r.txt'])
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
    self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    self.driver.get('https://www.neobux.com/c/?vl=93F392118E286631')
