from django import forms

from webapp.models import Poll, Choice


class PollForms(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoicePollForms(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['option']
