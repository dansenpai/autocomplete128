from django.conf.urls import url
from .views import PlayersList, PlayerCreate, PlayerUpdate, \
  PlayerDetail, PlayerDelete, AutoComplete

urlpatterns = [
  url(r'^$', PlayersList.as_view(), name='players_list' ),
  url(r'^player/new/$', PlayerCreate.as_view(), name='player_create'),
  url(r'^player/(?P<pk>[0-9]+)/$', PlayerUpdate.as_view(), name='player_update'),
  url(r'^player/(?P<pk>[0-9]+)/detail$', PlayerDetail.as_view(), name='player_detail'),
  url(r'^player/(?P<pk>[0-9]+)/delete/$', PlayerDelete.as_view(), name='player_delete'),
  url(r'^autocomplete/$', AutoComplete.as_view(), name='autocomplete'),
]