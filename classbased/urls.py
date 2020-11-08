from django.urls import path
app_name = 'classbased'

from .views import FirstView, FirstTemplate, FirstTemplateRedirect
from .crud_views import Create, List

urlpatterns = [
    path('first/', FirstView.as_view()),
    path('template/', FirstTemplate.as_view()),
    path('template1/', FirstTemplateRedirect.as_view()),
    path('template2/', FirstTemplateRedirect.as_view()),
    path('template3/', FirstTemplateRedirect.as_view()),
    path('create/', Create.as_view(), name= 'create'),
    path('list/', List.as_view(), name= 'list')
]