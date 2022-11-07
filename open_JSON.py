import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

import json
from restaurants.models import Restaurant, Tag

file_path = "./gangnam.json"

with open(file_path, 'r') as file:
    data = json.load(file)
print(data['DATA'][0]['upso_nm'])
print(data['DATA'][0]['site_addr'])
print(data['DATA'][0]['upso_site_telno'])
print(data['DATA'][0]['snt_uptae_nm'])
print(data['DATA'][0]['main_edf'])

data = data['DATA']

for i in range(300):
    new_restaurant = Restaurant(
            name = data[i]['upso_nm'],
            address = data[i]['site_addr'],
            shop_number = data[i]['upso_site_telno'] or '음식점에 직접 문의해주세요.',
            between_pay = '음식점에 직접 문의해주세요.',
            opening_time = '음식점에 직접 문의해주세요.',
            break_day = '음식점에 직접 문의해주세요.',)
    new_restaurant.save()
    try: 
        tags = data[i]['main_edf'].split(",")
        for tag in tags:
            if not tag:
                continue
            else:
                tag = tag.strip()
                _tag, _ = Tag.objects.get_or_create(name=tag)
                new_restaurant.tags.add(_tag)

        tag_nm = data[i]['snt_uptae_nm'].strip()
        _tag, _ = Tag.objects.get_or_create(name=tag_nm)
        new_restaurant.tags.add(_tag)
        
    except:
        tag = data[i]['snt_uptae_nm'].strip()
        _tag, _ = Tag.objects.get_or_create(name=tag)
        new_restaurant.tags.add(_tag)