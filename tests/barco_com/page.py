import pytest

from .model.page.clickshare.support.page_get_warranty_info import PageClickshareSupportGetWarrantyInfo


@pytest.fixture(scope='session')
def page_clickshare_support_get_warranty_info(page_language, page_region) -> PageClickshareSupportGetWarrantyInfo:
    return PageClickshareSupportGetWarrantyInfo(page_language, page_region)
