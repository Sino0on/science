from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api_schema', get_schema_view(title='API Schema', description='Guide for drf'), name='api_schema'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('server.urls')),
    path('swagger-ui/', TemplateView.as_view(
      template_name='docs.html',
      extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
