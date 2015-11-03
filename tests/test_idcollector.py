import requests

from imdb.idcollector import IdCollector


class TestIdCollector(object):

    def test_init(self):
        id_collector = IdCollector()
        assert id_collector.ids_list == []
        assert id_collector.html.status_code == 200 

    def test_parse_html_for_links(self):
        instance = IdCollector()
        links = instance._parse_html_for_links()
        assert len(links) == 250

    def test_get_ids_100(self):
        instance = IdCollector()
        instance.get_ids(100)
        assert len(instance.ids_list) == 100

    def test_get_ids_10(self):
        instance = IdCollector()
        instance.get_ids(10)
        assert len(instance.ids_list) == 10

    def test_get_ids_200(self):
        instance = IdCollector()
        instance.get_ids(200)
        assert len(instance.ids_list) == 200

    def test_get_ids_300(self):
        instance = IdCollector()
        instance.get_ids(300)
        assert len(instance.ids_list) == 250

#@pytest.mark.parametrize('param, result', )
#@mock.patch()