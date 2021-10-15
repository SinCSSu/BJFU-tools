from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import init


def run():
    result = []
    for user in init.school_exit_application_users:
        try:
            option = webdriver.ChromeOptions()
            option.add_argument("--headless")
            option.add_argument("--disable-gpu")
            driver = webdriver.Chrome(executable_path=init.drive_path, options=option)
            driver.get('http://cas.bjfu.edu.cn/cas/login')
            driver.find_element_by_id('un').send_keys(user[0])
            driver.find_element_by_id('pd').send_keys(user[1])
            driver.find_element_by_id('index_login_btn').click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//li[@name='学生出校申请']").click()
            windows = driver.window_handles
            driver.switch_to.window(windows[-1])
            locator = (By.XPATH, "//a[text()='确定']")
            WebDriverWait(driver, 4).until(EC.presence_of_element_located(locator))
            driver.find_element_by_xpath("//a[text()='确定']").click()
            driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="formIframe"]'))
            driver.find_element_by_xpath("//input[@id='QTSY']").send_keys("吃饭")
            driver.find_element_by_xpath("//button[@data-id='CXLB']").click()
            driver.find_element_by_xpath(
                "//button[@data-id='CXLB']/..//ul[@class='dropdown-menu inner selectpicker']/li[@rel='1']").find_element_by_tag_name(
                'span').click()
            driver.find_element_by_xpath("//button[@data-id='CXSY']").click()
            driver.find_element_by_xpath(
                "//button[@data-id='CXSY']/..//ul[@class='dropdown-menu inner selectpicker']/li[@rel='3']").find_element_by_tag_name(
                'span').click()
            driver.find_element_by_xpath("//button[@data-id='SZSF']").click()
            driver.find_element_by_xpath(
                "//button[@data-id='SZSF']/..//ul[@class='dropdown-menu inner selectpicker']/li[@rel='1']").find_element_by_tag_name(
                'span').click()
            driver.find_element_by_xpath("//button[@data-id='SZSQ']").click()
            driver.find_element_by_xpath(
                "//button[@data-id='SZSQ']/..//ul[@class='dropdown-menu inner selectpicker']/li[@rel='1']").find_element_by_tag_name(
                'span').click()
            driver.find_element_by_xpath("//button[@data-id='SZX']").click()
            driver.find_element_by_xpath(
                "//button[@data-id='SZX']/..//ul[@class='dropdown-menu inner selectpicker']/li[@rel='6']").find_element_by_tag_name(
                'span').click()
            now = datetime.datetime.now()
            tm = now.strftime("%Y-%m-%d %H:%M")
            js = 'document.getElementById("JHCXSJ").removeAttribute("readOnly");'
            driver.execute_script(js)
            driver.find_element_by_xpath("//input[@id='JHCXSJ']").send_keys(tm)
            tm = list(tm)
            tm[11] = '2'
            tm[12] = '3'
            tm[14] = '5'
            tm[15] = '9'
            tm = ''.join(tm)
            js = 'document.getElementById("JHFXSJ").removeAttribute("readOnly");'
            driver.execute_script(js)
            driver.find_element_by_xpath("//input[@id='JHFXSJ']").send_keys(tm)
            driver.find_element_by_xpath("//div[@id='CXCN_vant']//i").click()
            driver.switch_to.default_content()
            driver.find_element_by_xpath("//button[@id='commit']").click()
            driver.quit()
            result.append((user[0], 1))
        except:
            result.append((user[0], 0))
    return result
