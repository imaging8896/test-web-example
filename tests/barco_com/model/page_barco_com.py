import enum

from ...model import Page


class PageBarcoCom(Page):

    @enum.unique
    class Language(enum.Enum):
        Deutsch = "de"
        English = "en"
        Spanish = "es"
        French = "fr"
        Italiano = "it"
        Japanese = "ja"
        Korean = "ko"
        Nederlands = "nl"
        Polish = "pl"
        Portuguese = "pt"
        Russian = "ru"
        SimplifiedChinese = "zh-cn"

    def __init__(self, language: Language, region: str, url_path: str) -> None:
        self.language = language
        self.region = region
        self.url_path = url_path

        super().__init__(f"https://www.barco.com/{language.value}/{url_path}")
