import enum


class PageBarcoCom:

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
        self.domain = "https://www.barco.com"
        self.url = f"{self.domain}/{language.value}/{url_path}"

    @property
    def trust_cookies_button(self) -> str:
        return ".//div[@id='onetrust-button-group']/div/button"
