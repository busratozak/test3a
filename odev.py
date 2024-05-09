from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

#Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

class test_sauce:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window
        self.driver.get("https://www.saucedemo.com/")

    def test_invalid_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print (f"TEST SONUCU:  {testResult}")

#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

    def test_invalid_login2(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMesage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMesage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU:  {testResult}")

#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

    def test_invalid_login3(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        errorMesage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMesage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU:  {testResult}")
 
#Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")
        testResult = len(products)
        if testResult == 6: 
            print("TEST SONUCU:  True")
        else:
            print("TEST SONUCU:  False")
        

    #Kullanıcı, ürünleri en düşük fiyattan en yükseğe doğru sıralayabilmeli

    def test_sort_products (self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"product_sort_container")))
        sorting = self.driver.find_element(By.CLASS_NAME,"product_sort_container") 
        sorting.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]")))
        sortingList = self.driver.find_element(By.XPATH,"//*[@id=\"header_container\"]/div[2]/div/span/select/option[3]")
        sortingList.click()
        firstTwoProductPrices = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        firstTwoProductPrices = [float(element.text.replace("$", "")) for element in firstTwoProductPrices]

        # En ucuz ürünün listenin başında olduğunu kontrol etme
        if firstTwoProductPrices[0] <= firstTwoProductPrices[1]:
            print("TEST SONUCU:  True")
        else:
            print("TEST SONUCU:  False")
        


testClass = test_sauce()
testClass.test_invalid_login()
testClass.test_invalid_login2()
testClass.test_invalid_login3()
testClass.test_valid_login()
testClass.test_sort_products()
