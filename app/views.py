from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, DetailView
from django.views.generic.edit import DeleteView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Player
from .forms import FormPlayer
from django.db.models import Q
import json
import random

class PlayersList(View):
  players = []
  template_name = 'app/players_list.html'

  def get(self, request, *args,**kwargs):
    query = Q()
    if request.GET.get('term', False):
        query = Q(name__icontains=request.GET['term'])
    players = Player.objects.filter(query)
    paginator = Paginator(players, 100)
    page = int(request.GET.get('page', 1))

    try:
        self.players = paginator.page(page)
    except (EmptyPage, InvalidPage):
        self.players = paginator.page(paginator.num_pages)
    
    response = {
      'players': self.players,
      'actual': page, 'total': paginator.num_pages,
      'next': page + 1, 'prev': page - 1,
      'list_pages': range(1, paginator.num_pages + 1),
      'st': request.GET.get('st', '0')
      }

    return render(request, self.template_name, response)

class PlayerCreate(View):
  form_class = FormPlayer
  template_name = 'app/player_form.html'

  def get(self, request, *args, **kwargs):
      initial = {}
      try:
          r = requests.get('http://api.randomuser.me/')
          data = json.loads(r.text)
          data = data['results'][0]
          initial = {
              'name': "%s %s" % (
                  data['name']['first'], data['name']['last']), 
               'rank_position': random.randrange(0, 2000)}
      except Exception as e:
          print(e)
      form = self.form_class(initial=initial)
      return render(
          request, self.template_name,
          {'form': form, 'name_form': 'Novo Player'})

  def post(self, request, *args, **kwargs):
      form = self.form_class(request.POST)
      if form.is_valid():
          data = form.cleaned_data
          player = Player(name=data['name'], rank_position=data['rank_position'])
          player.save()
          return HttpResponseRedirect('/?st=2')

      return render( request, self.template_name, {'form': form, 'name_form': 'Cadastrar Player'})

class PlayerUpdate(View):
  template_name = 'app/player_form.html'

  def get(self, request, *args,**kwargs):
    return render(request, self.template_name, {})

class PlayerDelete(View):
  template_name = 'app/confirm_delete.html'

  def get(self, request, *args,**kwargs):
    return render(request, self.template_name, {})

class PlayerDetail(View):
  template_name = 'app/player_detail.html'
  
  def get(self, request, *args,**kwargs):
    return render(request, self.template_name, {})

class AutoComplete(View):
  def get(self, request, *args,**kwargs):
    return HttpResponse(js, mimetype)