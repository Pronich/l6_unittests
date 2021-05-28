from selenium import webdriver
from settings import login, password

def login_to_ya(login, password):
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://passport.yandex.ru/auth');
    driver.find_element_by_xpath("//input[@id='passp-field-login']").send_keys(login)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//input[@id='passp-field-passwd']").send_keys(password)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.implicitly_wait(10)
    name = driver.find_element_by_class_name('personal-info__first')
    return name.text

