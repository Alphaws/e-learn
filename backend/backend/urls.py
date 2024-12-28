"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from roadmap.views import SubjectListView, BlogPostsBySubjectView
from rest_framework_simplejwt.views import TokenObtainPairView
from roadmap.views import LoginView, RegisterView, UserProfileView
from roadmap.views.subject_retrieve_view import SubjectRetrieveView
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', hello),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('auth/', include([
            path('register/', RegisterView.as_view(), name='register'),
            path('login/', LoginView.as_view(), name='token_obtain_pair'),
            # path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
            # @todo: ForgotPassword
            # @todo: ResetPassword
            path('profile/', UserProfileView.as_view(), name='get_user_profile'),
        ])),
        path('subjects/', SubjectListView.as_view(), name='subject-list'),
        path('subject/<slug:slug>/', SubjectRetrieveView.as_view(), name='subject-detail'),

        path('subject/<slug:subject_slug>/blogposts/', BlogPostsBySubjectView.as_view(), name='subject-blogposts'),
        # @todo: Get latest blog posts (limit parameter)
        # @todo: Get blogposts for a subject

    ]))
]
