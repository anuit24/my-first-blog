from django.conf.urls import url
from .views import adddata

urlpatterns = [
    url(r'^adddata',adddata),
    
    
]
