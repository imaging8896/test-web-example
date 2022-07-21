from ... import PageBarcoCom


class PageClickshareSupportGetWarrantyInfo(PageBarcoCom):
    
    def __init__(self, language: PageBarcoCom.Language, region: str) -> None:
        super().__init__(language, region, "clickshare/support/warranty-info")

        self.get_warranty_info_component = ComponentGetWarrantyInfo()
        self.warranty_results_component =  ComponentWarrantyResults()


class ComponentGetWarrantyInfo:
    root = ".//div[@class='content-body']/section/div/div[1]/div"

    header_text = f"{root}/div[1]/h1"

    body_serial_num_label = f"{root}/div[2]/div[1]/div[1]/label"
    body_serial_num_input = f"{root}/div[2]/div[1]/div[1]/input"
    body_serial_num_displayed_error_span = f"{root}/div[2]/div[1]/div[1]/span[@style='']"

    body_get_info_button = f"{root}/div[2]/div[1]/div[2]/button"

    body_policy_link = f"{root}/div[2]/div[2]/div/a"


class ComponentWarrantyResults:
    results_div = f".//div[@class='content-body']/section/div/div[2]"
    root =        f"{results_div}/div/div"

    header_text =            f"{root}/article/div/h2"
    header_serial_num_text = f"{root}/article/div/h2/span"

    error_header_text =            f"{root}/div/h2"
    error_header_serial_num_text = f"{root}/div/h2/span"
    error_p =                      f"{root}/div/div/p"
    error_link =                   f"{root}/div/div/a"

    image = f"{root}/article/div/div/div[1]/div/div/img"

    fields_headers = f"{root}/article/div/div/div[2]/dl/dt"
    fields =         f"{root}/article/div/div/div[2]/dl/dd"

    desc_header_text = f"{root}/article/div/div/div[2]/dl/dt[1]"
    desc_text =        f"{root}/article/div/div/div[2]/dl/dd[1]"

    part_num_header_text = f"{root}/article/div/div/div[2]/dl/dt[2]"
    part_num_text =        f"{root}/article/div/div/div[2]/dl/dd[2]"

    delivery_date_header_text = f"{root}/article/div/div/div[2]/dl/dt[3]"
    delivery_date_text =        f"{root}/article/div/div/div[2]/dl/dd[3]"

    installation_date_header_text = f"{root}/article/div/div/div[2]/dl/dt[4]"
    installation_date_text =        f"{root}/article/div/div/div[2]/dl/dd[4]"

    warranty_end_date_header_text = f"{root}/article/div/div/div[2]/dl/dt[5]"
    warranty_end_date_text =        f"{root}/article/div/div/div[2]/dl/dd[5]"

    service_contract_end_date_header_text = f"{root}/article/div/div/div[2]/dl/dt[6]"
    service_contract_end_date_text =        f"{root}/article/div/div/div[2]/dl/dd[6]"
