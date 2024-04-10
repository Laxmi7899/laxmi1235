from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flightradar24.com/data/airports/pnq")

arrival_section = driver.find_element(By.XPATH, "//a[@class = 'btn ']")

airport_data_ids = {
            "Bengaluru" : "arriva_landing- BLR",
            "Delhi" : "arriva_landing- DEL",
            "Goa" : "arriva_landing- GOI",
            "Chandigarh" : "arriva_landing- IXC",
            "Hyderabad" : "arriva_landing- HYD",
            "Nagpur" : "arriva_landing- NAG",
            "Dubai" : "arriva_landing- DXB",
}

for airport, data_id in airport_data_ids.items():
    try:
        flight_status  = arrival_section.find_element(By.Xpath, "//*[@id='cnt-data-content']//*[@class= 'hide-mobile-only ng-binding']")
        print(f"{airport}:{flight_status}")
    except:
        print(f"{airport}: data not available")

driver.quit()