from django.conf.urls import url

from .views import Index


urlpatterns = [
    url(r'^test1$', Index.as_view(), name='test1'),
    url(r'^test2$', Index.as_view(), name='test2')
]