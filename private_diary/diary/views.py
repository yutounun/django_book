from email.policy import default
import imp
from operator import ipow
from django.views import generic
from django.urls import reverse_lazy
import logging
from .forms import InquiryForm

# logger setting
logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
  template_name = "index.html"

class InquiryView(generic.FormView):
  template_name = "inquiry.html"
  form_class = InquiryForm
  success_url = reverse_lazy('diary:inquiry')

  # run unless validation blocks form objects
  def form_valid(self, form):
    form.send_email()
    logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
    # call parent class's form_valid
    return super().form_valid(form)