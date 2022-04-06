from django.urls import path, re_path, register_converter
from . import views
from .converters import YearConverter_2000, MonthConverter, DayConverter

app_name = 'instagram' # URL Reverse에서 namespace역할을 하게 됨

register_converter(YearConverter_2000, 'year_2000')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')
 
urlpatterns = [
       path('new/', views.post_new, name='post_new'),
       path('<int:pk>/edit', views.post_edit, name='post_edit'),
       path('<int:pk>/delete', views.post_delete, name='post_delete'),
       path('', views.post_list, name='post_list'),
       path('<int:pk>/', views.post_detail, name='post_detail'),
       #path('archives/<year_2000:year>/', views.archives_year), # re_path(r"archives/(?P<year>20\d{2})/", views.archives_year)
       path('archive/', views.post_archive, name='post_archive'),
       path('archive/<year_2000:year>/', views.post_archive_year, name='post_archive_year'),
]