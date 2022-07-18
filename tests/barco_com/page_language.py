import pytest

from .model.page import PageBarcoCom


@pytest.fixture(scope='session', params=[
    # For all languages
    # language for language in PageBarcoCom.Language
    PageBarcoCom.Language.English
])
def page_language(request):
    return request.param
