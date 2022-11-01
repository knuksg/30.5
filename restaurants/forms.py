from django import forms
from .models import restaurants, categorys

class restaurantsForm(forms.ModelForm):

    class Meta:
        model = restaurants
        fields = ['name', 'address', 'shop_number','between_pay','opening_time','break_day']
        labels = {
            'name' : '상호명',
            'address': '주소',
            'shop_number' : '전화번호',
            'between_pay' : '기본 가격대',
            'opening_time' : '영업 시간',
            'break_day' : '휴무일',
        }