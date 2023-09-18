from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

searchBox = driver.find_element_by_xpath('//*[@id="search"]')
# searchBox.click()
searchBox.send_keys('Yash Gupta')

signin = driver.find_element_by_xpath('//*[@id="text"]')
# signin = driver.find_element_by_xpath('//*[@id="button"]')
signin.click()

searchBtn = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchBtn.click()
