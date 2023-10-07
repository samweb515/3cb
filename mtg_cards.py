class GameAction:
    def __init__(self, name, cost, timing, zone):
        self.name = name
        self.cost = cost
        self.timing = timing
        self.zone = zone


class Card:
    def __init__(self, card_types, game_actions, power=None, toughness=None):
        self.game_actions = game_actions
        if (any(typ) == "Artifact"
            or any(typ) == "Battle"
            or any(typ) == "Enchantment"
            or any(typ) == "Creature"
            or any(typ) == "Land"
            or any(typ) == "Planeswalker"
            for typ in card_types):
            # is Permanent
            self.is_permanent = True
            self.is_tapped = False
            self.summoning_sick = True
        else:
            self.is_permanent = False
        if (any(typ) == "Land" for typ in card_types):
            self.game_actions.append(GameAction("Land", None, True, "Hand"))
        else:
            # is spell
            pass
        if (any(typ) == "Creature" for typ in card_types):
            self.power = power
            self.toughness = toughness
            self.is_blocked = False
            self.damage_marked = 0
        if (any(typ) == "Battle" for typ in card_types):
            # WIP
            pass
        if (any(typ) == "Planeswalker" for typ in card_types):
            # WIP
            pass


typs = ["Artifact", "Creature"]
Card(typs, GameAction("Cast", 0, True, "Hand"))
