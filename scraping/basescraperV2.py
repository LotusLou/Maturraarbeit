from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin


class baseScraper:
    def __init__(self, url: str):
        self.url = url
        self.driver = self.setupDriver()

    def setupDriver(self):
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)

    def open(self, url: str | None = None):
        self.driver.get(url or self.url)

    def _ctx(self, root):
        # root ist entweder WebElement (card) oder None
        return root if root is not None else self.driver

    def find_all(self, xpath: str, root=None, timeout: int = 10):
        ctx = self._ctx(root)
        try:
            return WebDriverWait(ctx, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
        except TimeoutException:
            return []

    def find_one(self, xpath: str, root=None, timeout: int = 10):
        ctx = self._ctx(root)
        try:
            return WebDriverWait(ctx, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            return None

    def get_text(self, xpath: str, root=None, default: str = ""):
        el = self.find_one(xpath, root=root)
        if not el:
            return default
        text = el.text or ""
        return text.strip()

    def get_attr(self, xpath: str, attr: str, root=None, default=None):
        el = self.find_one(xpath, root=root)
        if not el:
            return default
        val = el.get_attribute(attr)
        return val if val is not None else default

    def abs_url(self, href: str | None):
        if not href:
            return None
        return urljoin(self.url, href)

    def close(self):
        self.driver.quit()
