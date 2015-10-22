from django.conf.urls import patterns, include, url

urlpatterns = patterns('base.views',
    url(r'^$', 'index_view', {'templateName': '/base/index.html'}),
)