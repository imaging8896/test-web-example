from ... import PageBarcoCom


class PageClickshareSupportGetWarrantyInfo(PageBarcoCom):
    
    def __init__(self, language: PageBarcoCom.Language, region: str) -> None:
        super().__init__(language, region, "clickshare/support/warranty-info")
