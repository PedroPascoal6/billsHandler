from django.conf.urls import include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bill import views
from rest_framework.schemas import get_schema_view
from bill.views import ExampleView


schema_view = get_schema_view(title='Bill API')

# Create a router and register our viesets with it
router = DefaultRouter()
router.register('d', views.BillViewSet)
# router.register('user', views.BillsByUser)
# router.register(r'user', views.BillsByUser, basename='bill')
router.register('save', views.BillCreateObject)
router.register('users', views.UserViewSet)
router.register('excel', views.ExportBills)
# router.register('op', views.ExampleView, base_name="op")
# router.register(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view())

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
    path('api-auth/',
         include('rest_framework.urls')),
    path('op/', ExampleView.as_view()),
    path('user/', views.BillsByUser.as_view())
]
