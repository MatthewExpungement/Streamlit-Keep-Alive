from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def click_wakeup_button(url):
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
        # Open the URL
        print(f"Opening {url}...")
        driver.get(url)
        
        print("Waiting for the page to load...")

        time.sleep(5)
        #First search to see if the app is already running
        print("Checking if app is already running...")

        # First try to find in main document
        app_container = driver.find_element(By.CSS_SELECTOR, "div.stAppViewContainer")

        app_container = None
        
        # If not found, check inside iframes
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            driver.switch_to.frame(iframe)
            app_container = driver.find_element(By.CSS_SELECTOR, "div.stAppViewContainer")
            if app_container:
                break

        if app_container:
            print("App appears to be already running (found stAppViewContainer)")
        else:
            print("Could not confirm app is running.")
            # For some reason my CSS selector did not work to find the buttton
            # So instead I just find all buttons and check their text
            buttons = driver.find_elements(By.TAG_NAME, "button")
            if len(buttons) > 0:
                for button in buttons:
                    if button.text == "Yes, get this app back up!":
                        print("Found wakeup button! Clicking...")
                        button.click()
                        break
            else:
                print("No buttons found on the page.")
                print("Something is wrong we should have discovered the app is already up or found the button.")
                raise Exception("No buttons found on the page.")


        # Wait a moment to confirm action completed
        time.sleep(3)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    # Replace with the actual URL
    # Get URLs from environment variable, fallback to defaults if not set
    urls_env = os.environ.get("STREAMLIT_URLS")
    urls = [url.strip() for url in urls_env.split(",")]
    for target_url in urls:
        click_wakeup_button(target_url)
        print("------")