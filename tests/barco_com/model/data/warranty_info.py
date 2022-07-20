from dataclasses import dataclass


@dataclass
class WarrantyInfo:
    serial_num: str
    desc: str
    part_num: str
    delivery_date: str
    installation_date: str
    warranty_end_date: str
    service_contract_end_date: str
    image_url: str
