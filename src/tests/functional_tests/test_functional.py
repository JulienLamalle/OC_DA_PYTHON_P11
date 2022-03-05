from sre_constants import SUCCESS
from src.tests.conftest import competitions, webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def test_interface(webdriver):
  BASE_URL = "http://localhost:5000"
  SUCCESS_REDIRECT_URL = "http://localhost:5000/clubs"
  webdriver.get(BASE_URL)
  email_input = webdriver.find_element(By.NAME, "email")
  email_input.send_keys("admin@irontemple.com")
  email_input.submit()

  WebDriverWait(webdriver, 5).until(
      EC.visibility_of_element_located(
        (By.ID, "welcome"))
  )

  competition = webdriver.find_element(By.ID, "booking_link")
  competition.click()
  time.sleep(2)
  input_to_select_number_of_places_to_book = webdriver.find_element(
    By.ID, "number-book-input")
  input_to_select_number_of_places_to_book.send_keys("1")
  time.sleep(2)
  booking_button = webdriver.find_element(By.ID, "book-submission-btn")
  booking_button.click()

  time.sleep(2)

  link_to_logout = webdriver.find_element(By.ID, "link_to_logout")
  link_to_logout.click()

  WebDriverWait(webdriver, 5).until(
      EC.visibility_of_element_located(
        (By.ID, "home"))
  )

  time.sleep(2)

  link_to_list_of_clubs = webdriver.find_element(
    By.ID, "link_to_list_of_clubs")
  link_to_list_of_clubs.click()
  time.sleep(3)

  assert webdriver.current_url == SUCCESS_REDIRECT_URL
  tearDown(webdriver)


def tearDown(webdriver):
  if webdriver:
    webdriver.close()
    webdriver.quit()
