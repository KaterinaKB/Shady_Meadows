import logging

import pytest
from selene import browser
from selenium import webdriver
from project_config import project_config
from shady_meadows.data.client_and_booking import client
from shady_meadows.model.application import app
from shady_meadows.utils import attachments as attach


@pytest.fixture(scope="function")
def setup_browser():
    options = webdriver.ChromeOptions()
    options.browser_version = "100.0"
    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True,
        },
    )
    options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})

    browser.config.driver_options = options

    browser.config.driver_remote_url = (
        f"https://{project_config.login}:{project_config.password}@"
        f"selenoid.autotests.cloud/wd/hub"
    )

    browser.config.base_url = "https://automationintesting.online"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_logs(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture()
def delete_data_after_test():
    yield
    app.api.find_booking_id_and_delete_booking(client)


