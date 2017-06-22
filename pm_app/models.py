from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = (('PM', 'project_manager'),
                    ('collaborator', 'collaborator')
                    )

    user = models.OneToOneField(User, related_name='profile')
    role = models.CharField(choices=ROLE_CHOICES, max_length=15)

    def __str__(self):
        return "{}".format(self.user)


class Team(models.Model):

    class Meta(object):
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    name = models.CharField(
        max_length=256,
        blank=False,
    )

    project_manager = models.ForeignKey(UserProfile, related_name='team_manager')

    invited = models.ManyToManyField(UserProfile, related_name='invited_collaborators')

    approved = models.ManyToManyField(UserProfile, related_name='approved_collaborators', blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Task(models.Model):

    class Meta(object):
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    STATE_CHOICES = (('new', 'new'),
                    ('open', 'open'),
                    ('in progress', 'in progress'),
                     ('done', 'done')
                    )

    TYPE_CHOICES = (('bug fix', 'bug fix'),
                    ('code', 'code'),
                    ('test', 'test'),
                    )

    name = models.CharField(
        max_length=256,
        blank=False,
    )

    project_manager = models.ForeignKey(UserProfile, related_name='task_manager')

    assigned = models.ManyToManyField(UserProfile, related_name='assigned_collaborators', blank=True)

    state = models.CharField(choices=STATE_CHOICES, max_length=11, default='new')

    type = models.CharField(choices=TYPE_CHOICES, max_length=7)

    def __str__(self):
        return "{}".format(self.name)