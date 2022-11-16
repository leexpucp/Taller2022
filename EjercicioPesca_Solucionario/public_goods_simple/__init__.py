from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'public_goods_simple'
    multiplier = 1
    players_per_group = 4
    num_rounds = 10
    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField(initial=0) # la extracción total del recurso de los participantes
    individual_share = models.CurrencyField()
    other_contribution= models.CurrencyField(initial=0) # la extracción del recurso del resto de los participantes. Utilizar esta variable en la función "set_payoffs"
    

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min = 0,
        max = 10,
        label = "¿Cuántas unidades de pescado deseas extraer?"
    )


# FUNCTIONS

def set_payoffs(group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)

# Sentencia for para la determinación del pago
    for player in players:
        player.payoff = 8*player.contribution - 0.3*player.contribution**2 + 80 - 2*group.total_contribution


# PAGES

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
    timeout_seconds = 60

class Pagos(Page):
    pass

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Contribute, ResultsWaitPage, Results, Pagos]
# Eliminaria el html Nivel