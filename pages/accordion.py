from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):
    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.what_lorem_ipsum = WebElement(driver, '#section1Content > p')
        self.where_lorem_ipsum1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.where_lorem_ipsum2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.why_lorem_ipsum = WebElement(driver, '#section3Content > p')
        self.head_what_lorem_ipsum = WebElement(driver, '#section1Heading')