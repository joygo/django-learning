# myapp/tasks.py

from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
from bs4 import BeautifulSoup 
from mysite import models
import schedule
import time


def weather_check(self, *args, **kwargs):

    url = 'https://weather.com/zh-TW/weather/hourbyhour/l/Dongrong+Taipei?canonicalCityId=d7a30822715ad1b2572c83dce89530df3e4fae10abff541b08d7c5f36764ec3f'  # 將此 URL 替換為你要爬取的網頁 URL

    # 發送 GET 請求以獲取網頁內容
    response = requests.get(url)

    # 檢查是否成功獲取響應
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析網頁內容
        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 要查找的 CSS class 名稱
        target_class = 'tempB'  # 將此替換為你要查找的 CSS class
        
        # 使用 BeautifulSoup 的 find_all 方法查找所有具有特定 class 的元素
        div_with_id = soup.find('details', id='detailIndex0')
        
        # 遍歷找到的元素，並提取其文本內容
        if div_with_id:
            feels_like_element = soup.find('span', {'data-testid': 'TemperatureValue'})
            # 提取體感溫度文本
            if feels_like_element:
                feels_like = feels_like_element.text
                datas = models.WeatherMonitor.objects.all()
                for data in datas:
                    if data.temp_range < int(feels_like):
                        with open('/home/joygo/w_log.txt', 'a') as f:
                            f.write('temp is {} over {}'.format(feels_like, data.temp_range))
                            
                        
                
                print("體感溫度:", feels_like)
            else:
                print("找不到體感溫度")
    else:
        print('無法獲取網頁內容')
        

# 创建定时任务
schedule.every(1).minutes.do(weather_check)

# 运行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)

