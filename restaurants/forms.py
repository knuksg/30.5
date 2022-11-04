from django import forms
from .models import Restaurant

class RestaurantsForm(forms.ModelForm):
    tags = forms.CharField(required = False, label = "태그")

    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'shop_number','between_pay','opening_time','break_day', 'tags']
        labels = {
            'name' : '상호명',
            'address': '주소',
            'shop_number' : '전화번호',
            'between_pay' : '기본 가격대',
            'opening_time' : '영업 시간',
            'break_day' : '휴무일',
        }