from django.conf.urls import url

from teams.views import teams_list, teams_create, teams_update, teams_delete

urlpatterns = [
    url(r'^$', teams_list),
    url(r'^new$', teams_create),
    url(r'^edit/(?P<pk>\d+)$', teams_update),
    url(r'^delete/(?P<pk>\d+)$', teams_delete),
]
