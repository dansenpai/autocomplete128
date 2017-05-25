from django import forms

class FormPlayer(forms.Form):
    name = forms.CharField( label= 'Nome', required=True, widget=forms.TextInput())
    rank_position = forms.IntegerField(label= "Ranking" , required=True, widget=forms.NumberInput())
