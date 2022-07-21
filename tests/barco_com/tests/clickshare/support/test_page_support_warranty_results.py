import pytest

from hamcrest import assert_that, equal_to, is_


@pytest.mark.parametrize("timeout_wait_for_results", [5])
def test_user_can_see_correct_warranty_results_ui_components(browser_user, page_clickshare_support_get_warranty_info, data_warranty_info, get_page_trust_cookies_func, timeout_wait_for_results):
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

    get_warranty_info_loading = page.get_warranty_info_component.body_get_info_button_loading
    assert_that(browser_user.wait_until_element_visible(get_warranty_info_loading, 2), is_(True))
    assert_that(browser_user.wait_until_element_invisible(get_warranty_info_loading, timeout_wait_for_results), is_(True))
    del get_warranty_info_loading

    results_article = page.warranty_results_component.results_article
    error_results_div = page.warranty_results_component.error_results_div
    assert_that(browser_user.see_element(results_article), is_(True))
    assert_that(browser_user.see_element(error_results_div), is_(False))
    del results_article
    del error_results_div

    results_header_text =            page.warranty_results_component.header_text
    results_header_serial_num_text = page.warranty_results_component.header_serial_num_text
    assert_that(len(browser_user.wait_to_get_elements(results_header_text, 5)), equal_to(1))
    assert_that(len(browser_user.wait_to_get_elements(results_header_serial_num_text, 5)), equal_to(1))

    assert_that(browser_user.see_element_text(results_header_text), equal_to(f"Warranty results for {data_warranty_info.serial_num}"))
    assert_that(browser_user.see_element_text(results_header_serial_num_text), equal_to(data_warranty_info.serial_num))
    assert_that(browser_user.see_element_css_property(results_header_serial_num_text, "color"), equal_to(
        {
            "chrome":  "rgba(240, 0, 0, 1)",
            "firefox": "rgb(240, 0, 0)",
            "msedge":  "rgba(240, 0, 0, 1)",
        }[browser_user.driver.name]
    ))
    del results_header_text
    del results_header_serial_num_text

    results_fields_headers = page.warranty_results_component.fields_headers
    results_fields =         page.warranty_results_component.fields
    assert_that(len(browser_user.wait_to_get_elements(results_fields_headers, 5)), equal_to(6))
    assert_that(len(browser_user.wait_to_get_elements(results_fields, 5)), equal_to(6))
    del results_fields_headers
    del results_fields

    for field_header_text, expect_header_text in [
        (page.warranty_results_component.desc_header_text, "Description"),
        (page.warranty_results_component.part_num_header_text, "Part number"),
        (page.warranty_results_component.delivery_date_header_text, "Delivery date"),
        (page.warranty_results_component.installation_date_header_text, "Installation date"),
        (page.warranty_results_component.warranty_end_date_header_text, "Warranty end date"),
        (page.warranty_results_component.service_contract_end_date_header_text, "Service contract end date"),
    ]:
        assert_that(len(browser_user.wait_to_get_elements(field_header_text, 5)), equal_to(1))
        assert_that(browser_user.see_element_text(field_header_text), equal_to(expect_header_text))
