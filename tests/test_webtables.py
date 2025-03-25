import time
from pages.tables import Tables

def test_tables(browser):
	"""Проверка блока No rows found"""
	page_tables = Tables(browser)

	page_tables.visit()
	assert not page_tables.no_data.exist()

	"""Удаляем все записи"""
	while page_tables.btn_delete_row.exist():
		page_tables.btn_delete_row.click()

	time.sleep(2)
	assert page_tables.no_data.exist()


def test_registration_webtables(browser):
	web_tables = Tables(browser)
	web_tables.visit()

	assert web_tables.btn_add_new_record.exist()
	web_tables.btn_add_new_record.click()
	assert web_tables.dialog_box_registration_form.exist()

	assert not web_tables.user_form.get_dom_attribute('class') == 'was-validated'
	web_tables.btn_submit.click()
	assert web_tables.user_form.get_dom_attribute('class') == 'was-validated'
	browser.refresh()

	web_tables.btn_add_new_record.click()
	web_tables.first_name.send_keys('Jenifer')
	web_tables.last_name.send_keys('Aniston')
	web_tables.email.send_keys('test@test.eu')
	web_tables.age.send_keys('45')
	web_tables.salary.send_keys('5000')
	web_tables.departament.send_keys('Drama')
	assert web_tables.dialog_box_registration_form.exist()
	web_tables.btn_submit.click()
	time.sleep(4)
	assert not web_tables.dialog_box_registration_form.exist()

	assert web_tables.added_new_first_name.get_text() == 'Jenifer'
	assert web_tables.added_new_last_name.get_text() == 'Aniston'
	assert web_tables.added_new_email.get_text() == 'test@test.eu'
	assert web_tables.added_new_departament.get_text() == 'Drama'
	time.sleep(4)

	web_tables.btn_edit_new_record.click()
	assert web_tables.dialog_box_registration_form.exist()
	assert web_tables.first_name.get_dom_attribute('value') == 'Jenifer'
	assert web_tables.last_name.get_dom_attribute('value') == 'Aniston'
	assert web_tables.email.get_dom_attribute('value') == 'test@test.eu'
	assert web_tables.departament.get_dom_attribute('value') == 'Drama'

	time.sleep(4)
	web_tables.first_name.clear()
	time.sleep(4)
	assert web_tables.first_name.get_text() == ''
	time.sleep(4)
	web_tables.first_name.send_keys('Jenny')
	time.sleep(4)
	web_tables.btn_submit.click()
	assert web_tables.added_new_first_name.get_text() == 'Jenny'
	time.sleep(4)

	web_tables.btn_delete_new_record.click()
	time.sleep(4)
	assert not web_tables.added_new_first_name.get_text() == 'Jenifer'
	assert not web_tables.added_new_last_name.get_text() == 'Aniston'
	assert not web_tables.added_new_email.get_text() == 'test@test.eu'
	assert not web_tables.added_new_departament.get_text() == 'Drama'

	time.sleep(4)