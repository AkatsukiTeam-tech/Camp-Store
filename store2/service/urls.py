from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from service.views import example_view, ServiceModel, ServiceModelView,signup
urlpatterns = [
    path('', example_view,name='home'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<slug:slug>/', ServiceModel.as_view(), name='service_category'),
    path('<slug:category>/<slug:slug>/', ServiceModelView.as_view(), name = 'service_model_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
