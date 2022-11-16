from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'public_goods_simple'
    multiplier = 1
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField(initial=0) # la extracción total del recurso de los participantes
    other_contribution= models.CurrencyField(initial=0) # la extracción del recurso del resto de los participantes. Utilizar esta variable en la función "set_payoffs"
    

class Player(BasePlayer):
    pass

# FUNCTIONS

def set_payoffs(group: Group):

# PAGES

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class Pagos(Page):
    pass

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results, Pagos]

