from django.views.generic.edit import FormView

from enrolment.forms import PlanForm


class EnrolmentView(FormView):
    template_name = "enrolment.html"
    form_class = PlanForm

class Plan(FormView):
    template_name = "choice.html"
    form_class = PlanForm