import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def wait_for_download_complete(download_path, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if any(file.endswith(".crdownload") for file in os.listdir(download_path)):
            time.sleep(1)
        else:
            return True
    return False

def main():

    download_path = r"C:\Users\leeli\Downloads"

    # Object of ChromeOptions
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    chromedriver_path = r"C:\Program Files\Google\Chrome"

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.ups.com/us/en/support/shipping-support/shipping-costs-rates/daily-rates.page")

    for prefix in range(0, 1000):

        input_element = driver.find_element(By.ID, 'ups-zone_zip')
        input_element.clear()
        input_element.send_keys(f"{str(prefix).zfill(3)}")

        download_button = driver.find_element(By.CSS_SELECTOR, 'button.ups-cta[title="Download Chart"]')
        download_button.click()

        time.sleep(2)

        if wait_for_download_complete(download_path):
            print("Download completed successfully!")
        else:
            print("Timeout: Download took too long.")

        time.sleep(2)

    driver.quit()


if __name__ == "__main__":
    main()
