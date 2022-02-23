from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('power-chart/', views.power_chart, name='power-chart'),
	path('json-example/', views.json_example, name='json_example'),
    path('json-example/data/', views.chart_data, name='chart_data'),
]
