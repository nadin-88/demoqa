from pages.modal_dialogs import ModalDialogs
import time


def test_small_and_large_buttons(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.btnSmallModal.exist()
    assert modal_dialogs.btnLargeModal.exist()
    assert not modal_dialogs.modal_windows.exist()

    modal_dialogs.btnSmallModal.click()
    time.sleep(2)
    assert modal_dialogs.modal_windows.exist()
    assert modal_dialogs.title_SmallModal.get_text() == 'Small Modal'
    assert modal_dialogs.btnCloseSmallModal.exist()
    modal_dialogs.btnCloseSmallModal.click()
    time.sleep(2)
    assert not modal_dialogs.modal_windows.exist()

    modal_dialogs.btnLargeModal.click()
    time.sleep(2)
    assert modal_dialogs.modal_windows.exist()
    assert modal_dialogs.title_LargeModal.get_text() == 'Large Modal'
    assert modal_dialogs.btnCloseLargeModal.exist()
    modal_dialogs.btnCloseLargeModal.click()
    time.sleep(2)
    assert not modal_dialogs.modal_windows.exist()