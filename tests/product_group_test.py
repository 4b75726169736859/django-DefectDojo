import sys
import unittest

from base_test_class import BaseTestCase
from group_test import GroupTest
from product_test import ProductTest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait


class ProductGroupTest(BaseTestCase):

    def test_group_add_product_group(self):
        driver = self.navigate_to_group_view()
        # Open the menu to add product groups and click the 'Add' button
        driver.find_element(By.ID, "dropdownMenuAddProductGroup").click()
        driver.find_element(By.ID, "addProductGroup").click()
        # Select the product 'Research and Development'
        try:
            WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "id_products")))
        except TimeoutException:
            self.fail("Timed out waiting for products dropdown to initialize ")
        driver.execute_script("document.getElementsByName('products')[0].style.display = 'inline'")
        element = driver.find_element(By.XPATH, "//select[@name='products']")
        product_option = element.find_elements(By.TAG_NAME, "option")[0]
        Select(element).select_by_value(product_option.get_attribute("value"))
        # Select the role 'Reader'
        Select(driver.find_element(By.ID, "id_role")).select_by_visible_text("Reader")
        # "Click" the submit button to complete the transaction
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text="Product groups added successfully."))
        # Query the site to determine if the member has been added
        self.assertEqual(driver.find_elements(By.NAME, "member_product")[0].text, "QA Test")
        self.assertEqual(driver.find_elements(By.NAME, "member_product_role")[0].text, "Reader")

    def test_group_edit_product_group(self):
        driver = self.navigate_to_group_view()
        # Open the menu to manage members and click the 'Edit' button
        driver.find_elements(By.NAME, "dropdownManageProductGroup")[0].click()
        driver.find_elements(By.NAME, "editProductGroup")[0].click()
        # Select the role 'Owner'
        Select(driver.find_element(By.ID, "id_role")).select_by_visible_text("Owner")
        # "Click" the submit button to complete the transaction
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text="Product group updated successfully."))
        # Query the site to determine if the member has been edited
        self.assertEqual(driver.find_elements(By.NAME, "member_product")[0].text, "QA Test")
        self.assertEqual(driver.find_elements(By.NAME, "member_product_role")[0].text, "Owner")

    def test_group_delete_product_group(self):
        driver = self.navigate_to_group_view()
        # Open the menu to manage members and click the 'Delete' button
        driver.find_elements(By.NAME, "dropdownManageProductGroup")[0].click()
        driver.find_elements(By.NAME, "deleteProductGroup")[0].click()
        # "Click" the submit button to complete the transaction
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-danger").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text="Product group deleted successfully."))
        # Query the site to determine if the member has been deleted
        self.assertFalse(driver.find_elements(By.NAME, "member_product"))

    def test_product_add_product_group(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to the product page
        self.goto_product_overview(driver)
        # Select and click on the particular product to view
        driver.find_element(By.LINK_TEXT, "QA Test").click()
        # Open the menu to add groups and click the 'Add' button
        driver.find_element(By.ID, "dropdownMenuAddProductGroup").click()
        driver.find_element(By.ID, "addProductGroup").click()
        # Select the group 'Group Name'
        try:
            WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "id_groups")))
        except TimeoutException:
            self.fail("Timed out waiting for groups dropdown to initialize ")
        driver.execute_script("document.getElementsByName('groups')[0].style.display = 'inline'")
        element = driver.find_element(By.XPATH, "//select[@name='groups']")
        group_option = element.find_elements(By.TAG_NAME, "option")[0]
        Select(element).select_by_value(group_option.get_attribute("value"))
        # Select the role 'Reader'
        Select(driver.find_element(By.ID, "id_role")).select_by_visible_text("Reader")
        # "Click" the submit button to complete the transaction
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text="Product groups added successfully."))
        # Query the site to determine if the member has been added
        self.assertEqual(driver.find_elements(By.NAME, "group_name")[0].text, "Group Name")
        self.assertEqual(driver.find_elements(By.NAME, "group_role")[0].text, "Reader")

    def test_product_edit_product_group(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to the product page
        self.goto_product_overview(driver)
        # Select and click on the particular product to view
        driver.find_element(By.LINK_TEXT, "QA Test").click()
        # Open the menu to manage members and click the 'Edit' button
        # The first group is the group we are looking for
        driver.find_elements(By.NAME, "dropdownManageProductGroup")[0].click()
        driver.find_elements(By.NAME, "editProductGroup")[0].click()
        # Select the role 'Maintainer'
        Select(driver.find_element(By.ID, "id_role")).select_by_visible_text("Maintainer")
        # "Click" the submit button to complete the transaction
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text="Product group updated successfully."))
        # Query the site to determine if the member has been edited
        self.assertEqual(driver.find_elements(By.NAME, "group_name")[0].text, "Group Name")
        self.assertEqual(driver.find_elements(By.NAME, "group_role")[0].text, "Maintainer")

    def test_product_delete_product_group(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to the product page
        self.goto_product_overview(driver)
        # Select and click on the particular product to view
        driver.find_element(By.LINK_TEXT, "QA Test").click()
        # Open the menu to manage members and click the 'Delete' button
        # The first group is the group we are looking for
        driver.find_elements(By.NAME, "dropdownManageProductGroup")[0].click()
        driver.find_elements(By.NAME, "deleteProductGroup")[0].click()
        # "Click" the submit button to complete the transaction
        driver.find_element(By.CSS_SELECTOR, "input.btn.btn-danger").click()
        # Assert the message to determine success status
        self.assertTrue(self.is_success_message_present(text="Product group deleted successfully."))
        # Query the site to determine if the member has been deleted
        self.assertFalse(driver.find_elements(By.NAME, "group_name"))

    def navigate_to_group_view(self):
        # Login to the site. Password will have to be modified
        # to match an admin password in your own container
        driver = self.driver
        # Navigate to group management page
        driver.get(self.base_url + "group")
        # Select the previously created group to edit
        # The name is not clickable
        # so we would have to select specific group by filtering list of groups
        driver.find_element(By.ID, "show-filters").click()
        # Insert name to filter by into name box
        driver.find_element(By.ID, "id_name").clear()
        driver.find_element(By.ID, "id_name").send_keys("Group Name")
        # click on 'apply filter' button
        driver.find_element(By.ID, "apply").click()
        # only the needed group is now available, proceed with opening the context menu and clicking 'Edit' button
        driver.find_element(By.ID, "dropdownMenuGroup").click()
        driver.find_element(By.ID, "viewGroup").click()

        return driver


def suite():
    suite = unittest.TestSuite()
    # Add each test the the suite to be run
    # success and failure is output by the test
    suite.addTest(BaseTestCase("test_login"))
    suite.addTest(GroupTest("test_create_group"))
    suite.addTest(ProductTest("test_create_product"))
    suite.addTest(ProductGroupTest("test_group_add_product_group"))
    suite.addTest(ProductGroupTest("test_group_edit_product_group"))
    suite.addTest(ProductGroupTest("test_group_delete_product_group"))
    suite.addTest(ProductGroupTest("test_product_add_product_group"))
    suite.addTest(ProductGroupTest("test_product_edit_product_group"))
    suite.addTest(ProductGroupTest("test_product_delete_product_group"))
    suite.addTest(GroupTest("test_group_edit_name_and_global_role"))
    suite.addTest(GroupTest("test_group_delete"))
    suite.addTest(ProductTest("test_delete_product"))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(descriptions=True, failfast=True, verbosity=2)
    ret = not runner.run(suite()).wasSuccessful()
    BaseTestCase.tearDownDriver()
    sys.exit(ret)
