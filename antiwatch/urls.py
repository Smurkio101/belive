from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('register/', app_views.register, name='register'),
    path ('profile/', app_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='app/pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/pages/logout.html'), name='logout'),
    path('', include("app.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)