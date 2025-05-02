from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

schema_view = get_schema_view(
    openapi.Info(
        title="BizFlow API",
        default_version='v1',
        description="BizFlow API",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('account/', include('account.urls')),
    path('', include('index.urls')),
    path('product/', include('product.urls')),
    path('product_api/', include('product_api.urls')),
]
