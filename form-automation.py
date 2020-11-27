from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# Load the driver
chrome_driver = "chromedriver"

# Got to Website
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.google.com")

# Insert text into form
search = driver.find_element_by_css_selector("[name=q]")
search.send_keys('Mathew Steininger Website')

# Submit
search.submit()

# Click first result
first_result = driver.find_element_by_css_selector("[class=g]").find_element_by_tag_name("a")
first_result.click()

# capture the screen
driver.get_screenshot_as_file("capture.png")
