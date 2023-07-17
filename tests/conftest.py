import pytest
from selene import browser
# from demoqa.utils import attachments as attach
# from project_config import project_config
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def setup_browser():

    # options = webdriver.ChromeOptions()
    # options.browser_version = '100.0'
    # options.set_capability(
    #     'selenoid:options',
    #     {
    #         'enableVNC': True,
    #         'enableVideo': True,
    #         'enableLog': True,
    #     },
    # )
    # browser.config.driver_options = options
    #
    # browser.config.driver_remote_url = (
    #     f'https://{project_config.login}:{project_config.password}@'
    #     f'selenoid.autotests.cloud/wd/hub'
    # )

    browser.config.base_url = "https://automationintesting.online"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    # attach.add_html(browser)
    # attach.add_logs(browser)
    # attach.add_screenshot(browser)
    # attach.add_video(browser)

    browser.quit()