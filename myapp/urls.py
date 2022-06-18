from django.contrib import admin
from django.urls import include, path
from ponv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ponv/", include("ponv.urls")),
    path('', views.predict_model, name='predict_model'),
]
