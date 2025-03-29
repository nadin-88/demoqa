import time
from pages.tables import Tables

def test_sort(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    headers = [page_tables.header_first_name,
              page_tables.header_last_name,
              page_tables.header_email,
              page_tables.header_age,
              page_tables.header_salary,
              page_tables.header_department,
              page_tables.header_action]

    for header in headers:
        assert header.exist()
        assert header.get_dom_attribute('class') == "rt-th rt-resizable-header -cursor-pointer"
        header.click()
        time.sleep(2)
        assert header.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
        header.click()
        time.sleep(2)
        assert header.get_dom_attribute('class') == "rt-th rt-resizable-header -sort-desc -cursor-pointer"
        time.sleep(2)