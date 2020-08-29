from django.urls import reverse
from django.views.generic import TemplateView

from webapp.forms import AnswerForm
from webapp.models import Poll, Answer


class AnswerView(TemplateView):
   template_name = 'answer_view.html'
   form_class = AnswerForm

   def form_valid(self, form):
       self.task = form.save()
       return super().form_valid(form)

   def get_success_url(self):
       return reverse('answer_view', kwargs={'pk': self.task.pk})
