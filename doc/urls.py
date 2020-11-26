from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jtod', JsonView.as_view(), name='jtod'),
    path('dtoj', DocView.as_view(), name='dtoj'),
    path('jsonform', JsonView.as_view(), name='jsonform'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
