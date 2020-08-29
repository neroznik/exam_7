from django.core.paginator import Paginator
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView

from webapp.models import Poll
from webapp.forms import PollForms
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'poll'
    paginate_by = 5
    paginate_orphans = 0
    model = Poll
    ordering = ['-created_at']


    def get_queryset(self):
        return Poll.objects.all()


class PollView(DetailView):
    template_name = 'poll/poll_view.html'
    context_key = 'poll'
    model = Poll





class PollCreateView(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForms
    fields = ['question']


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})



class PollUpdateView(UpdateView):
    template_name = 'poll/poll_update.html'
    form_class = PollForms
    model = Poll

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})

class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('index')
