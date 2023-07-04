# !pip install selenium
# !pip install webdriver_manager
from selenium import webdriver
import pandas as pd
  
# for holding the resultant list
paper_abs = []
paper_method=[]
paper_eval = []
paper_conclusion = []
paper_discussion = []
cnt = 0
at = ""
mt = ""
et = ""
ct = ""
dt = ""
  
# for page in range(1, 3, 1):
# lis = ['Chennai','Mumbai','Delhi']
# for i in lis:
page_url = "https://packages.yatra.com/holidays/intl/search.htm?destination=mumbai"
# page_url = "https://packages.yatra.com/holidays/intl/search.htm?destination="+str(i)
# page_url = "https://packages.yatra.com/holidays/intl/search.htm?destination="+str(i)
# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# page_url = "https://link.springer.com/article/10.1007/s11023-021-09573-8"    #Add URL here
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=chrome_path)

# driver = webdriver.Firefox()
 
# enter keyword to search
# keyword = "geeksforgeeks"
driver.get(page_url)
# title = driver.find_element_by_class_name("c-article-title")
abstract = driver.find_element("class","package-name")
at = abstract.text
method1 = driver.find_element("class","amount")
mt = method1.text
# evaluation = driver.find_element("id","Sec8-content")
# et = evaluation.text
# discussion = driver.find_element("id","Sec35-content")
# dt = discussion.text
# conclusion = driver.find_element("id","Sec43-content")
# ct = conclusion.text

# paper_title.append(title.text)
# x = abstract.text if not x else x
paper_abs.insert(cnt,at)
# paper_discussion.insert(cnt,dt)
# paper_conclusion.insert(cnt,ct)
paper_method.insert(cnt,mt)
# paper_eval.insert(cnt,et)
# print(paper_discussion)
  
#closing the driver
driver.close()

dataDf = pd.DataFrame()
dataDf["Paper Abstract"] = paper_abs
# dataDf["Paper Conclusion"] = paper_conclusion
# dataDf["Paper Discussion"] = paper_discussion
# dataDf["Paper Evaluation"] = paper_eval
dataDf["Paper Methodology"] = paper_method
print(dataDf)

#this will return a CSV file which we will use to make PPTs
# dataDf.to_csv(r'xyz_dataset.csv', index=False) 