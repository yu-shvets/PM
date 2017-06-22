"""PM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from pm_app.views import index, NewTeamCreate, TeamDetailView, approve, NewTaskCreate, TaskDetailView, TaskUpdate, \
    TaskDelete, TaskAssign, StateUpdate
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from pm_app.regbackend import MyRegistrationView


urlpatterns = [
    # User Related urls
    url(r'^users/login/$', login, {'authentication_form': AuthenticationForm}, name='login'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^users/profile/$', login_required(TemplateView.as_view(
        template_name='registration/profile.html')), name='profile'),
    url(r'^users/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    url(r'^$', index, name='home'),
    url(r'^newteam/$', NewTeamCreate.as_view(), name='newteam'),
    url(r'^teams/(?P<pk>.+)/$', TeamDetailView.as_view(), name='team_info'),
    url(r'^approve/(?P<team_id>\d+)/$', approve, name='approve'),
    url(r'^newtask/$', NewTaskCreate.as_view(), name='newtask'),
    url(r'^tasks/(?P<pk>.+)/$', TaskDetailView.as_view(), name='task_info'),
    url(r'^edit/(?P<pk>\d+)/$', TaskUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', TaskDelete.as_view(), name='delete'),
    url(r'^assign/(?P<pk>\d+)/$', TaskAssign.as_view(), name='assign'),
    url(r'^update/(?P<pk>\d+)/$', StateUpdate.as_view(), name='update'),

    url(r'^admin/', admin.site.urls),
]
