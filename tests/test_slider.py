from pages.slider import Slider
from selenium.webdriver import Keys
from conftest import browser

def test_slider_v3(browser):
    slider = Slider(browser)

    slider.visit()
    assert slider.slider.exist()
    assert slider.field_input.exist()

    while not slider.field_input.get_dom_attribute('value') == '50':
        slider.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider.field_input.get_dom_attribute('value') == '50'