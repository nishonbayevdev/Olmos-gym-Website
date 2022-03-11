from django.urls import path
from .views import \
   classDeteals\
   ,home\
   ,aboutUs\
   ,classTimetable\
   ,gallery\
   ,blog\
   ,notFound\
   ,contact\
   ,index\
   ,services\
   ,team\
   ,main\
   ,blogDetails\
   ,contactSend
urlpatterns = [
   path('',home,name='home'),
   path('classdetail/',classDeteals,name='classdetail'),
   path('about/',aboutUs,name='about'),
   path('classTimetable/',classTimetable,name='classTimetable'),
   path('team/',team,name='team'),
   path('gallery/',gallery,name='gallery'),
   path('blog/',blog,name='blog'),
   path('notFound/',notFound,name='notFound'),
   path('contact/',contact,name='contact'),
   path('index/',index,name='index'),
   path('services/',services,name='services'),
   path('main/',main,name='main'),
   path('blogDetails/',blogDetails,name='blogDetails'),
   path('contact/send/',contactSend,name='send')
]