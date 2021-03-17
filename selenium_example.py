from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
#opts.set_headless()
#assert opts.headless

browser = Chrome(options=opts)
browser.get("https://accounts.spotify.com/en/login/")

# username
browser.find_element_by_id("login-username").send_keys("")
# password
browser.find_element_by_id("login-password").send_keys("")
# click 'log in' button
browser.find_element_by_id("login-buton").click()


browser.close()
quit()
