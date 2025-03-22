from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):

    def __init__(self,driver):
        self.base_url='https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_submenu = WebElement(driver, 'div:nth-child(3) > div > ul >li')
        self.icon = WebElement(driver, '#app > header > a > img')

        self.btnSmallModal = WebElement(driver, '#showSmallModal')
        self.btnLargeModal = WebElement(driver, '#showLargeModal')
        self.btnCloseSmallModal = WebElement(driver, '#closeSmallModal')
        self.btnCloseLargeModal = WebElement(driver, '#closeLargeModal')
        self.title_SmallModal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.title_LargeModal = WebElement(driver, '#example-modal-sizes-title-lg')
        self.modal_windows = WebElement(driver, 'body > div.fade.modal-backdrop.show')
