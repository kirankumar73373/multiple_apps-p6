from django.urls import path
from app1.views import*
app_name='something1'

urlpatterns=[
    path('keerthi/',keerthi,name='keerthi'),
    path('satya/',satya,name='satya'),
]