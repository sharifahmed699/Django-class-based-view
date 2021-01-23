from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name='articles'

urlpatterns = [
    path('',views.ArticleListView.as_view(),name="list"), 
    path('detail/<int:pk>/<str:slug>/',views.ArticleDetailView.as_view(),name="detail"),
    path('update/<int:pk>/<str:slug>/',views.ArticleUpdateView.as_view(),name="update"),
    path('delete/<int:pk>/<str:slug>/',views.ArticleDeleteView.as_view(),name="delete"),
    path('create/',views.ArticleCreateView.as_view(),name="create"),
    path('comment/<int:pk>/',views.CommentCreateView.as_view(),name="comment"),
    


    #path('',views.article_list_view,name="list"),
    # path('',TemplateView.as_view(template_name='article/list.html'),name="list"),
    # path('create/',views.ArticleFormView.as_view(),name="create"),
   
]