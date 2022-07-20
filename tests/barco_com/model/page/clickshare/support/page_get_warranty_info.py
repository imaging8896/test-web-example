from ... import PageBarcoCom


class PageClickshareSupportGetWarrantyInfo(PageBarcoCom):
    
    def __init__(self, language: PageBarcoCom.Language, region: str) -> None:
        super().__init__(language, region, "clickshare/support/warranty-info")

        self.get_warranty_info_component = ComponentGetWarrantyInfo()


class ComponentGetWarrantyInfo:
    root = ".//div[@class='content-body']/section/div/div[1]/div"

    header_text = f"{root}/div[1]/h1"

    body_serial_num_label = f"{root}/div[2]/div[1]/div[1]/label"
    body_serial_num_input = f"{root}/div[2]/div[1]/div[1]/input"
    body_serial_num_displayed_error_span = f"{root}/div[2]/div[1]/div[1]/span[@style='']"

    body_get_info_button = f"{root}/div[2]/div[1]/div[2]/button"

    body_policy_link = f"{root}/div[2]/div[2]/div/a"
