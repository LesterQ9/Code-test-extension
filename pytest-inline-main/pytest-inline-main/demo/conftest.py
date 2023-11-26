from py.xml import html
import pytest
from time import strftime
from pytest_metadata.plugin import metadata_key


def pytest_configure(config):
    config.stash[metadata_key]["start time"] = strftime('%Y-%m-%d %H:%M:%S')

def pytest_html_report_title(report):
    report.title = "The pytest-inline report"



@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["enviroment"] = "http://xxxxxx"