from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_create, name='product_create'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),  
    path('edit/<int:pk>/', views.product_form, name='product_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)