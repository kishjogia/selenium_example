from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.set_headless()
assert opts.headless

browser = Chrome(options=opts)
browser.get("https://google.co.uk")

search_form = browser.find_element_by_class_name("gLFyf.gsfi")
search_form.send_keys("python")
search_form.submit()

results = browser.find_elements_by_class_name("result")
print(results[0].text)

browser.close()
quit()
