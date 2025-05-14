from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('index.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)