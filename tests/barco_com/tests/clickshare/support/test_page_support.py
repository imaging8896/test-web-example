from hamcrest import assert_that, equal_to


def test_user_can_see_get_warranty_ui_components(browser_user, page_clickshare_support_get_warranty_info):
    browser_user.browse(page_clickshare_support_get_warranty_info.url)

    assert_that(browser_user.see_webpage_url(), equal_to(page_clickshare_support_get_warranty_info.url))

    browser_user.click(page_clickshare_support_get_warranty_info.one_trust_button)
