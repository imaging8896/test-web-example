import pytest

from hamcrest import assert_that, equal_to, is_


def test_browse_get_warranty_info_webpage(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func):
    page = page_clickshare_support_get_warranty_info
    
    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))


@pytest.mark.parametrize("timeout_wait_for_results", [5])
def test_user_can_get_warranty_results_for_correct_serial_number(browser_user, page_clickshare_support_get_warranty_info, data_warranty_info, get_page_trust_cookies_func, timeout_wait_for_results):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    browser_user.fill_in_input_value(serial_num_input, data_warranty_info.serial_num)

    assert_that(browser_user.see_element_attribute(serial_num_input, "value"), equal_to(data_warranty_info.serial_num))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    browser_user.click(get_info_button)
    del get_info_button

    results_article = page.warranty_results_component.results_article
    assert_that(browser_user.wait_until_element_visible(results_article, timeout_wait_for_results), is_(True))
    del results_article

    for field_text, expect_text in [
        (page.warranty_results_component.desc_text, data_warranty_info.desc),
        (page.warranty_results_component.part_num_text, data_warranty_info.part_num),
        (page.warranty_results_component.delivery_date_text, data_warranty_info.delivery_date),
        (page.warranty_results_component.installation_date_text, data_warranty_info.installation_date),
        (page.warranty_results_component.warranty_end_date_text, data_warranty_info.warranty_end_date),
        (page.warranty_results_component.service_contract_end_date_text, data_warranty_info.service_contract_end_date),
    ]:
        assert_that(len(browser_user.wait_to_get_elements(field_text, 5)), equal_to(1))
        assert_that(browser_user.see_element_text(field_text), equal_to(expect_text))
        
    results_image = page.warranty_results_component.image
    assert_that(len(browser_user.wait_to_get_elements(results_image, 5)), equal_to(1))
    assert_that(browser_user.see_element_attribute(results_image, "src"), equal_to(data_warranty_info.image_url))
    del results_image
