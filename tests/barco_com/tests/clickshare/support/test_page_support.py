import pytest

from hamcrest import assert_that, equal_to, is_, is_in


def test_browse_get_warranty_info_webpage(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func):
    page = page_clickshare_support_get_warranty_info
    
    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))


def test_user_can_see_get_warranty_ui_components(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    header_text = page.get_warranty_info_component.header_text
    assert_that(len(browser_user.wait_to_get_elements(header_text, 3)), equal_to(1))
    assert_that(browser_user.wait_to_see_element_contain_text(header_text, "Check your ClickShare warranty", 3), is_(True))
    assert_that(browser_user.see_element_text(header_text), equal_to("Check your ClickShare warranty"))
    del header_text
    
    serial_num_label = page.get_warranty_info_component.body_serial_num_label
    assert_that(len(browser_user.wait_to_get_elements(serial_num_label, 3)), equal_to(1))
    assert_that(browser_user.wait_to_see_element_contain_text(serial_num_label, "Serial number", 3), is_(True))
    assert_that(browser_user.see_element_text(serial_num_label), equal_to("Serial number"))
    del serial_num_label

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    assert_that(browser_user.wait_to_see_element_contain_text(get_info_button, "Get info", 3), is_(True))
    assert_that(browser_user.see_element_text(get_info_button), equal_to("Get info"))
    del get_info_button


def test_user_can_see_forcus_effect_when_hovering_over_serial_num_input(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    assert_that(browser_user.see_element_css_property(serial_num_input, "border"), equal_to("1px solid rgb(0, 0, 0)"))
    # 有其他 CSS 要驗證就要 RD 提供期望答案
    browser_user.hover_over(serial_num_input)
    assert_that(browser_user.see_element_css_property(serial_num_input, "border"), equal_to("2px solid rgb(0, 0, 0)"))


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

    results_div = page.warranty_results_component.results_div
    assert_that(browser_user.wait_until_element_visible(results_div, timeout_wait_for_results), is_(True))
    del results_div

    results_header_text =            page.warranty_results_component.header_text
    results_header_serial_num_text = page.warranty_results_component.header_serial_num_text
    assert_that(len(browser_user.wait_to_get_elements(results_header_text, 5)), equal_to(1))
    assert_that(len(browser_user.wait_to_get_elements(results_header_serial_num_text, 5)), equal_to(1))

    assert_that(browser_user.see_element_text(results_header_text), equal_to(f"Warranty results for {data_warranty_info.serial_num}"))
    assert_that(browser_user.see_element_text(results_header_serial_num_text), equal_to(data_warranty_info.serial_num))

    print(browser_user.driver.name)
    if browser_user.driver.name == "chrome":
        assert_that(browser_user.see_element_css_property(results_header_serial_num_text, "color"), equal_to("rgba(240, 0, 0, 1)"))
    else:
        assert_that(browser_user.see_element_css_property(results_header_serial_num_text, "color"), equal_to("rgb(240, 0, 0)"))
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


@pytest.mark.parametrize("incorrect_serial_num", [
    "1963552439", 
    "0000000000"
])
@pytest.mark.parametrize("timeout_wait_for_results", [10]) # XXX Issue
def test_user_can_see_incorrect_warranty_results_ui_components(browser_user, page_clickshare_support_get_warranty_info, incorrect_serial_num, get_page_trust_cookies_func, timeout_wait_for_results):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    browser_user.fill_in_input_value(serial_num_input, incorrect_serial_num)

    assert_that(browser_user.see_element_attribute(serial_num_input, "value"), equal_to(incorrect_serial_num))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    browser_user.click(get_info_button)
    del get_info_button

    results_div = page.warranty_results_component.results_div
    assert_that(browser_user.wait_until_element_visible(results_div, timeout_wait_for_results), is_(True))
    del results_div

    error_results_header_text =            page.warranty_results_component.error_header_text
    error_results_header_serial_num_text = page.warranty_results_component.error_header_serial_num_text
    assert_that(len(browser_user.wait_to_get_elements(error_results_header_text, 5)), equal_to(1))
    assert_that(len(browser_user.wait_to_get_elements(error_results_header_serial_num_text, 5)), equal_to(1))

    assert_that(browser_user.see_element_text(error_results_header_text), equal_to(f"Warranty results for {incorrect_serial_num}"))
    assert_that(browser_user.see_element_text(error_results_header_serial_num_text), equal_to(incorrect_serial_num))

    print(browser_user.driver.name)
    if browser_user.driver.name == "chrome":
        assert_that(browser_user.see_element_css_property(error_results_header_serial_num_text, "color"), equal_to("rgba(240, 0, 0, 1)"))
    else:
        assert_that(browser_user.see_element_css_property(error_results_header_serial_num_text, "color"), equal_to("rgb(240, 0, 0)"))
    del error_results_header_text
    del error_results_header_serial_num_text

    error_p =    page.warranty_results_component.error_p
    error_link = page.warranty_results_component.error_link
    assert_that(len(browser_user.wait_to_get_elements(error_p, 5)), equal_to(1))
    error_message = browser_user.see_element_text(error_p)
    assert_that(
        error_message, 
        is_in(
            [
                "We couldn't find a product with this serial number. Please double-check the serial number and try again.",
                "We couldn't find a Clickshare product with this serial number. Please double-check the serial number and try again.",
            ]
        )
    )
    if error_message == "We couldn't find a product with this serial number. Please double-check the serial number and try again.":
        assert_that(len(browser_user.wait_to_get_elements(error_link, 5)), equal_to(0))
        # No link
    elif error_message == "We couldn't find a Clickshare product with this serial number. Please double-check the serial number and try again.":
        assert_that(len(browser_user.wait_to_get_elements(error_link, 5)), equal_to(1))
        assert_that(browser_user.see_element_attribute(error_link, "href"), equal_to(f"{page.domain}/support/warranty?serial={incorrect_serial_num}"))
    else:
        raise Exception(f"There is a new error message `{error_message}` or test bug.")

    del error_p
    del error_link
