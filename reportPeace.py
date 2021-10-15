from selenium import webdriver
import time
import init


def run():
    result = []
    for user in init.report_peace_users:
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
            driver.find_element_by_xpath("//li[@name='北林师生报平安（学生）']").click()
            windows = driver.window_handles
            driver.switch_to.window(windows[-1])
            time.sleep(10)
            driver.find_element_by_xpath("//button[@id='commit']").click()
            driver.quit()
            result.append((user[0], 1))
        except:
            result.append((user[0], 0))
    return result
