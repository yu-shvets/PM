from registration.backends.simple.views import RegistrationView
from .forms import ProfileForm
from .models import UserProfile
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from registration.views import ActivationView
from registration.models import RegistrationProfile
from django.contrib.sites.shortcuts import get_current_site


class MyRegistrationView(RegistrationView):

    form_class = ProfileForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        r = form_class.cleaned_data['role']
        new_profile = UserProfile.objects.create(user=new_user, role=r)
        new_profile.save()

        return new_user


