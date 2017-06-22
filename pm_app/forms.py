from registration.forms import RegistrationFormUniqueEmail
from django import forms
from .models import Team, UserProfile, Task


class ProfileForm(RegistrationFormUniqueEmail):
    ROLE_CHOICES = (('PM', 'project_manager'),
                    ('collaborator', 'collaborator')
                    )

    role = forms.ChoiceField(choices=ROLE_CHOICES)


class TeamForm(forms.ModelForm):

    invited = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.filter(role='collaborator'))

    class Meta:
        model = Team
        fields = ['name', 'invited']


class AssignForm(forms.ModelForm):

    assigned = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.filter(role='collaborator'))

    class Meta:
        model = Task
        fields = ['assigned']


class TaskForm(forms.ModelForm):

    assigned = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.filter(role='collaborator'))

    class Meta:
        model = Task
        fields = ['name', 'type', 'assigned']


class StateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StateForm, self).__init__(*args, **kwargs)

        selected_choices = (('in progress', 'in progress'),
                            ('done', 'done')
                            )

        self.fields['state'].choices = [(k, v) for k, v in selected_choices]

    class Meta:
        model = Task
        fields = ['state']

