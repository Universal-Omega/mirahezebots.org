"""Test rendering of HTML by Flask."""
from MirahezeBots_jsonparser import jsonparser as jp

from app import display_content


def test_about_page():
    """Tests about page."""
    content = display_content('about', jp.createdict('./config.json'))
    assert 'IRC' in content  # nosec
