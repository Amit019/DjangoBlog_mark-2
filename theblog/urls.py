
from django.urls import path,include
# from . import views
from .views import IndexView,ArticleDetailView, AddPostView, UpdatedPostView, DeletePostView,AddCategoryView,CategoryView,LikeView,AddCommentView

urlpatterns = [
    path('', IndexView.as_view(),name='index'),
    path('article/<int:pk>', ArticleDetailView.as_view(),name='article'),
    # path('', views.index,name='index'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('add_category/', AddCategoryView.as_view(),name='add_category'),
    path('article/edit/<int:pk>', UpdatedPostView.as_view(),name='edit_post'),
    path('article/remove/<int:pk>', DeletePostView.as_view(),name='delete_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment'),
    path('category/<str:cate>/', CategoryView,name='category'),
    path('like/<int:pk>/', LikeView,name='like_post'),
]