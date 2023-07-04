from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
# from selenium import webElement
  
# for holding the resultant list
package_price = []
package_duration = []
package_name=[]
package_inclusions = []
package_place = []
v = []


place = "udaipur"
page_url = "https://packages.yatra.com/holidays/intl/search.htm?destination="+place      #Add URL here

driver = webdriver.Chrome()
driver.get(page_url)


amount = driver.find_elements(By.CLASS_NAME,"final-price")
for i in range(len(amount)):
    package_price.append(amount[i].text or "")

for i in range(len(amount)):
    package_place.append(place)

pName = driver.find_elements(By.CLASS_NAME,"package-name")
for i in range(len(amount)):
    package_name.append(pName[i].text or "") 


pDuration = driver.find_elements(By.CLASS_NAME,"package-duration")
for i in range(len(amount)):
    package_duration.append(pDuration[i].text or "")    


pInclusion = driver.find_elements(By.CLASS_NAME,"package-name")
for i in range(len(amount)):
    package_inclusions.append(pInclusion[i].text or "")  



for k in range(len(package_name)):

    before = driver.window_handles[0]
    link = driver.find_element(By.PARTIAL_LINK_TEXT, package_name[k])
    link.click()
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)

    amount = driver.find_elements(By.ID,"detailedItinerary")
    for i in range(len(amount)):
        v.append(amount[i].text or "")

    window_after = driver.window_handles[-1]
    driver.switch_to.window(window_after)

    driver.get(page_url)

#closing the driver
driver.close()


dataDf = pd.DataFrame()
dataDf["Place"] = package_place
dataDf["Pack_Name"] = package_name
dataDf["Price"] = package_price
dataDf["Time"] = package_duration
dataDf["About_trip"] = v
dataDf["Package Inclusions"] = package_inclusions
print(dataDf)

# #this will return a CSV file
dataDf.to_csv(r'xyz_dataset.csv', index=False) 

