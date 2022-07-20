import pytest

from hamcrest import assert_that, equal_to, is_

from .model.page.clickshare.support.page_get_warranty_info import PageClickshareSupportGetWarrantyInfo


@pytest.fixture(scope='function') # session will get thread bug for Chrome driver
def get_page_trust_cookies_func():
    def _prepare_func(browser_user, page):
        def _func():
            trust_cookies_button = page.trust_cookies_button
            assert_that(len(browser_user.wait_to_get_elements(trust_cookies_button, 10)), equal_to(1))
            assert_that(browser_user.wait_element_clickable(trust_cookies_button, 10), is_(True))

            browser_user.click(trust_cookies_button)
            assert_that(browser_user.wait_until_element_invisible(trust_cookies_button, 5))
        return _func
    return _prepare_func


@pytest.fixture(scope='session')
def page_clickshare_support_get_warranty_info(page_language, page_region) -> PageClickshareSupportGetWarrantyInfo:
    return PageClickshareSupportGetWarrantyInfo(page_language, page_region)
