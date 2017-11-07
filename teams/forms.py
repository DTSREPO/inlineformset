from django import forms
from django.forms import inlineformset_factory

from teams.models import Team, Member

class TeamForm(forms.models.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'

MemberFormSet = inlineformset_factory(Team, Member, can_delete=True,
        fields=('name', 'position'), extra=1)
