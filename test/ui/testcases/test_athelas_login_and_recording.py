import urllib.parse
from test.ui.pages.admin_pages.admin_home_page import AdminHomePage
import test.ui.conftest as cnf
from test.ui.data.data import Data
from test.ui.pages.admin_pages.admin_login_page import LoginPage
from test.ui.pages.admin_pages.admin_provider_page import AdminProviderPage
from test.ui.pages.appointment_screen_page import AppointmentScreenPage
from test.ui.pages.home_screen_page import HomeScreenPage
from test.ui.pages.athelas_scribe_app_page import AthelasScribeAppPage
from test.ui.testcases.base_test import BaseTest
import time

class TestAthelasLoginAndRecording(BaseTest):
    def setup_class(self):
        # self.home_screen_page = HomeScreenPage(self.appium_driver)
        self.athelas_page = AthelasScribeAppPage(self.appium_driver)
        self.data = Data()

    def test_login_record_and_logout(self):
        self.athelas_page.wait_for_visibility_of(self.athelas_page.NEW_RECORDING_TITLE,10)
        assert self.athelas_page.is_element_visible(self.athelas_page.SCRIBE_ON_TRIAL_MESSAGE,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.LANDING_PAGE_LOGIN_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.START_RECORDING_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.MENU_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_BUTTON,self.athelas_page.MENU_LOGIN_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_LOGIN_BUTTON,
                                                        self.athelas_page.LOGIN_TITLE)
        assert self.athelas_page.is_element_visible(self.athelas_page.LOGIN_EMAIL_FIELD)
        self.athelas_page.enter_text_at(self.athelas_page.LOGIN_EMAIL_FIELD,self.data.athelas_app_scribe)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.LOGIN_CONTINUE_BUTTON,
                                                        self.athelas_page.LOGIN_PASSWORD_FIELD)
        assert self.athelas_page.is_element_visible(self.athelas_page.LOGIN_PASSWORD_FIELD,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.FINAL_LOGIN_BUTTON,3)
        self.athelas_page.enter_text_at(self.athelas_page.LOGIN_PASSWORD_FIELD,self.data.athelas_scribe_pass)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.FINAL_LOGIN_BUTTON)
        assert self.athelas_page.is_element_visible(self.athelas_page.NEW_RECORDING_TITLE,10)
        assert self.athelas_page.is_element_visible(self.athelas_page.START_RECORDING_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.PATIENT_NAME_TEXT_FIELD,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.CLINICAL_TEMPLATE_DROPDOWN,3)

        self.athelas_page.enter_text_at(self.athelas_page.PATIENT_NAME_TEXT_FIELD,'Test Patient')
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.START_RECORDING_BUTTON,
                                                        self.athelas_page.END_VISIT_BUTTON)
        assert self.athelas_page.is_element_visible(self.athelas_page.END_VISIT_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.PAUSE_BUTTON,3)
        time.sleep(30)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.END_VISIT_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.VISIT_ENDED_CHECK_STATUS_MSG,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.VISIT_ENDED_NOTE_GENERATION_MSG,3)

        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_BUTTON,
                                                        self.athelas_page.MENU_LOGOUT_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_LOGOUT_BUTTON,
                                                        self.athelas_page.LOGOUT_MODAL_BODY)
        assert self.athelas_page.is_element_visible(self.athelas_page.LOGOUT_MODAL_BODY,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.LOGOUT_MODAL_OK_BUTTON,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.LOGOUT_MODAL_CANCEL_BUTTON,3)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.LOGOUT_MODAL_OK_BUTTON)
        assert self.athelas_page.is_element_visible(self.athelas_page.NEW_RECORDING_TITLE,10)
        assert self.athelas_page.is_element_visible(self.athelas_page.SCRIBE_ON_TRIAL_MESSAGE,3)
        assert self.athelas_page.is_element_visible(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON,3)