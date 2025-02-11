import time
from test.ui.pages.athelas_scribe_app_page import AthelasScribeAppPage
from test.ui.testcases.base_test import BaseTest
from test.ui.utils.common_assertions import CommonSteps
from test.ui.data.data import Data
import allure
import pytest

@pytest.mark.usefixtures("appium_driver")
class TestAthelasLoginAndRecording(BaseTest, CommonSteps):

    def setup_class(self):
        self.data = Data()
        self.athelas_page = AthelasScribeAppPage(self.appium_driver)
        CommonSteps.setup_class(self)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    def test_login_with_password(self):
        self.athelas_page.wait_for_visibility_of(self.athelas_page.NEW_RECORDING_TITLE, 15)

        with allure.step("Verify landing page elements should be properly shown after opening app"):
            self.common_assertions_for_text(self.athelas_page.SCRIBE_ON_TRIAL_MESSAGE, text="You're on Scribe Trial")
            self.common_assertions_for_button(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON, text='Sign Up')
            self.common_assertions_for_button(self.athelas_page.LANDING_PAGE_LOGIN_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LANDING_PAGE_LOGIN_BUTTON, text='Log In')
            self.common_assertions_for_button(self.athelas_page.START_RECORDING_BUTTON)
            self.common_assertions_for_text(self.athelas_page.START_RECORDING_BUTTON, text='START RECORDING')
            self.common_assertions_for_button(self.athelas_page.MENU_BUTTON)
            self.common_assertions_for_text(self.athelas_page.MENU_BUTTON, text='Menu')

        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_BUTTON, self.athelas_page.MENU_LOGIN_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_LOGIN_BUTTON, self.athelas_page.LOGIN_TITLE)

        with allure.step("Verify login page contents for email"):
            assert self.athelas_page.is_element_visible(self.athelas_page.LOGIN_EMAIL_FIELD)

        if hasattr(pytest, 'provider_email') and pytest.provider_email is not None:
            self.athelas_page.enter_text_at(self.athelas_page.LOGIN_EMAIL_FIELD, pytest.provider_email)
        elif hasattr(pytest, 'login') and pytest.login is not None:
            self.athelas_page.enter_text_at(self.athelas_page.LOGIN_EMAIL_FIELD, pytest.login['email'])
        else:
            self.athelas_page.enter_text_at(self.athelas_page.LOGIN_EMAIL_FIELD, self.data.get("login.email"))

        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.LOGIN_CONTINUE_BUTTON, self.athelas_page.LOGIN_PASSWORD_FIELD)

        with allure.step("Verify login page contents for password"):
            assert self.athelas_page.is_element_visible(self.athelas_page.LOGIN_PASSWORD_FIELD, 3)
            self.common_assertions_for_button(self.athelas_page.FINAL_LOGIN_BUTTON)
            self.common_assertions_for_text(self.athelas_page.FINAL_LOGIN_BUTTON, text='Log In')

        if hasattr(pytest, 'login') and pytest.login is not None:
            self.athelas_page.enter_text_at(self.athelas_page.LOGIN_PASSWORD_FIELD, pytest.login['password'])
        elif hasattr(pytest, 'provider_password') and pytest.provider_password is not None:
            self.athelas_page.enter_text_at(self.athelas_page.LOGIN_PASSWORD_FIELD, pytest.provider_password)
        else:
            self.athelas_page.enter_text_at(self.athelas_page.LOGIN_PASSWORD_FIELD, self.data.get("login.password"))

        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.FINAL_LOGIN_BUTTON)

        with allure.step("Verify login has been completed and proper contents are shown"):
            self.common_assertions_for_text(self.athelas_page.NEW_RECORDING_TITLE, wait_time=10, text='New Recording')
            self.common_assertions_for_button(self.athelas_page.START_RECORDING_BUTTON)
            self.common_assertions_for_text(self.athelas_page.START_RECORDING_BUTTON, text='START RECORDING')
            assert self.athelas_page.is_element_visible(self.athelas_page.PATIENT_NAME_TEXT_FIELD, 3)
            assert self.athelas_page.is_element_visible(self.athelas_page.CLINICAL_TEMPLATE_DROPDOWN, 3)

    
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    def test_create_visit_recording(self):
        self.athelas_page.enter_text_at(self.athelas_page.PATIENT_NAME_TEXT_FIELD, self.data.PATIENT_NAME)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.START_RECORDING_BUTTON, self.athelas_page.END_VISIT_BUTTON)

        with allure.step("Verify pause and end recording buttons are present after starting recording"):
            self.common_assertions_for_button(self.athelas_page.END_VISIT_BUTTON)
            self.common_assertions_for_text(self.athelas_page.END_VISIT_BUTTON, text='End Visit')
            self.common_assertions_for_button(self.athelas_page.PAUSE_BUTTON)
            self.common_assertions_for_text(self.athelas_page.PAUSE_BUTTON, text='PAUSE')

        time.sleep(30)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.END_VISIT_BUTTON, 3)

        with allure.step("Verify proper contents are shown after ending recording"):
            self.common_assertions_for_text(self.athelas_page.VISIT_ENDED_CHECK_STATUS_MSG, text='Check status in My Scribes')
            self.common_assertions_for_text(self.athelas_page.VISIT_ENDED_NOTE_GENERATION_MSG, text='May take a while for transcription and clinical note generation to finish')

    
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    def test_created_appointment_available_in_my_scribes(self):
        self.athelas_page.click_and_wait(self.athelas_page.MY_SCRIBES_BUTTON, 1)

        with allure.step("Verify navigation to my scribes from record screen"):
            self.common_assertions_for_text(self.athelas_page.MY_SCRIBES_HEADER, text='My Scribes')

        with allure.step("Verify the created appointment is available in the list of appointments"):
            assert self.athelas_page.is_element_visible(self.athelas_page.CREATED_PATIENT_NAME, 10)

    
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    def test_logout(self):
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_BUTTON, self.athelas_page.MENU_LOGOUT_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_LOGOUT_BUTTON, self.athelas_page.LOGOUT_MODAL_BODY)

        with allure.step("Verify logout confirmation modal contents"):
            self.common_assertions_for_text(self.athelas_page.LOGOUT_MODAL_BODY, text='Are you sure you want to log out?')
            self.common_assertions_for_button(self.athelas_page.LOGOUT_MODAL_OK_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LOGOUT_MODAL_OK_BUTTON, text='OK')
            self.common_assertions_for_button(self.athelas_page.LOGOUT_MODAL_CANCEL_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LOGOUT_MODAL_CANCEL_BUTTON, text='CANCEL')

        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.LOGOUT_MODAL_OK_BUTTON)

        with allure.step("Verify logout has been completed and proper contents are shown"):
            self.common_assertions_for_text(self.athelas_page.NEW_RECORDING_TITLE, wait_time=10, text='New Recording')
            self.common_assertions_for_text(self.athelas_page.SCRIBE_ON_TRIAL_MESSAGE, text="You're on Scribe Trial")
            self.common_assertions_for_button(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON, text='Sign Up')