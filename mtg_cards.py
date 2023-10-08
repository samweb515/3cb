class GameAction:
    def __init__(self, name, cost, zone="Hand", timing=None):
        self.name = name
        self.cost = cost
        self.timing = timing
        # 0 = instant speed, 1 = sorcery speed, strings for specific timing restrictions?
        self.zone = zone


class Card:
    def __init__(self, name, card_types, game_actions, power=None, toughness=None):
        # WIP: add triggers, static abilities, keywords, etc
        self.name = name
        self.game_actions = game_actions
        self.card_types = card_types
        if (any(typ) == "Artifact"
            or any(typ) == "Battle"
            or any(typ) == "Enchantment"
            or any(typ) == "Creature"
            or any(typ) == "Land"
            or any(typ) == "Planeswalker"
            for typ in self.card_types):
            # is Permanent
            self.is_permanent = True
            self.is_tapped = False
            self.summoning_sick = True
        else:
            self.is_permanent = False
        if (any(typ) == "Land" for typ in self.card_types):
            self.game_actions.append(GameAction("Land", None, True, "Hand"))
        else:
            # is spell
            pass
        if (any(typ) == "Creature" for typ in self.card_types):
            self.game_actions.append(GameAction("Attack", None, True, "Battlefield"))
            self.game_actions.append(GameAction("Block", None, True, "Battlefield"))
            self.power = power
            self.toughness = toughness
            self.is_blocked = False
            self.damage_marked = 0
        if (any(typ) == "Battle" for typ in self.card_types):
            # WIP
            pass
        if (any(typ) == "Planeswalker" for typ in self.card_types):
            # WIP
            pass


cardlib = {
    "Memnite": Card("Memnite", ["Artifact", "Creature"],
                    [GameAction("Cast", 0)]),
}
