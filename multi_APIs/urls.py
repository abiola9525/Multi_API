from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from country_details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('', include('country_details.urls')),
    path('', include('blog_api.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)