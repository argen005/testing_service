from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="KG Friend API",
        default_version='v1',
        description="KG Friend",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="argen.kubatbekov@gmail.com"),
        license=openapi.License(name="BSD License"),
        dochost="http://127.0.0.1:8000",
        schemes=['http', 'https'],
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),\
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('auth/', include('users.urls')),
]