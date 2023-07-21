from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_headless_selenium_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    url = "http://10.202.37.235:30001/"
    driver.get(url)

    time.sleep(2)
    print("select inventory tab")
    inventory_tab = driver.find_element_by_css_selector("#main-component-container > div.sc-AxirZ.dGbZTB > div.sc-AxiKw.caSCzR > div > button:nth-child(3) > div.TabStyles__StyledLabel-sc-1ry8mzj-3.gRwQTe")
    inventory_tab.click()
    time.sleep(3)
    driver.quit()

    print("click apply changes button")
    # Find an element by its ID and perform an action (e.g., filling in a search field)
    apply_button = driver.find_element_by_css_selector("#main-component-container > div.sc-AxhUy.biNwaT > div.sc-AxheI.hSSwJb > div > button.ClickableStyles__StyledA-sc-7al1vw-0.osAQV.ButtonSimpleStyles__StyledClickable-vlarwe-0.jOPXmR.ButtonStyles__StyledButtonSimple-eqxqs2-1.imMhPF > span > span")
    apply_button.click()
    time.sleep(12)

if __name__ == "__main__":
    run_headless_selenium_test()