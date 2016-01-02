from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
now = time.localtime()

driver = webdriver.Firefox()
driver.get('https://play.google.com/store/search?q=&c=apps&docType=1&sp=CAFiEQoP66Gv642w7ZmI7Ie87ZWRegUYAMABAooBAggB:S:ANO1ljJdglM')
driver.set_window_size(3000, 3000)
search_list = ['홈쇼핑','홈쇼핑방송편성표','홈쇼핑앱','cj오쇼핑','cj홈쇼핑','현대홈쇼핑','롯데홈쇼핑','GS홈쇼핑','GSSHOP','GS샵','지에스홈쇼핑','지에스샵','홈앤쇼핑','홈&쇼핑','홈앤쇼핑앱','아임쇼핑','im쇼핑','공영홈쇼핑','드림앤쇼핑']

line = '홈쇼핑 모아 순위 결과\n'
with open("/Users/judelee/Desktop/lucy/list" + str(now.tm_mon) + "월"+ str(now.tm_mday) + "일" + str(now.tm_min) + "분", "w") as f:
    for i in range(len(search_list)):

        element = driver.find_element_by_id('gbqfq')
        element.clear()
        if element.get_attribute('value') == '':
            element.send_keys(search_list[i])
            element.send_keys(Keys.RETURN)
            driver.refresh()

            WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "card-list")))

            title_list = []
            count = 0
            for result in driver.find_elements_by_class_name('card-list'):
                if count != 0:
                    break
                WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "details")))
                count += 1
                for div in result.find_elements_by_class_name('details'):
                    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
                    title_span = div.find_element_by_class_name('title')
                    title_list.append(title_span.get_attribute('title'))

            for j in range(len(title_list)):
                home_str = '홈쇼핑모아-TV홈쇼핑 편성표,생방송,알림,검색을 한눈에'
                if home_str == title_list[j]:
                    print(search_list[i], j+1)
                    line += str(search_list[i]) + " " + str(j+1) + '\n'

    line += '라이브홈쇼핑 순위 결과 \n'
    for i in range(len(search_list)):

        element = driver.find_element_by_id('gbqfq')
        element.clear()
        if element.get_attribute('value') == '':
            element.send_keys(search_list[i])
            element.send_keys(Keys.RETURN)
            driver.refresh()

            WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "card-list")))

            title_list = []
            count = 0
            for result in driver.find_elements_by_class_name('card-list'):
                if count != 0:
                    break
                WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "details")))
                count += 1
                for div in result.find_elements_by_class_name('details'):
                    WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
                    title_span = div.find_element_by_class_name('title')
                    title_list.append(title_span.get_attribute('title'))

            for j in range(len(title_list)):
                home_str = '라이브홈쇼핑-TV홈쇼핑 편성표,생방송알림,검색,추가할인'
                if home_str == title_list[j]:
                    print(search_list[i], j+1)
                    line += str(search_list[i]) + " " + str(j+1) + '\n'
    f.write("%s\n" % line)
driver.close()
