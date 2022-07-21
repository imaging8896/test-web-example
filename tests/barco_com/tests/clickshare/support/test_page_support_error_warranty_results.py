import pytest

from hamcrest import assert_that, equal_to, is_, is_in


@pytest.mark.parametrize("incorrect_serial_num", [
    "1963552439", 
    "0000000000",
    "123456789",
    "123456789123456789",
    "123456789123456789123456789123456789",
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

    get_warranty_info_loading = page.get_warranty_info_component.body_get_info_button_loading
    assert_that(browser_user.wait_until_element_visible(get_warranty_info_loading, 2), is_(True))
    assert_that(browser_user.wait_until_element_invisible(get_warranty_info_loading, timeout_wait_for_results), is_(True))
    del get_warranty_info_loading

    results_article = page.warranty_results_component.results_article
    error_results_div = page.warranty_results_component.error_results_div
    assert_that(browser_user.see_element(results_article), is_(False))
    assert_that(browser_user.see_element(error_results_div), is_(True))
    del results_article
    del error_results_div

    error_results_header_text =            page.warranty_results_component.error_header_text
    error_results_header_serial_num_text = page.warranty_results_component.error_header_serial_num_text
    assert_that(len(browser_user.wait_to_get_elements(error_results_header_text, 5)), equal_to(1))
    assert_that(len(browser_user.wait_to_get_elements(error_results_header_serial_num_text, 5)), equal_to(1))

    assert_that(browser_user.see_element_text(error_results_header_text), equal_to(f"Warranty results for {incorrect_serial_num}"))
    assert_that(browser_user.see_element_text(error_results_header_serial_num_text), equal_to(incorrect_serial_num))
    assert_that(browser_user.see_element_css_property(error_results_header_serial_num_text, "color"), equal_to(
        {
            "chrome":  "rgba(240, 0, 0, 1)",
            "firefox": "rgb(240, 0, 0)",
            "msedge":  "rgba(240, 0, 0, 1)",
        }[browser_user.driver.name]
    ))
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
