from otree.api import *

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'inicio_sancion'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):

    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    acepta = models.StringField(choices=['No', 'Sí'], widget=widgets.RadioSelectHorizontal, )
    pass

# PAGES

class instrucciones(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass

class instrucciones_time(Page):
    pass

class calculo(Page):
    pass


page_sequence = [ instrucciones, calculo, instrucciones_time]
