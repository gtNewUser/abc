import os
import time
import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class UIautoTest(unittest.TestCase):
    def get_config(self):
        config = configparser.ConfigParser()
        #config.read(os.path.join(os.environ['PATH'],'myselenium.ini'))#找ini文件
        config.read('./myselenium.ini')
        return config

    def setUp(self):
        config = self.get_config()
        #是否无界面运行
        try:
            us_head = os.environ['us_head']
        except:
            us_head = None
            print('没有配置环境变量,按有界面方式运行')
        chrome_optios = Options()
        if us_head is not None and us_head.lower() == 'true':
            print('无界面运行')
            chrome_optios.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=config.get('drivers','chrome_drivers'),options=chrome_optios)

    def tearDown(self):
        self.driver.quit()

    def use_baidu(self,search_keyword,testcase_name):
        self.driver.get('https://www.baidu.com')
        print('打开百度网页')
        time.sleep(2)
        assert f'百度一下' in self.driver.title

        ele = self.driver.find_element_by_name('wd')
        ele.send_keys(f'{search_keyword}{Keys.RETURN}')
        print(f'输入关键词是：{search_keyword}')
        time.sleep(2)
        self.assertTrue(f'{search_keyword}' in self.driver.title)

    def test_myUI1(self):
        self.use_baidu('python','test_myUI1')

    def test_myUI2(self):
        self.use_baidu('selenium','test_myUI2')

