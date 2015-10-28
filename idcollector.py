# -*- coding: utf-8 -*-

# 2.parse html and export ids tylko do tego projektu

import re
import sys

from bs4 import BeautifulSoup

from get_html import GetHTML


class IdCollector(object):
    def __init__(self):
        self.html = GetHTML("http://www.imdb.com/chart/top?ref=ft_250").data_request()
        self.ids_list = []
        self.links = None

    def _parse_html_for_links(self):
        parsed_text = BeautifulSoup(self.html.text, "html.parser")
        self.links = parsed_text.find_all('a', title=True, href=re.compile("^/title/"))
        return self.links

    def get_ids(self, limit): #parse html funkcja
        # returns list of top imdb id's up to a limit
        links = self._parse_html_for_links()
        count = 0  #counter to limit items to limit

        for link in links:
            if count >= limit:
                    break
            count += 1
            #get fragment of the link containing imdb tt id
            tt=link.get('href')[7:16]
            self.ids_list.append(tt)

        return self.ids_list
        