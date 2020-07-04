from tqdm import tqdm

from selenium import webdriver
from applicant import ApplicantsPage

TIMES_TO_RUN = 100000
URL = ''

def fuck_you():
    requests = 0
    failed = 0
    driver = webdriver.Firefox()
    driver.maximize_window()
    for i in tqdm(range(TIMES_TO_RUN)):
        try:
            driver.get(URL)
            app = ApplicantsPage(driver)
            app.apply()
            requests += 1
            print('Successful: ' + str(requests))
        except:
            failed += 1
            print('Unsuccesful: ' + str(failed))
    driver.quit()


if __name__ == "__main__":
    fuck_you()
