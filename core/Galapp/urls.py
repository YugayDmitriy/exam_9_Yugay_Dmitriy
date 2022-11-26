from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
    path('', views.home, name="index"),
    path('home', views.home, name='home-page'),
    path('upload_modal', views.upload_modal, name='upload-modal'),
    path('save_upload', views.save_upload, name='save-upload'),
    path('gallery', views.view_gallery, name='gallery-page'),
    path('trash', views.view_trash, name='trash-page'),
    path('trash_image/<int:pk>', views.trash_upload, name='trash-upload'),
    path('restore_image/<int:pk>', views.restore_upload, name='restore-upload'),
    path('delete_image/<int:pk>', views.delete_upload, name='delete-upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
