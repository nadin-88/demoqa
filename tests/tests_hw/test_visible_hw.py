from pages.accordion import Accordion

import time
def test_visible_accordion(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert accordion.what_lorem_ipsum.visible()
    accordion.head_what_lorem_ipsum.click()
    time.sleep(2)
    assert not accordion.what_lorem_ipsum.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.where_lorem_ipsum1.visible()
    assert not accordion.where_lorem_ipsum2.visible()
    assert not accordion.why_lorem_ipsum.visible()


