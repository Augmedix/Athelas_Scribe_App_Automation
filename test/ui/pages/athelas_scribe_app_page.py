import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import allure

from test.ui.data.data import Data
from test.ui.pages.base_page import BasePage


class AthelasScribeAppPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = Data()

    NEW_RECORDING_TITLE = (AppiumBy.ACCESSIBILITY_ID,'New Recording')
    PATIENT_NAME_TEXT_FIELD = (AppiumBy.ACCESSIBILITY_ID,'Patient Name')
    CLINICAL_TEMPLATE_DROPDOWN = (AppiumBy.XPATH,'//XCUIElementTypeButton[contains(@name,"Clinical Template")]')
    SOAP_TEMPLATE = (AppiumBy.ACCESSIBILITY_ID,'SOAP')
    PROGRESS_NOTE_TEMPLATE = (AppiumBy.ACCESSIBILITY_ID,'Progress Note')
    MEETING_NOTE_TEMPLATE = (AppiumBy.ACCESSIBILITY_ID,'Meeting Note')
    START_RECORDING_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'START RECORDING')
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Menu')
    MICROPHONE_PERMISSION_MODAL = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="“Scribe Mobile” Would Like to Access the Microphone"]')
    ALLOW_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Allow')
    PAUSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'PAUSE')
    END_VISIT_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'End Visit')
    VISIT_ENDED_CHECK_STATUS_MSG = (AppiumBy.ACCESSIBILITY_ID,'Check status in My Scribes')
    VISIT_ENDED_NOTE_GENERATION_MSG = (AppiumBy.ACCESSIBILITY_ID,'May take a while for transcription and clinical note generation to finish')
    MENU_TITLE = (AppiumBy.XPATH,'//XCUIElementTypeOther[@name="Menu"]')
    MENU_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Login')
    LOGIN_TITLE = (AppiumBy.ACCESSIBILITY_ID,'Log In')
    LOGIN_EMAIL_FIELD = (AppiumBy.XPATH,'//XCUIElementTypeTextField[contains(@name,"Enter work email")]')
    KEYBOARD_DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Done')
    LOGIN_CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Continue')
    LOGIN_PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID,'Enter password')
    FINAL_LOGIN_BUTTON = (AppiumBy.XPATH,'(//XCUIElementTypeStaticText[@name="Log In"])[2]')
    MENU_LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Log Out')
    LOGOUT_CONFIRMATION_MODAL = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[@name="Are you sure you want to log out?"]/parent::*')
    LOGOUT_MODAL_OK_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'OK')
    LOGOUT_MODAL_CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'CANCEL')
    LOGOUT_MODAL_BODY = (AppiumBy.ACCESSIBILITY_ID,'Are you sure you want to log out?')
    SCRIBE_ON_TRIAL_MESSAGE = (AppiumBy.ACCESSIBILITY_ID,"You're on Scribe Trial")
    LANDING_PAGE_SIGN_UP_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Sign Up')
    LANDING_PAGE_LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Log In')
    MY_SCRIBES_BUTTON = (AppiumBy.XPATH,'//XCUIElementTypeImage[@name="My Scribes"]')
    MY_SCRIBES_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeOther[@name="My Scribes"]')
    CREATED_PATIENT_NAME = (AppiumBy.XPATH, f"//XCUIElementTypeStaticText[contains(@name, '{Data().PATIENT_NAME}')]")
