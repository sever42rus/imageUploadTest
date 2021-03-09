from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,  include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='hello_page/index.html')),
    path('auth/', include('users.urls')),
    path('image/', include('image.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
