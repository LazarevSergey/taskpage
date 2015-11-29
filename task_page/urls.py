from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', "task_page.views.task_page", name='task_page'),
)