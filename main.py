# prepare your eyes


class Step:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Card:
    def __init__(self):
        self.game_actions = []


class Spell(Card):
    def __init__(self, cost, timing):
        super().__init__()
        self.game_actions.append(self.cast())
        self.cost = cost
        self.timing = timing

    def cast(self, cost, step, timing):
        return cost is None and step.name == any(timing)


class Permanent:
    def __init__(self):
        self.is_tapped = False
        self.summoning_sick = True


class Creature(Permanent, Card):
    def __init__(self, power, toughness):
        super().__init__()
        self.power = power
        self.toughness = toughness
        self.is_blocked = False
        self.damage_marked = 0


class Player:
    def __init__(self, place_in_turn_order, deck):
        # deck is submitted cards as list of objects
        self.place_in_turn_order = place_in_turn_order
        self.hand = deck
        self.library = []
        self.battlefield = []
        self.graveyard = []
        self.exile = []
        self.triggers = []
        self.available_game_actions = []
        # add game actions
        for card in self.hand:
            self.available_game_actions.append(card.game_actions)
        self.is_passing = False

    def draw_card(self):
        if self.library:
            self.hand.append(self.library[0])
            self.library.pop(0)

    def game_actions(self, step, is_active):
        print(is_active, self.place_in_turn_order, "is doing stuff at speed of: ", step.name)
        if False:
            pass
        else:
            self.is_passing = True

    def declare_attackers(self):
        print(self.place_in_turn_order, " is attacking stuff")

    def declare_blockers(self):
        print(self.place_in_turn_order, " is blocking stuff")


class Controller:
    # controls steps and game actions
    def __init__(self):
        self.stack = []
        self.attacking_creatures = []

        memnite = "a good card"
        self.players = [
            Player(0, [memnite, memnite, memnite]),
            Player(1, [memnite, memnite, memnite])
        ]

        self.steps_and_phases = [
            Step("Untap", False),
            Step("Upkeep", True),
            Step("Draw", True),
            Step("Main Phase", True),
            Step("Beginning Combat", True),
            Step("Declare Attackers", True),
            Step("Declare Blockers", True),
            Step("First Strike Damage", True),
            Step("Damage", True),
            Step("End Combat", True),
            Step("Main Phase", True),
            Step("End", True),
            Step("Cleanup", False)
        ]
        for step in self.steps_and_phases:
            self.do_step(step)

    def do_step(self, step):
        if step.name == "Untap":
            for permanent in self.players[0].battlefield:
                permanent.is_tapped = False
        if step.name == "Draw":
            self.players[0].draw_card()
        if step.name == "Declare Attackers":
            self.players[0].declare_attackers()
        if step.name == "Declare Blockers":
            self.players[1].declare_blockers()  # change later
        if step.name == "First Strike Damage":
            # WIP
            for creature in self.attacking_creatures:
                if creature.does_first_strike:
                    if creature.is_blocked:
                        print("assign damage")
                    else:
                        creature.defending_permanent_or_player.mark_damage(creature.power)
        if step.name == "Damage":
            # WIP
            for creature in self.attacking_creatures:
                if creature.does_normal_strike:
                    if creature.is_blocked:
                        print("assign damage")
                    else:
                        creature.defending_permanent_or_player.mark_damage(creature.power)
        if step.name == "Cleanup":
            for player in self.players:
                for permanent in player.battlefield:
                    if isinstance(permanent, Player):
                        permanent.damage_marked = 0
        if step.priority:
            for player in self.players:
                self.stack.append(player.triggers)
            # begin priority
            for player in self.players:
                player.is_passing = False
                while not player.is_passing:
                    player.game_actions(step, player == self.players[0])

            print("priority stuffs")

        print("Done ", step.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Controller()

