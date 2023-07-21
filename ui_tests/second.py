from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_headless_selenium_test():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    # url = "http://10.202.37.235:30001/"
    # driver.get(url)
    #
    # time.sleep(2)
    # print("select inventory tab")
    # inventory_tab = driver.find_element_by_css_selector("#main-component-container > div.sc-AxirZ.dGbZTB > div.sc-AxiKw.caSCzR > div > button:nth-child(3) > div.TabStyles__StyledLabel-sc-1ry8mzj-3.gRwQTe")
    # inventory_tab.click()
    # time.sleep(3)
    # driver.quit()

    url = "https://www.onet.pl/"
    driver.get(url)
    page_title = driver.title
    print("Page Title:", page_title)


if __name__ == "__main__":
    run_headless_selenium_test()