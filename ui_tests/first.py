from selenium import webdriver
import time


if __name__ == "__main__":
    driver_path = "/Users/pszkamruk/work/selenium_webdriver/chromedriver_mac64/chromedriver"

    # Create a new instance of the browser driver
    driver = webdriver.Chrome(executable_path=driver_path)

    # Maximize the browser window (optional)
    driver.maximize_window()

    # Navigate to a website
    url = "http://10.202.37.235:30001/"
    driver.get(url)

    # Wait for a few seconds to let the page load (optional)

    time.sleep(2)
    print("select inventory tab")
    inventory_tab = driver.find_element_by_css_selector("#main-component-container > div.sc-AxirZ.dGbZTB > div.sc-AxiKw.caSCzR > div > button:nth-child(3) > div.TabStyles__StyledLabel-sc-1ry8mzj-3.gRwQTe")
    inventory_tab.click()
    time.sleep(3)

    print("click edit button")
    edit_btn = driver.find_element_by_css_selector("#main-component-container > div:nth-child(3) > div > div:nth-child(2) > div.TableStyles__Styled-sc-1cmfss7-0.eTqeNy > div.TableStyles__StyledTableContainer-sc-1cmfss7-1.cUNRxz > table > tbody > tr.RowStyles__StyledStripeNone-f0igqq-0.RowStyles__StyledStripeOdd-f0igqq-1.cKFZLJ > td:nth-child(10) > button:nth-child(1)")
    edit_btn.click()
    time.sleep(4)

    print("click cancel button")
    cancel_btn = driver.find_element_by_css_selector("body > div:nth-child(3) > div > div > div.ModalStyles__Styled-sc-5fn8ds-0.eDKPNC > div.BoxStyles__Styled-sc-1h4b5f6-0.iNniqa.FooterStyles__StyledBox-yszcmv-0.kdfrCO > button.ClickableStyles__StyledA-sc-7al1vw-0.osAQV.ButtonSimpleStyles__StyledClickable-vlarwe-0.hvtLgL.ButtonStyles__StyledButtonSimple-eqxqs2-1.imMhPF > span > span")
    cancel_btn.click()
    time.sleep(5)

    print("click apply changes button")
    # Find an element by its ID and perform an action (e.g., filling in a search field)
    apply_button = driver.find_element_by_css_selector("#main-component-container > div.sc-AxhUy.biNwaT > div.sc-AxheI.hSSwJb > div > button.ClickableStyles__StyledA-sc-7al1vw-0.osAQV.ButtonSimpleStyles__StyledClickable-vlarwe-0.jOPXmR.ButtonStyles__StyledButtonSimple-eqxqs2-1.imMhPF > span > span")
    apply_button.click()
    time.sleep(12)

    print("close")
    # Close the browser
    driver.quit()



