from hamcrest import assert_that, equal_to, is_


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


def test_user_can_see_correct_warranty_results_ui_components(browser_user, page_clickshare_support_get_warranty_info, data_warranty_info, get_page_trust_cookies_func):
    page = page_clickshare_support_get_warranty_info

    browser_user.browse(page.url, get_page_trust_cookies_func(browser_user, page))
    assert_that(browser_user.wait_to_see_webpage_url(page.url, 5), is_(True))

    serial_num_input = page.get_warranty_info_component.body_serial_num_input
    assert_that(len(browser_user.wait_to_get_elements(serial_num_input, 3)), equal_to(1))

    browser_user.fill_in_input_value(serial_num_input, data_warranty_info.serial_num)

    assert_that(browser_user.see_element_value(serial_num_input), equal_to(data_warranty_info.serial_num))
    del serial_num_input

    get_info_button = page.get_warranty_info_component.body_get_info_button
    assert_that(len(browser_user.wait_to_get_elements(get_info_button, 3)), equal_to(1))
    browser_user.click(get_info_button)
    del get_info_button

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


