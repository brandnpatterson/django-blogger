from django.conf.urls import url
from django.contrib import admin
from posts.views import posts_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', posts_view)
]
