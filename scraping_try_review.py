#step 1 scrape reviews
from selenium import webdriver
chrome_path = r"C:\Program Files\Python36\Scripts\chrome_driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

import csv
import io
with open ('sentiment.csv', 'w') as f:
    f.write("index,review\n")
index = 1
driver.get('https://www.gartner.com/reviews/market/meeting-solutions-web-conferencing/vendor/att/product/att-connect')
review = driver.find_elements_by_class_name("snippetSummary")
with io.open ('sentiment.csv', 'a',encoding="utf-8") as f:
    for everyPost in review:
        print(index)
        f.write("index"+","+everyPost.text+"\n")
        index = index+1
        
        #print(" ")
    
driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[2]/a').click()
review = driver.find_elements_by_class_name("snippetSummary")
with io.open ('sentiment.csv', 'a') as f:
    for everyPost in review:
        f.write("index"+","+everyPost.text+"\n")
        index = index + 1
        #print(" ")
    
driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[4]/a').click()
review = driver.find_elements_by_class_name("snippetSummary")
with io.open ('sentiment.csv', 'a') as f:
    for everyPost in review:
        f.write("index"+","+everyPost.text+"\n")
        index =index+1
        #print(" ")
    
driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div/div[15]/ol/li[5]/a').click()
review = driver.find_elements_by_class_name("snippetSummary")
with io.open ('sentiment.csv', 'a') as f:   
    for everyPost in review:
        f.write("index"+","+everyPost.text+"\n")
        index = index+1
        
driver.close()


#step 2  importing libraries


import nltk
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import re

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
# reading file
dataset = pd.read_csv('sentiment (1).csv',sep = 'delimeter')

dataset.insert(0,'index',1)

dataset.insert(1,'label',1)

for i in range(37):
    dataset['index'][i] = i
    dataset['label'][i] = np.random.randint(0,2)

dataset['review'][4]

processed_review = []
# NLP
for i in range(37):
    temp = re.sub(r'[\(\)]','',dataset['review'][i])
    temp = re.sub('[^a-zA-Z-]',' ',temp)
    temp = temp.lower()
    temp = temp.split()
    temp = [ps.stem(token) for token in temp if not token in set(stopwords.words('english'))]
    
    temp = ' '.join(temp)
    processed_review.append(temp)
#step 3 predicting score  
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(processed_review)
X = X.toarray()
y = dataset['label'].values

from sklearn.naive_bayes import GaussianNB
n_b = GaussianNB()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)


n_b.fit(X_train,y_train)

n_b.score(X_train,y_train)
n_b.score(X_test,y_test)
n_b.score(X,y)