from django.conf.urls import url 
from microservicio import views 
 
urlpatterns = [ 
    url(r'api/search_route/(?P<route_name>(.*))', views.search_route),
    url(r'api/search_stop/(?P<stop_name>(.*))', views.search_stop),
    url('api/search_all', views.search_all),
]
