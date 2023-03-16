from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from accesTravel import settings
from usermanagement import views

urlpatterns = [
    path('login', views.dologin, name='login'),
    path('logout', views.logout, name='logout'),
    path('get_user_details', views.GetUserDetails),
    path('agence_registration', views.agence_registration, name='agence_registration'),
    path('client_registration', views.client_registration, name='client_registration'),
    path('wib_registration', views.wib_registration, name='wib_registration'),
    path('accounts/', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)