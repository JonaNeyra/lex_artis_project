import requests
from bs4 import BeautifulSoup


class HtmlParser:
    """
    Obtener el parse de un sitio web
    """

    def __init__(self, url, verify=False):
        """
        :param url:
        :param verify:
        """
        self.url = url
        self.verify = verify

    def parse(self):
        """
        :return:
        """
        response = requests.get(self.url, verify=self.verify)
        return BeautifulSoup(response.text, 'html.parser')
