import pytest

from .model import PageBarcoCom


@pytest.fixture(scope='session', params=[language for language in PageBarcoCom.Language])
def barco_com_language(request):
    return request.param
