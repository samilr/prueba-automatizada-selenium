from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TheInternetTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Form Authentication").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))

        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        login_button.click()

        success_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success")))
        self.assertIn("You logged into a secure area!", success_message.text)

    def test_add_remove_elements(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='addElement()']")))

        add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
        add_button.click()
        delete_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.added-manually")))

        self.assertTrue(delete_button.is_displayed())
        delete_button.click()
        self.assertFalse(driver.find_elements(By.CSS_SELECTOR, "button.added-manually"))

    def test_checkboxes(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
            self.assertTrue(checkbox.is_selected())

    def test_dropdown(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Dropdown").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "dropdown")))

        dropdown = driver.find_element(By.ID, "dropdown")
        dropdown.click()
        option = driver.find_element(By.CSS_SELECTOR, "option[value='1']")
        option.click()

        selected_option = dropdown.find_element(By.CSS_SELECTOR, "option:checked")
        self.assertEqual(selected_option.text, "Option 1")

    def test_dynamic_controls(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Dynamic Controls").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")))

        checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
        checkbox_button.click()

        self.wait.until(EC.invisibility_of_element(checkbox))
        self.assertFalse(driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']"))

        add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
        add_button.click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))

        self.assertTrue(driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").is_displayed())

    def test_dynamic_loading(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Dynamic Loading").click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Example 1: Element on page that is hidden")))

        driver.find_element(By.LINK_TEXT, "Example 1: Element on page that is hidden").click()
        start_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
        start_button.click()

        hello_world = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4")))
        self.assertEqual(hello_world.text, "Hello World!")

    def test_forgot_password(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Forgot Password").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "email")))

        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("test@example.com")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        success_message = self.wait.until(EC.presence_of_element_located((By.ID, "content")))
        self.assertIn("Your e-mail's been sent!", success_message.text)

    def test_hovers(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Hovers").click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "figure")))

        figures = driver.find_elements(By.CLASS_NAME, "figure")
        for figure in figures:
            webdriver.ActionChains(driver).move_to_element(figure).perform()
            self.assertTrue(figure.find_element(By.CLASS_NAME, "figcaption").is_displayed())

    def test_js_alerts(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsAlert()']")))

        alert_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
        alert_button.click()

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "I am a JS Alert")
        alert.accept()

    def test_js_confirm(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsConfirm()']")))

        confirm_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
        confirm_button.click()

        confirm = driver.switch_to.alert
        self.assertEqual(confirm.text, "I am a JS Confirm")
        confirm.accept()

    def test_js_prompt(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[onclick='jsPrompt()']")))

        prompt_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
        prompt_button.click()

        prompt = driver.switch_to.alert
        self.assertEqual(prompt.text, "I am a JS prompt")
        prompt.send_keys("Hello!")
        prompt.accept()

        result = driver.find_element(By.ID, "result")
        self.assertIn("You entered: Hello!", result.text)

    def test_ab_testing(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "A/B Testing").click()
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))

        heading = driver.find_element(By.TAG_NAME, "h3")
        self.assertEqual(heading.text, "A/B Test Control")

    def test_basic_auth(self):
        driver = self.driver
        auth_url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
        driver.get(auth_url)
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "p")))

        paragraph = driver.find_element(By.TAG_NAME, "p")
        self.assertIn("Congratulations", paragraph.text)

    def test_broken_images(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "Broken Images").click()
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))

        images = driver.find_elements(By.TAG_NAME, "img")
        broken_images = [img for img in images if img.get_attribute('naturalWidth') == '0']
        self.assertGreater(len(broken_images), 0, "No broken images found")

if __name__ == "__main__":
    unittest.main()
