from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from config import settings as s


class Browser():

    def __init__(
        self, navegador=s.navegador, dir_descargas=s.dir_descargas, headless=False):
        self.navegador=navegador
        self.dir_descargas=dir_descargas
        self.paso='Inicialización driver'
        prefs = {'download.default_directory' : self.dir_descargas}
            
        if self.navegador=='Chrome':
            self.options = Options()
            if headless:
                print('running headless mode')
                self.options.add_argument('--headless')
            self.options.add_experimental_option('prefs', prefs)
            self.options.add_argument("--start-maximized")  
            self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options = self.options)

        self.wait10 = WebDriverWait(self.driver, 20)
        self.wait100 = WebDriverWait(self.driver, 180)