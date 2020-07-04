import random
import string
import os

import names

from selenium.webdriver.support.select import Select


class ApplicantsPage:

    def __init__(self, driver):

        # For regular text input:
        self.nombre_element = driver.find_element_by_xpath('')

        # For Select inputs:
        self.educacion_estado = driver.find_element_by_xpath('')
        self.educacion_estado = Select(self.educacion_estado)

        # For the submit button
        self.submit = driver.find_element_by_xpath('')
        

    def apply(self):
        # For regular text input:
        nombre = names.get_first_name()
        self.nombre_element.send_keys(nombre)

        # For Select inputs:
        sex_list = ['Femenino', 'Masculino']
        sex = sex_list[random.randint(0,1)]
        self.sex_element.select_by_visible_text(sex)

        self.submit.click()

    def random_email(self):
        email_list = ['@yahoo.com', '@gmail.com', '@aol.com', '@hotmail.com', '@companyname.com', '@companyname.com.mx', '@icloud.com', '@me.com', '@outlook.com']
        return self.random_char(random.randint(1, 11)) + email_list[random.randint(0, len(email_list) - 1)]

    def random_char(self, y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))


    def random_birth_date(self):
        day = str(random.randint(1, 30))
        month = str(random.randint(1, 12))
        year = str(random.randint(1970, 2000))
        return day + '/' + month + '/' + year

