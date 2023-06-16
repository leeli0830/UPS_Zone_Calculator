from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()

    driver.get("https://www.ups.com/us/en/support/shipping-support/shipping-costs-rates/daily-rates.page")

    input_element = driver.find_element('id', 'ups-zone_zip')
    input_element.send_keys('30311')

    download_button = driver.find_element(By.CSS_SELECTOR, 'button[title="Download Chart"]')
    download_button.click()
    # input_element.send_keys(Keys.RETURN)

    # driver.quit()


if __name__ == "__main__":
    main()