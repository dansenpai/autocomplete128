from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.shortcuts import render, get_object_or_404
import json
import random
from django.views.generic.edit import DeleteView

class PlayersList(View):
  template_name = 'app/players_list.html'

  def get(self, request, *args,**kwargs):
    return render(request, self.template_name, {})

class PlayerCreate(View):
  template_name = 'app/player_form.html'

  def get(self, request, *args,**kwargs):
      return render(request, self.template_name, {})

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