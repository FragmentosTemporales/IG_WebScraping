import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .browser import Browser
from config import settings as s


class Instagram(Browser):
    def __init__(self, navegador=s.navegador, dir_descargas=s.dir_descargas, headless=False):
        super().__init__(navegador, dir_descargas, headless)

    def login_IG(self, usuario=s.user_ig, contraseña=s.pw_ig):
        self.paso = "Login Instagram"
        print(self.paso)

        self.driver.get('https://www.instagram.com/')

        time.sleep(2)

        self.paso = 'Logeando Usuario'
        print(self.paso)

        user = self.wait10.until(EC.presence_of_element_located((By.XPATH, '//input[@name="username"]')))
        user.send_keys(usuario)

        time.sleep(2)

        self.paso = "Ingresando contraseña"

        password = self.wait10.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))
        password.send_keys(contraseña)

        self.paso = "Presionando submit"

        btn_submit = self.wait10.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        btn_submit.click()

        time.sleep(5)

    def div_not_now(self):
        btn_not_now = self.wait10.until(EC.element_to_be_clickable((By.XPATH, '//div[@tabindex="0"]')))
        btn_not_now.click()
        time.sleep(5)

    def btn_not_now(self):
        btn_not_now = self.wait10.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_a9-- _ap36 _a9_1"]')))
        btn_not_now.click()
        time.sleep(5)

    def exect(self):

        try:
            self.login_IG()
            self.div_not_now()
            self.btn_not_now()
            time.sleep(5)

        except Exception as e:
            logging.error(e)
