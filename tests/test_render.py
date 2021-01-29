from .app import display_content

from MirahezeBots_jsonparser import jsonparser as jp


def test_about_page():
    """Tests about page."""
    content = display_content('about', jp.createdict('../config.json'))
    assert 'IRC' in content
