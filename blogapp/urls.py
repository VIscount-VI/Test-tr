from django.urls import path
from .views import createlist, Save, Index, Index_2

urlpatterns = [
    path('list/', createlist.as_view(), name='list'),
    path('save/', Save, name='save'),
    path('', Index, name='index'),
    path('o2/', Index_2, name='index_2'),
]