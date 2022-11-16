from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'inicio'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES

class instrucciones(Page):
    pass

class calculo(Page):
    pass

class instrucciones_time(Page):
    pass



page_sequence = [instrucciones, calculo, instrucciones_time]
