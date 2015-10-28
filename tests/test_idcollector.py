from idcollector import IdCollector

def test_parse_html_for_links():
    instance = IdCollector()
    links = instance._parse_html_for_links()
    assert len(links) == 250