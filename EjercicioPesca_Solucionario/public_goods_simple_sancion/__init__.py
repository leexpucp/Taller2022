from otree.api import *
import random



class Constants(BaseConstants):
    name_in_url = 'public_goods_simple_sancion'
    multiplier = 1
    players_per_group = 4
    num_rounds = 10
    sancion = 9.6

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField(initial=0) # la extracción total del recurso de los participantes
    other_contribution= models.CurrencyField(initial=0) # la extracción del recurso del resto de los participantes. Utilizar esta variable en la función "set_payoffs"
    random_num = models.CurrencyField(initial=0)
    random_player_id = models.CurrencyField(initial=0)

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min = 0,
        max = 10,
        label = "¿Cuántas unidades de pescado deseas extraer?"
    )

    sancion_monto = models.CurrencyField(initial=0)
    pago_final =  models.CurrencyField(initial=0)
    supervision = models.StringField(
        initial = "no fue supervisado"
    )
    monitoreo = models.StringField(
        initial = "no hay monitoreo"
    )

# FUNCTIONS

    
def set_payoffs(group: Group):
       
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)

    group.random_num = random.randint(0,1)
    group.random_player_id = random.randint(1,4)

 # Sentencia for para la determinación del pago: COLOCAR ESTE TITULO EN LA PLANTILLA PARA QUE SE IDENTIFIQUE CON EL TEXTO
 # En la plantilla revisar qué cosas aparece en los html, y qué cosas serán completadas por el alumno.
    for p in players:
        p.payoff = 8*p.contribution - 0.3*p.contribution**2 + 80 - 2*group.total_contribution

 # Sentencias condicionales para monitoreo y supervisión

    ## ¿HAY MONITOREO?

        if group.random_num <= 0.5:
            p.monitoreo="sí hay monitoreo"

    ## ¿HAY SUPERVISIÓN?
        if p.id_in_group == group.random_player_id:
            p.supervision = "sí fue supervisado" 
    # Las funciones condicionales anteriores se usan para ser usadas en el html de pagos.

# Determinación del pago final en caso haya sanción

        if p.id_in_group == group.random_player_id and p.contribution>1 and group.random_num<=0.5:
            p.sancion_monto= Constants.sancion*(p.contribution-1)
            p.pago_final = p.payoff - p.sancion_monto

        else:
            p.pago_final = p.payoff


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
