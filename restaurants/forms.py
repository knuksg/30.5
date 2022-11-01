from django import forms
from .models import Restaurant, Category

class RestaurantsForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'shop_number','between_pay','opening_time','break_day']
        labels = {
            'name' : '상호명',
            'address': '주소',
            'shop_number' : '전화번호',
            'between_pay' : '기본 가격대',
            'opening_time' : '영업 시간',
            'break_day' : '휴무일',
        }

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['tag1','tag2','tag3','tag4','tag5']
        labels = {
            'tag1': '태그',
            'tag2': '태그',
            'tag3': '태그',
            'tag4': '태그',
            'tag5': '태그',
        }