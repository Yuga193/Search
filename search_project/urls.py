# search_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', product_views.product_list, name='home'),  # ルートURLを設定
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)