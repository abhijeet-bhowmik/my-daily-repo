from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_views()),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_views()),
]