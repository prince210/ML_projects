# =============================================================================
# import requests
# import urllib.request
# import time
# from bs4 import BeautifulSoup
# 
# url = 'https://www.gartner.com/reviews/market/meeting-solutions-web-conferencing/vendor/att/product/att-connect'
# 
# #with open('https://www.gartner.com/reviews/review/view/634478') as html_file:
# #    soup = BeautifulSoup(html_file, 'lxml')
# from requests import get
# 
# response = get(url)
# 
# print(response.text)
# # page = urllib.request.urlopen(url)
# 
# soup = BeautifulSoup(response,"html.parser")
# 
# elements = soup.find('span',class_='commentSuffix')
# 
# print(soup.prettify())
# 
# for divs in soup.findAll('div', attrs = {'class': 'col-xs-12'}):
#     text_file = divs.find('span',class_='commentSuffix').text
#     print(text_file)
# 
#     
# =============================================================================


from selenium import webdriver
chrome_path = r"C:\Program Files\Python36\Scripts\chrome_driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

import csv

with open ('sentiment.csv', 'w') as f:
    f.write("review\n")

driver.get('https://www.gartner.com/reviews/market/meeting-solutions-web-conferencing/vendor/att/product/att-connect')
review = driver.find_elements_by_class_name("snippetSummary")
with open ('sentiment.csv', 'a') as f:
    for everyPost in review:
        f.write(everyPost.text+"\n")
        #print(" ")
    
driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[2]/a').click()
review = driver.find_elements_by_class_name("snippetSummary")
with open ('sentiment.csv', 'a') as f:
    for everyPost in review:
        f.write(everyPost.text+"\n")
        #print(" ")
    
driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[4]/a').click()
review = driver.find_elements_by_class_name("snippetSummary")
with open ('sentiment.csv', 'a') as f:
    for everyPost in review:
        f.write(everyPost.text+"\n")
        #print(" ")
    
driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[5]/a').click()
review = driver.find_elements_by_class_name("snippetSummary")
with open ('sentiment.csv', 'a') as f:   
    for everyPost in review:
        f.write(everyPost.text+"\n")
        
driver.close()
      # print(" ")
# =============================================================================
# for i in range(1,5):
#     driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[]/a').click()
#     review = driver.find_elements_by_class_name("snippetSummary")
#     for everyPost in review:
#        print(everyPost.text)
#        print(" ")
# =============================================================================

    
# =============================================================================
# another try
 # =============================================================================
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# =============================================================================
#review_SeeMore = driver.find_elements_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[4]/div/div/section/div/section[2]/section[2]/div[1]/span/a')
# for review in review_SeeMore:
#         for paragraph in review.find_elements(By.TAG_NAME, "p"):
#             print(paragraph.get_attribute('textContent').encode("utf-8"))
#         print('\n============================\n')
#         
# # another try
# driver.find_elements_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[4]/div/div/section/div/section[2]/section[2]/div[1]/span/a').click()
# review = driver.find_element_by_class_name("commentSuffix")
# print(review)
# 
# 
# #last one try
# view_more_elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.uxd-link.uxd-link-primary[]")))
# for more_element in view_more_elements:
#     more_element.click()
# all_reviews = driver.find_elements_by_xpath("//div[@class='right-rail']//p[(text())]")
# for review in all_reviews:
#     print(review.text)
# =============================================================================
driver.quit()