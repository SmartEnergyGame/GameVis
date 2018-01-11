from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Instructions(Page):
        pass
class survey(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2']

class AssignationWaitPage(WaitPage):
        body_text = "Waiting for other participants to complete survey."

page_sequence = [survey, AssignationWaitPage,Instructions]
