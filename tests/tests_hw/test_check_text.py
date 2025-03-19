from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_footer.get_text() =='© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_text_center(browser):
    demo_qa_page = DemoQa(browser)
    elem_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elem_page.text_center.get_text() == 'Please select an item from left to start practice.'


#lecture8
def test_page_elements(browser):
    elem_page = ElementsPage(browser)
    elem_page.visit()
    assert elem_page.icon.exist()
    assert elem_page.btn_sidebar_first.exist()
    assert elem_page.btn_sidebar_first_textbox.exist()
