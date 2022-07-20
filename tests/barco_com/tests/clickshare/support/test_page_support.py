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
    assert_that(
        browser_user.wait_to_see_element_contain_text(header_text, "Check your ClickShare warranty", 3), 
        is_(True)
    )
    assert_that(browser_user.see_element_text(header_text), equal_to("Check your ClickShare warranty"))
