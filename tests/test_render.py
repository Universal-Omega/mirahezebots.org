from .app import display_content


def test_about_page():
    content = display_content('about', jp.createdict('../config.json'))
    assert 'IRC' in content
