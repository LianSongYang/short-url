from django.urls import path
from .views import index, generate_short_url,redirect_to_url

urlpatterns = [
    path('', index, name='index'),  # 這行處理 `/`
    path('shorten/', generate_short_url, name='generate_short_url'),
    path('<str:short_code>/', redirect_to_url, name='redirect_to_url'),
]

