from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from payme.views import MerchantAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


class PaymeCallBackAPIView(MerchantAPIView):
    def create_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"create_transaction for order_id: {order_id}, response: {action}")

    def perform_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"perform_transaction for order_id: {order_id}, response: {action}")

    def cancel_transaction(self, order_id, action, *args, **kwargs) -> None:
        print(f"cancel_transaction for order_id: {order_id}, response: {action}")


schema_view = get_schema_view(
    openapi.Info(
        title="Sultan Travel",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

admin.site.index_title = "Sultan Travel"
admin.site.site_header = "Sultan Travel"
admin.site.site_title = 'Sultan Travel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('news/', include('main.urls')),
    path('duolar/', include('duolar.urls')),
    path('handbook/', include('handbook.urls')),
    path('place/', include('place.urls')),
    path('preparation/', include('preperation.urls')),
    path('accounts/', include('accounts.urls')),
    path('order/', include('orders.urls')),
    path("payments/merchant/", PaymeCallBackAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
