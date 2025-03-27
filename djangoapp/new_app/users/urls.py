from django.urls import path, include
from .views import SignUpView, profile_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='sign_up'),  # URL для регистрации
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile_view, name='profile'),
    # Встроенные URL для входа/выхода
]
