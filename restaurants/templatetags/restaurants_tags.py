from django import template
register = template.Library()

@register.filter
def latest_content(queryset):
    review = queryset.review_set.order_by('-pk')[0].content
    return review

@register.filter
def latest_image(queryset):
    if queryset.review_set.order_by('-pk')[0].user.image:
        review = queryset.review_set.order_by('-pk')[0].user.image.url
        return review
    else:
        return 'https://postfiles.pstatic.net/MjAyMDExMDFfMTA1/MDAxNjA0MjI4ODc1Mzk0.05ODadJdsa3Std55y7vd2Vm8kxU1qScjh5-3eVJ9T-4g.h7lHansSdReVq7IggiFAc44t2W_ZPTPoZWihfRMB_TYg.JPEG.gambasg/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EA%B8%B0%EB%B3%B8%ED%94%84%EB%A1%9C%ED%95%84_%ED%8C%8C%EB%9E%91.jpg?type=w773'

@register.filter
def latest_user(queryset):
    review = queryset.review_set.order_by('-pk')[0].user
    return review