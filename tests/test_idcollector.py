from imdb.idcollector import IdCollector

def test_parse_html_for_links():
    instance = IdCollector()
    links = instance._parse_html_for_links()
    assert len(links) == 250

def test_get_ids_100():
    instance = IdCollector()
    instance.get_ids(100)
    assert len(instance.ids_list) == 100

def test_get_ids_10():
    instance = IdCollector()
    instance.get_ids(10)
    assert len(instance.ids_list) == 10

def test_get_ids_200():
    instance = IdCollector()
    instance.get_ids(200)
    assert len(instance.ids_list) == 200

def test_get_ids_300():
    instance = IdCollector()
    instance.get_ids(300)
    assert len(instance.ids_list) == 250