from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from pm_app.models import Team, Task
from pm_app.forms import TeamForm, TaskForm, AssignForm, StateForm
from django.views.generic import DetailView
from django.urls import reverse_lazy


def index(request):

    teams = Team.objects.all()
    tasks = Task.objects.all()

    return render(request, 'index.html', {'teams': teams, 'tasks': tasks})


class NewTeamCreate(CreateView):

    redirect_field_name = 'index.html'

    model = Team
    form_class = TeamForm
    template_name = 'newteam.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_manager = self.request.user.profile
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect('/')


class TeamDetailView(DetailView):

    model = Team
    template_name = 'team_info.html'


def approve(request, team_id):
    team = Team.objects.get(id=int(team_id))
    collaborator = request.user.profile
    team.approved.add(collaborator)

    return HttpResponseRedirect('/teams/%s/' % team_id)


class NewTaskCreate(CreateView):

    redirect_field_name = 'index.html'

    model = Task
    form_class = TaskForm
    template_name = 'newtask.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.project_manager = self.request.user.profile
        obj.save()
        return HttpResponseRedirect('/')


class TaskDetailView(DetailView):

    model = Task
    template_name = 'task_info.html'


class TaskAssign(UpdateView):

    model = Task
    form_class = AssignForm
    template_name = 'task_update_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.state = 'open'
        obj.save()
        form.save_m2m()
        return HttpResponseRedirect('/')


class TaskUpdate(UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'task_update_form.html'
    success_url = reverse_lazy('home')


class TaskDelete(DeleteView):

    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('home')


class StateUpdate(UpdateView):

    model = Task
    form_class = StateForm
    template_name = 'state_update_form.html'
    success_url = reverse_lazy('home')
