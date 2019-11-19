from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('projects/', include("projects.urls")),
    path('blog/', include("blog.urls")),
    path('tinymce', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
]
