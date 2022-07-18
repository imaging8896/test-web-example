import pytest


@pytest.fixture(scope='session', params=[
    "Taiwan, China",
])
def page_region(request):
    return request.param
