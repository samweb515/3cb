# prepare your eyes


class Step:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Permanent:
    def __init__(self):
        self.is_tapped = False
        self.summoning_sick = True


class Creature(Permanent):
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
        self.is_active_player = not place_in_turn_order
        self.hand = deck
        self.library = []
        self.battlefield = []
        self.graveyard = []
        self.exile = []
        self.triggers = []
        print(self.place_in_turn_order, self.is_active_player)

    def draw_card(self):
        if self.library:
            self.hand.append(self.library[0])
            self.library.pop(0)

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
        self.active_player = self.players[0]

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
        for player in self.players:
            self.stack.append(player.triggers)
        if step.name == "Untap":
            for permanent in self.active_player.battlefield:
                permanent.is_tapped = False
        if step.name == "Draw":
            self.active_player.draw_card()
        if step.name == "Declare Attackers":
            self.active_player.declare_attackers()
        if step.name == "Declare Blockers":
            self.players[1].declare_blockers()
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
            print("priority stuffs")

        print("Done ", step.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Controller()

