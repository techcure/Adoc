from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *
from django.views import View


urlpatterns = [
   
       path('', IndexView.as_view(), name='index'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)