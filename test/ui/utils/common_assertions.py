
import allure
import pytest

from test.ui.data.data import Data
from test.ui.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pytest_check as check

data = Data()

class CommonSteps:
    """This module contains Common assertions with steps for the test cases"""
    def setup_class(self):
        self.base_page = BasePage(self.appium_driver)

    def common_assertions_for_button(self, button_locator, visible: bool = True, enabled: bool = True, wait_time:int=2):
        try:
            element = self.base_page.get_element(button_locator, wait_time)
        except (NoSuchElementException, TimeoutException):
        # If the button is not found and we expect it to be visible, fail the assertion
            with allure.step(f'Verify button visibility: {visible}'):
                if visible:
                    assert False
                else:
                    # If we expect it not to be visible, we can consider it passed
                    assert not visible
            return

        # If we get here, the element was found

        # Assert visibility
        with allure.step(f'Verify button visibility: {visible}'):
            check.equal(element.is_displayed(), visible)

        # Assert enabled state
        with allure.step(f'Verify button enabled: {enabled} for tap'):
            check.equal(element.is_enabled(), enabled)


    def common_assertions_for_text(self, text_locator, visible: bool = True, enabled: bool = True, text: str = '', wait_time: int = 3):
        try:
            element = self.base_page.get_element(text_locator, wait_time)
        except (NoSuchElementException, TimeoutException):
            # If the text is not found, and we expect it to be visible, fail the assertion
            with allure.step(f'Verify text visibility: {visible}'):
                if visible:
                    assert False
                else:
                    # If we expect it not to be visible, we can consider it passed
                    assert not visible
            return
            
        # If we get here, the element was found

        with allure.step(f'Verify text visibility: {visible}'):
            # Assert visibility
            check.equal(element.is_displayed(), visible)
        with allure.step(f'Verify text should match with `{text}` '):
            # Assert text
            check.equal(element.text, text)
        # Assert enabled state
        with allure.step(f'Verify text enabled: {enabled} for tap'):
            check.equal(element.is_enabled(), enabled)

    def common_assertions_for_image(self, image_locator, visible: bool = True, enabled: bool = True, wait_time: int = 3):
        try:
            element = self.base_page.get_element(image_locator, wait_time)
        except (NoSuchElementException, TimeoutException):
            # If the text is not found, and we expect it to be visible, fail the assertion
            with allure.step(f'Verify button visibility: {visible}'):
                if visible:
                    assert False
                else:
                    # If we expect it not to be visible, we can consider it passed
                    assert not visible
            return

        # If we get here, the element was found
        with allure.step(f'Verify image visibility: {visible}'):
            # Assert visibility
            check.equal(element.is_displayed(), visible)

        # Assert enabled state
        with allure.step(f'Verify image enabled: {enabled} for tap'):
            check.equal(element.is_enabled(), enabled)