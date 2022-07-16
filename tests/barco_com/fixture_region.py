import pytest

from .model import PageBarcoCom


@pytest.fixture(scope='session', params=[
    "Taiwan, China",
])
def barco_com_region(request):
    return request.param
