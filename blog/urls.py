from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexPage.as_view(), name='index'),
    re_path(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    re_path(r'^article/all/$', views.AllArticleAPIView.as_view(), name='all_articles'),
    re_path(r'^article/$', views.SingleArticleAPIView.as_view(), name='single_article'),
    re_path(r'^article/getByPredicate/$', views.GetArticleByPredicateView.as_view(), name='predicate_article'),
    re_path(r'^article/create/$', views.CreateArticleView.as_view(), name='create_article'),
    re_path(r'^article/edit/$', views.EditeArticleView.as_view(), name='edit_article'),
    re_path(r'^article/delete/$', views.DeleteArticleView.as_view(), name='delete_article'),
]