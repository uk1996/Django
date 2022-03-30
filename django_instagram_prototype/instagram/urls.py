from django.urls import path, re_path, register_converter
from . import views

app_name = 'instagram' # URL Reverse에서 namespace역할을 하게 됨

# 커스텀 Path Converter
class YearConverter_2000:
       regex = "20\d{2}"
       
       def to_python(self, value): # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
              return int(value)
       
       def to_url(self, value): # url reverse 시에 호출
              return str(value)

register_converter(YearConverter_2000, 'year_2000')
 

urlpatterns = [
       path('', views.post_list, name='post_list'),
       path('<int:pk>/', views.post_detail),
       #path('archives/<year_2000:year>/', views.archives_year), # re_path(r"archives/(?P<year>20\d{2})/", views.archives_year)
       path('archive/', views.post_archive, name='post_archive'),
]