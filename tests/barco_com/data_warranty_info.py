import pytest

from .model.data.warranty_info import WarrantyInfo


@pytest.fixture(scope='session', params=[
    WarrantyInfo(
        serial_num="1863552437", 
        desc="CLICKSHARE CX-50 SET NA", 
        part_num="R9861522NA",
        delivery_date="05/07/2020 00:00:00",
        installation_date="09/28/2020 09:16:22",
        warranty_end_date="09/27/2021 09:16:22",
        service_contract_end_date="01/01/0001 00:00:00",
        image_url="https://az877327.vo.msecnd.net/~/media/clickshare2020/images/product%20shots%20-%20transparent/cx-50_buttons_top%20png.png?v=1"
    ), # You can add correct warranty info test data here
])
def data_warranty_info(request) -> WarrantyInfo:
    # Prepare data here
    yield request.param
    # Teardown data here
