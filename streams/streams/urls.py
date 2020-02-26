from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('streams/', include('viihdeAPI.API_urls')),
    path('', include('viihdeAPI.GUI_urls'))
]
