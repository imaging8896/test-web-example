import pytest

from hamcrest import assert_that, equal_to, is_


def test_user_cannot_get_warranty_results_without_serial_number(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    browser_user.fill_in_input_value(serial_num_input, "")

    assert_that(browser_user.see_element_attribute(serial_num_input, "value"), equal_to(""))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    browser_user.click(get_info_button)
    del get_info_button

    get_warranty_info_loading = page.get_warranty_info_component.body_get_info_button_loading
    assert_that(browser_user.wait_until_element_visible(get_warranty_info_loading, 5), is_(False))
    del get_warranty_info_loading

    results_article = page.warranty_results_component.results_article
    error_results_div = page.warranty_results_component.error_results_div
    assert_that(browser_user.see_element(results_article), is_(False))
    assert_that(browser_user.see_element(error_results_div), is_(False))
    del results_article
    del error_results_div

    serial_num_error_spans = page.get_warranty_info_component.body_serial_num_error_spans
    assert_that(browser_user.wait_until_element_visible(serial_num_error_spans, 5), is_(True))
    user_see_error_spans = browser_user.see_elements(serial_num_error_spans)
    assert_that(len(user_see_error_spans), equal_to(1))
    error_span = user_see_error_spans[0]

    assert_that(error_span.text, equal_to("Please specify a serial number"))
    assert_that(error_span.value_of_css_property("color"), equal_to(
        {
            "chrome":  "rgba(224, 32, 32, 1)",
            "firefox": "rgb(224, 32, 32)",
            "msedge":  "rgba(224, 32, 32, 1)",
        }[browser_user.driver.name]
    ))
    del serial_num_error_spans


@pytest.mark.parametrize("less_6_chars_serial_num", [
    "1", 
    "2",
    "12345",
    "  ",
    "@",
    "$"
])
def test_user_cannot_get_warranty_results_with_less_6_chars_serial_number(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func, less_6_chars_serial_num):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    browser_user.fill_in_input_value(serial_num_input, less_6_chars_serial_num)

    assert_that(browser_user.see_element_attribute(serial_num_input, "value"), equal_to(less_6_chars_serial_num))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    browser_user.click(get_info_button)
    del get_info_button

    get_warranty_info_loading = page.get_warranty_info_component.body_get_info_button_loading
    assert_that(browser_user.wait_until_element_visible(get_warranty_info_loading, 5), is_(False))
    del get_warranty_info_loading

    results_article = page.warranty_results_component.results_article
    error_results_div = page.warranty_results_component.error_results_div
    assert_that(browser_user.see_element(results_article), is_(False))
    assert_that(browser_user.see_element(error_results_div), is_(False))
    del results_article
    del error_results_div

    serial_num_error_spans = page.get_warranty_info_component.body_serial_num_error_spans
    assert_that(browser_user.wait_until_element_visible(serial_num_error_spans, 5), is_(True))
    user_see_error_spans = browser_user.see_elements(serial_num_error_spans)
    assert_that(len(user_see_error_spans), equal_to(1))
    error_span = user_see_error_spans[0]

    assert_that(error_span.text, equal_to("Minimum 6 characters required"))
    assert_that(error_span.value_of_css_property("color"), equal_to(
        {
            "chrome":  "rgba(224, 32, 32, 1)",
            "firefox": "rgb(224, 32, 32)",
            "msedge":  "rgba(224, 32, 32, 1)",
        }[browser_user.driver.name]
    ))
    del serial_num_error_spans


@pytest.mark.skip(reason="Invalid serial number should not post")
@pytest.mark.parametrize("invalid_serial_num", [
    "123456789123456789123456789123456789",
    pytest.param("      ", marks=pytest.mark.skip(reason="6 spaces count as valid serial number")),
    "!@#$%^",
])
def test_user_cannot_get_warranty_results_with_invalid_serial_number(browser_user, page_clickshare_support_get_warranty_info, get_page_trust_cookies_func, invalid_serial_num):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    browser_user.fill_in_input_value(serial_num_input, invalid_serial_num)

    assert_that(browser_user.see_element_attribute(serial_num_input, "value"), equal_to(invalid_serial_num))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    browser_user.click(get_info_button)
    del get_info_button

    # XXX Issue
    get_warranty_info_loading = page.get_warranty_info_component.body_get_info_button_loading
    assert_that(browser_user.wait_until_element_visible(get_warranty_info_loading, 5), is_(False))
    del get_warranty_info_loading

    results_article = page.warranty_results_component.results_article
    error_results_div = page.warranty_results_component.error_results_div
    assert_that(browser_user.see_element(results_article), is_(False))
    assert_that(browser_user.see_element(error_results_div), is_(False))
    del results_article
    del error_results_div

    serial_num_error_spans = page.get_warranty_info_component.body_serial_num_error_spans
    assert_that(browser_user.wait_until_element_visible(serial_num_error_spans, 5), is_(True))
    user_see_error_spans = browser_user.see_elements(serial_num_error_spans)
    assert_that(len(user_see_error_spans), equal_to(1))
    error_span = user_see_error_spans[0]

    assert_that(error_span.text, equal_to("Please enter a valid serial number"))
    assert_that(error_span.value_of_css_property("color"), equal_to(
        {
            "chrome":  "rgba(224, 32, 32, 1)",
            "firefox": "rgb(224, 32, 32)",
            "msedge":  "rgba(224, 32, 32, 1)",
        }[browser_user.driver.name]
    ))
    del serial_num_error_spans
