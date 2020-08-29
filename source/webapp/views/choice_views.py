from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoicePollForms
from webapp.models import Choice, Poll


class ChoicePollCreateView(CreateView):
    model = Choice
    template_name = 'choice/choice_create.html'
    form_class = ChoicePollForms

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = choice
        choice.save()
        return redirect('poll_view', pk=poll.pk)



class ChoicePollUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoicePollForms

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoicePollDeleteView(DeleteView):
    model = Choice

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
