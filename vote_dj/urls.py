from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("vote.urls")),
    path("locations/", include("maps.urls")),
    path("messageboard/", include("messageboard.urls")),
    path("adopt/", include("adopt.urls")),
    path("volunteer/", include("volunteer.urls")),
    path("accounts/", include("allauth.urls")),
]
