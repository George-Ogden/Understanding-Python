from selenium import webdriver
import time
import requests

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.google.com/imghp")

driver.find_element_by_css_selector("input.gLFyf.gsfi").send_keys("python\n")
images = driver.find_elements_by_css_selector("img.rg_i")
urls = set()

def check(images):
    for image in images:
        if not image in urls and not image.get_attribute("src").startswith("data:image"):
            return image.get_attribute("src")
    return None

for image in images:
    image.click()
    options = driver.find_elements_by_css_selector("img.n3VNCb")
    while not (image := check(options)):
        time.sleep(0.1)
    urls.update([image])

driver.close()

for url in urls:
    with requests.get(url) as result:
        filename = result.url.split("?")[0].split("#")[0].split("/")[-1].replace("*","")
        if not "." in filename:
            continue
        with open(filename,"wb") as file:
            file.write(result.content)