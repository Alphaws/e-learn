from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

from roadmap.views import SubjectListView, BlogPostsBySubjectView
from roadmap.views import LoginView, RegisterView, UserProfileView
from roadmap.views.blog_post_list_view import BlogPostListView
from roadmap.views.blog_post_view import BlogPostRetrieveView
from roadmap.views.subject_retrieve_view import SubjectRetrieveView
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', hello),
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include(router.urls)),
        path('auth/', include([
            path('register/', RegisterView.as_view(), name='register'),
            path('login/', LoginView.as_view(), name='token_obtain_pair'),
            path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
            # @todo: ForgotPassword
            # @todo: ResetPassword
            path('profile/', UserProfileView.as_view(), name='get_user_profile'),
        ])),
        path('blog/', include([
            path('', BlogPostListView.as_view(), name='blog-list'),
            # blog details
            path('<slug:slug>/', BlogPostRetrieveView.as_view(), name='blog-detail'),
            # create blog

            # update blog
            # delete blog
        ])),
        path('subjects/', SubjectListView.as_view(), name='subject-list'),
        path('subject/<slug:slug>/', SubjectRetrieveView.as_view(), name='subject-detail'),
        path('subject/<slug:subject_slug>/blogposts/', BlogPostsBySubjectView.as_view(), name='subject-blogposts'),
        # @todo: Get latest blog posts (limit parameter)
        # @todo: Get blogposts for a subject

    ]))
]
