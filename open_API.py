import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

import json
import urllib.request
from restaurants.models import Restaurant, Tag

url = 'https://www.daegufood.go.kr/kor/api/tasty.html?mode=json&addr=%EC%A4%91%EA%B5%AC'

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
response_body = response.read()
content_dict = json.loads(response_body.decode('utf-8'))
data = content_dict['data']
# print(data[0]['BZ_NM'])
# print(data[0]['GNG_CS'])
# print(data[0]['TLNO'])
# print(data[0]['MNU'])
# print(data[0]['MBZ_HR'])
# print(data[0]['FD_CS'])
# print(data[0]['SMPL_DESC'])

for i in range(101):
    pay = data[i]['MNU'].replace(',', '')
    pay_str = ''
    for j in range(len(pay)):
        if pay[j].isdigit() and pay[j+1].isdigit() and pay[j+2].isdigit() and pay[j+3].isdigit():
            while pay[j] != '원':
                pay_str += pay[j]
                j += 1
            break
    try:
        pay = int(pay_str)

        if pay < 10000:
            pay = '만 원 이하'
        elif pay < 20000:
            pay = '1만 원대'
        elif pay < 30000:
            pay = '2만 원대'
        else:
            pay = '3만 원대 이상'
    except:
        pay = '음식점에 직접 문의해주세요.'

    new_restaurant = Restaurant(
        name = data[i]['BZ_NM'],
        address = data[i]['GNG_CS'],
        shop_number = data[i]['TLNO'],
        between_pay = pay,
        opening_time = data[i]['MBZ_HR'],
        break_day = '음식점에 직접 문의해주세요.',
        subtext = data[i]['SMPL_DESC'])
    new_restaurant.save()
    tags = data[i]['FD_CS'].split("/")
    for tag in tags:
        if not tag:
            continue
        else:
            tag = tag.strip()
            _tag, _ = Tag.objects.get_or_create(name=tag)
            new_restaurant.tags.add(_tag)