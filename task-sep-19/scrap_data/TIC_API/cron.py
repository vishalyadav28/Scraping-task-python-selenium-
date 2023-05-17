import json
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from TIC_API.models import  DataStore
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def store_updated_data():
    try:
        # selenium setup
        # settings to keep request unblock
        ua = UserAgent()
        user_agent = ua.random
        options = Options()
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("javascript.enabled")
        options.add_argument("enable-automation")
        options.add_argument("--disable-extensions")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        driver.get('https://transparency-in-coverage.uhc.com/')
        # opening driver headless
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located(
        (By.CLASS_NAME, "ant-list-items")))
        # driver will wait until tag completely loads
        page_data = driver.page_source
        parsed_data = BeautifulSoup(page_data, 'lxml')
        # convert it into more pythonic form using lxml
        soupdata = parsed_data.find_all('a')
        # storing data
        resulting_data = []
        company_name_list = DataStore.objects.values_list('company_name')
        company_name_list = list(map(lambda x:x[0],list(company_name_list)))
        try:
            for data in soupdata:
                temp =  (str(data).split('>'))[1]
                result = ' '.join(((temp[0:len(temp)-3]).split('_'))[1:])
                if result.startswith('-'):
                    result=result[1:]
                if result.endswith('index.json'):
                    result = result[:result.index("index.json")]
                    result=result.strip()
                    if result not in company_name_list:
                        get_url= urllib.request.urlopen(data['href'])
                        temp_report_data=(json.load(get_url))['reporting_structure'][0]
                        each_data = DataStore(
                            company_name=result,
                            report_data=temp_report_data,
                            plan_id=(temp_report_data['reporting_plans'])[0]['plan_id']
                        )
                        print(f"company_name : {result}, plan_id : {(temp_report_data['reporting_plans'])[0]['plan_id']}")
                        resulting_data.append(each_data)
                    else:
                        print("Already exists")
                else:
                    pass
        except:
            pass
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<final>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')   
        DataStore.objects.bulk_create(resulting_data, ignore_conflicts= True)
        driver.close()
    except Exception as e:
        print(str(e))


            
