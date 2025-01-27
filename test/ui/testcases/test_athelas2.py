from ftplib import all_errors
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
import allure
from test.ui.utils.common_assertions import CommonSteps
import threading
import pytest

class TestAthelasLoginAndRecording(BaseTest,CommonSteps):
    @pytest.fixture(scope="class")
    def drivers(self):
        self.data = Data()
        CommonSteps.setup_class(self)

        server1 = 'http://localhost:4723'
        server2 = 'http://localhost:4724'
        apk_type = 'go'
        change_device_time = False
        auto_accept_alert = False
        use_simulator = True

        drivers = {}

        # Initialize both drivers
        drivers["driver1"] = cnf.get_selected_device(apk_type=apk_type, 
                                                    change_device_time=change_device_time, 
                                                    auto_accept_alert=auto_accept_alert, 
                                                    url=server1)
        drivers["driver2"] = cnf.get_selected_device(apk_type=apk_type, 
                                                    change_device_time=change_device_time, 
                                                    auto_accept_alert=auto_accept_alert, 
                                                    url=server2, 
                                                    use_simulator=use_simulator)

        yield drivers

        # Cleanup
        drivers["driver1"].quit()
        drivers["driver2"].quit()

    @pytest.mark.parametrize("driver_key", ["driver1", "driver2"])
    def test_login_with_password(self, driver_key, drivers):
        self.athelas_page = drivers[driver_key]
        self.athelas_page.wait_for_visibility_of(self.athelas_page.NEW_RECORDING_TITLE,10)
        with allure.step("Verify landing page elements should be properly shown after opening app"):
            self.common_assertions_for_text(self.athelas_page.SCRIBE_ON_TRIAL_MESSAGE,
                                            text="You're on Scribe Trial")
            self.common_assertions_for_button(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON,
                                            text='Sign Up')
            self.common_assertions_for_button(self.athelas_page.LANDING_PAGE_LOGIN_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LANDING_PAGE_LOGIN_BUTTON,
                                            text='Log In')
            self.common_assertions_for_button(self.athelas_page.START_RECORDING_BUTTON)
            self.common_assertions_for_text(self.athelas_page.START_RECORDING_BUTTON,
                                            text='START RECORDING')
            self.common_assertions_for_button(self.athelas_page.MENU_BUTTON)
            self.common_assertions_for_text(self.athelas_page.MENU_BUTTON,
                                            text='Menu')
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_BUTTON,self.athelas_page.MENU_LOGIN_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_LOGIN_BUTTON,
                                                        self.athelas_page.LOGIN_TITLE)
        with allure.step("Verify login page contents for email"):
            assert self.athelas_page.is_element_visible(self.athelas_page.LOGIN_EMAIL_FIELD)
        self.athelas_page.enter_text_at(self.athelas_page.LOGIN_EMAIL_FIELD,self.data.athelas_app_scribe)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.LOGIN_CONTINUE_BUTTON,
                                                        self.athelas_page.LOGIN_PASSWORD_FIELD)
        with allure.step("Verify login page contents for password"):
            assert self.athelas_page.is_element_visible(self.athelas_page.LOGIN_PASSWORD_FIELD,3)
            self.common_assertions_for_button(self.athelas_page.FINAL_LOGIN_BUTTON)
            self.common_assertions_for_text(self.athelas_page.FINAL_LOGIN_BUTTON,
                                            text='Log In')
        self.athelas_page.enter_text_at(self.athelas_page.LOGIN_PASSWORD_FIELD,self.data.athelas_scribe_pass)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.FINAL_LOGIN_BUTTON)
        with allure.step("Verify login has been completed and proper contents are shown"):
            self.common_assertions_for_text(self.athelas_page.NEW_RECORDING_TITLE,wait_time=10,
                                            text='New Recording')
            self.common_assertions_for_button(self.athelas_page.START_RECORDING_BUTTON)
            self.common_assertions_for_text(self.athelas_page.START_RECORDING_BUTTON,
                                            text='START RECORDING')
            assert self.athelas_page.is_element_visible(self.athelas_page.PATIENT_NAME_TEXT_FIELD,3)
            assert self.athelas_page.is_element_visible(self.athelas_page.CLINICAL_TEMPLATE_DROPDOWN,3)


    def test_create_visit_recording(self):
        self.athelas_page.enter_text_at(self.athelas_page.PATIENT_NAME_TEXT_FIELD,'Test Patient')
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.KEYBOARD_DONE_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.START_RECORDING_BUTTON,
                                                        self.athelas_page.END_VISIT_BUTTON)
        with allure.step("Verify pause and end recording buttons are present after starting recording"):
            self.common_assertions_for_button(self.athelas_page.END_VISIT_BUTTON)
            self.common_assertions_for_text(self.athelas_page.END_VISIT_BUTTON,
                                            text='End Visit')
            self.common_assertions_for_button(self.athelas_page.PAUSE_BUTTON)
            self.common_assertions_for_text(self.athelas_page.PAUSE_BUTTON,
                                            text='PAUSE')
        time.sleep(30)
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.END_VISIT_BUTTON,3)
        with allure.step("Verify proper contents are shown after ending recording"):
            self.common_assertions_for_text(self.athelas_page.VISIT_ENDED_CHECK_STATUS_MSG,
                                            text='Check status in My Scribes')
            self.common_assertions_for_text(self.athelas_page.VISIT_ENDED_NOTE_GENERATION_MSG,
                                            text='May take a while for transcription and clinical note generation to finish')

    def test_logout(self):
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_BUTTON,
                                                        self.athelas_page.MENU_LOGOUT_BUTTON)
        self.athelas_page.click_and_wait_for_visibility(self.athelas_page.MENU_LOGOUT_BUTTON,
                                                        self.athelas_page.LOGOUT_MODAL_BODY)
        with allure.step("Verify logout confirmation modal contents"):
            self.common_assertions_for_text(self.athelas_page.LOGOUT_MODAL_BODY,
                                            text='Are you sure you want to log out?')
            self.common_assertions_for_button(self.athelas_page.LOGOUT_MODAL_OK_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LOGOUT_MODAL_OK_BUTTON,
                                            text='OK')
            self.common_assertions_for_button(self.athelas_page.LOGOUT_MODAL_CANCEL_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LOGOUT_MODAL_CANCEL_BUTTON,
                                            text='CANCEL')
        self.athelas_page.click_and_wait_for_invisibility(self.athelas_page.LOGOUT_MODAL_OK_BUTTON)
        with allure.step("Verify logout has been completed and proper contents are shown"):
            self.common_assertions_for_text(self.athelas_page.NEW_RECORDING_TITLE,wait_time=10,
                                            text='New Recording')
            self.common_assertions_for_text(self.athelas_page.SCRIBE_ON_TRIAL_MESSAGE,
                                            text="You're on Scribe Trial")
            self.common_assertions_for_button(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON)
            self.common_assertions_for_text(self.athelas_page.LANDING_PAGE_SIGN_UP_BUTTON,
                                            text='Sign Up')