from django import forms

from webapp.models import Poll, Choice


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['option']
