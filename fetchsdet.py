import os
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Automatically install the appropriate version of chromedriver
chromedriver_autoinstaller.install()

# Setup WebDriver
print(os.getcwd())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("http://sdetchallenge.fetch.com")

ele_count = 0


def weigh(left_bars, right_bars):

    global ele_count

    # Fill left bowl
    print("reset btn")
    bowls_reset = driver.find_element(By.XPATH, "//button[@id='reset' and text()='Reset' and not(@disabled)]")
    bowls_reset.click()

    left_bowl = driver.find_elements(By.CSS_SELECTOR, 'input[data-side="left"]')
    for i, bar in enumerate(left_bars):
        left_bowl[i].send_keys(str(bar))
        print("left:" + str(bar))

    # Fill right bowl
    print("right bowl")
    right_bowl = driver.find_elements(By.CSS_SELECTOR, 'input[data-side="right"]')
    for i, bar in enumerate(right_bars):
        right_bowl[i].send_keys(str(bar))
        print("right:" + str(bar))

    # Click "Weigh" button
    print("weigh")
    driver.find_element(By.ID, "weigh").click()

    weighings_li_ele = driver.find_element(By.CSS_SELECTOR, "div.game-info ol")
    weighings_ele = weighings_li_ele.find_elements(By.TAG_NAME, "li")
    old_count = len(weighings_ele)
    print(old_count)
    
    # Wait until the count of elements changes
    WebDriverWait(driver, 10).until(
        lambda driver: len(weighings_li_ele.find_elements(By.TAG_NAME, "li")) != old_count
    )

    # Get the result of weighing

    result = driver.find_element(By.CLASS_NAME, "result").text.split('\n')[1]
    print("result:" + result)
    return result


def find_fake_bar():
    weighings = []
    # Step 1: Divide into 3 groups of 3 bars
    group1 = [0, 1, 2]
    group2 = [3, 4, 5]
    group3 = [6, 7, 8]

    # Weigh group 1 vs group 2
    result = weigh(group1, group2)
    weighings.append((group1, group2, result))

    if result == "=":
        # Fake bar is in group 3
        suspect_group = group3
    elif result == "<":
        # Fake bar is in group 1
        suspect_group = group1
    else:
        # Fake bar is in group 2
        suspect_group = group2

    # Step 2: Weigh two bars from suspect group
    bar1, bar2, bar3 = suspect_group
    result = weigh([bar1], [bar2])
    weighings.append(([bar1], [bar2], result))

    if result == "=":
        fake_bar = bar3
    elif result == "<":
        fake_bar = bar1
    else:
        fake_bar = bar2

    return fake_bar, weighings


def main():
    fake_bar, weighings = find_fake_bar()
    
    # Click the fake bar button
    driver.find_element(By.ID, f"coin_{fake_bar}").click()

    # Get alert message
    alert = Alert(driver)
    alert_message = alert.text
    alert.accept()

    # Print results
    print(f"Alert message: {alert_message}")
    print(f"Number of weighings: {len(weighings)}")
    for i, weighing in enumerate(weighings):
        left, right, result = weighing
        print(f"Weighing {i+1}: {left} vs {right} => {result}")
        
    print(f"Answer: {fake_bar}")
    print("###Test Successfully Completed!!!###")

    confirm_quit = input("Do you want to quit the WebDriver? (y/n): ").lower()
    if confirm_quit == "y":
        driver.quit()
    else:
        print("WebDriver not quitting.")


if __name__ == "__main__":
    main()
