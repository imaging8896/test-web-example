import pytest

from .model import PageBarcoCom


@pytest.fixture(scope='function')
def page_barco_com_clickshare_support(barco_com_language, barco_com_region):
    page = PageClickshareSupport(barco_com_language, barco_com_region)
    return page


class PageClickshareSupport(PageBarcoCom):
    
    def __init__(self, language: PageBarcoCom.Language, region: str) -> None:
        super().__init__(language, region, "clickshare/support")
