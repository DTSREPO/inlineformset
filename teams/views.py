from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction

from teams.models import Team
from teams.forms import TeamForm, MemberFormSet


def teams_list(request):
    teams = Team.objects.all()
    return render(request, 'teams_list.html', {'teams': teams})


def teams_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        formset = MemberFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                team = form.save()
                formset.instance = team
                formset.save()

            return redirect('/teams/')
    else:
        form = TeamForm()
        formset = MemberFormSet()

    forms = [formset.empty_form] + formset.forms
    context = {'form': form, 'formset': formset, 'forms': forms}
    return render(request, 'teams_edit.html', context)


def teams_update(request, pk):
    team = get_object_or_404(Team, pk=pk)

    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        formset = MemberFormSet(request.POST, instance=team)

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()

            return redirect('/teams/')
    else:
        form = TeamForm(instance=team)
        formset = MemberFormSet(instance=team)

    forms = [formset.empty_form] + formset.forms
    context = {'form': form, 'formset': formset, 'forms': forms}
    return render(request, 'teams_edit.html', context)


def teams_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)

    if request.method == 'POST':
        team.delete()
        return redirect('/teams/')

    return render(request, 'teams_delete.html', {'team': team})
