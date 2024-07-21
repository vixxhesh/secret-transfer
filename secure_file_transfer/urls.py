from django.contrib import admin
from django.urls import path, include
from transfer import views as transfer_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transfer.urls')),
    path('send/', transfer_views.send_file, name='send_file'),
    path('receive/', transfer_views.receive_file, name='receive_file'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)