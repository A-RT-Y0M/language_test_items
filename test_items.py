import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_interface(browser):
    browser.get(link)
    #time.sleep(30)
    basket_button = browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert basket_button, "Button not exist"
    basket_button.click()