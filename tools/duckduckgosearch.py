"""DuckDuckGo search python tool"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def duckduckgo_search(query):
    """Gör en sökning på DuckDuckGo"""
    driver = webdriver.Chrome()
    driver.get("https://www.duckduckgo.com")

    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    search_box.send_keys(query + Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "r1-0"))
    )

    # Vänta på användarinput innan skriptet avslutas
    input("Press Enter to close the browser and end the script...")

    driver.quit()
