
from . import views
from django.urls import path

from pythtravel import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.demo,name='demo'),
    #path('',views.reva,name='reva'),
    #path('add/',views.add,name='add'),
#     path('contact/',views.contact,name='contact')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
