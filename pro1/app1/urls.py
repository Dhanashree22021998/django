from django.urls import path
from .views import *

urlpatterns = [
    path('a1/', addview),
    path('s1/',showview),
    path('u1/<int:pk>/',updateview,name='update'),
    path('d1/,<int:pk>/',deleteview,name='delete')
]