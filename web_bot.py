from secrets import *
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains


class WebBot():
    def __init__(self):
        # self.browser = webdriver.Chrome()# start the browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-agent={}'.format(useragent))
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--window-size=1920,1080")

        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        # self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(chrome_options=chrome_options,
                                        desired_capabilities=capabilities,)
                                        # executable_path=r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome')
        self.browser.get('https://cart.lazada.sg/cart')
        sleep(10)

    def login(self):

        default_login_btn = self.browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/form/div/div[2]/div[1]/button')
        default_login_btn.click()
        # # attempted to go beyond slider-captcha but no target is available
        # source = self.browser.find_element_by_xpath('//*[@id="nc_28_n1z"]')
        # action_chains = ActionChains(self.browser)
        # drag the verify button - not working currently
        # action_chains.drag_and_drop(source, target).perform()
        # Conclusion: Lazada login is able to detect that seleniun is a bot?

        # Google Login
        google_login = self.browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/form/div/div[2]/div[2]/div/div[2]/button[2]')
        google_login.click()
        sleep(3)

        # switch to login popup is not needed in lazada
        base_window = self.browser.window_handles[0]
        self.browser.switch_to_window(self.browser.window_handles[1])


        self.browser.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        # self.browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username)
        self.browser.find_element_by_xpath('//*[@id="identifierNext"]').click()
        # self.browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        sleep(3)
        # self.browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        self.browser.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="passwordNext"]').click()
        # self.browser.find_element_by_xpath('//*[@id="passwordNext"]/span').click()
        sleep(3)
        print("[1/N] Google Login completed")

        # switch back to base window - may not be needed
        self.browser.switch_to_window(base_window)

    def select_all_from_cart(self):
        sleep(2)
        select_all_btn = self.browser.find_element_by_xpath('//*[@id="listHeader_H"]/div/div/div[1]/label/input')
        select_all_btn.click()
        print("[2/N] select all from cart")

    def start_select_slot(self):
        # click proceed to checkout
        sleep(2)
        proceed_checkout_btn = self.browser.find_element_by_xpath('//*[@id="rightContainer_CR"]/div[2]/div[2]/div/div[3]/button')
        proceed_checkout_btn.click()

        # remove select slot popup
        sleep(2)
        got_it_btn = self.browser.find_element_by_xpath('//*[@id="dialog-body-1"]/button')
        got_it_btn.click()

        # click on select slot button
        select_slots_btn = self.browser.find_element_by_xpath('//div[@class="deliveryTimeRight"]')
        select_slots_btn.click()

        # identify a valid slot
        slots = self.browser.find_elements_by_css_selector("div[class*=slot-item-container]:not([class*='disabled'])")
        if len(slots):
            slots[0].click()
            print("[3/N] selected slot for delivery")
            return True
        else:
            print("[3/N] no slot available")
            return False

    def place_order_now(self):
        sleep(2)
        select_all_btn = self.browser.find_element_by_css_selector('button[class*=checkout-order-total-button]')
        select_all_btn.click()
        print("[4/N] proceed to checkout")

lazada_bot = WebBot()

lazada_bot.login()
lazada_bot.select_all_from_cart()
slots = lazada_bot.start_select_slot()
if slots:
    lazada_bot.place_order_now()
else:
    print("No slots available!")

print(" !! Program Running Successfully !! ")
