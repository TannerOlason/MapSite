from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('',views.home_page, name="home"),
    path('admin/', admin.site.urls),
    path('world/', include('world.urls')),
    path('about',views.about_page, name="about"),
    path('portfolio',views.portfolio_page, name="portfolio"),
    path('blog',views.blog_page, name="blog"),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
