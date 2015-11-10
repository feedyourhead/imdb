import requests
import pytest

from imdb.idcollector import IdCollector


class TestIdCollector(object):

    PARAM_RESULT = [
        (10, 10),
        (100, 100),
        (200, 200),
        (300, 250)
    ]

    def test_init(self):
        id_collector = IdCollector()
        assert id_collector.ids_list == []
        assert id_collector.html.status_code == 200 

    def test_parse_html_for_links(self):
        instance = IdCollector()
        links = instance._parse_html_for_links()
        assert len(links) == 250
    
    @pytest.mark.parametrize(
        "input,expected",
        PARAM_RESULT
    )
    def test_get_ids(self, input, expected):
        instance = IdCollector()
        instance.get_ids(input)
        assert len(instance.ids_list) == expected

    

#@pytest.mark.parametrize('param, result', )
#@mock.patch()
