class Player():
    def __init__(self, name, country, hand, kind):
        # Attributes
        self.name = name
        self.country = country
        self.hand = hand
        self.kind = kind

    # property
    @property
    def describe(self):
        return f"{player.hand} {player.kind}"

if __name__ == "__main__":

    players = [
        {"name": "Tendulkar", "hand": "Right-handed", "country": "India", "kind": "batsman"},
        {"name": "Muralidharan", "hand": "Right-handed", "country": "Sri-lanka", "kind": "bowler"},
        {"name": "Imrul", "hand": "Left-handed", "country": "Bangladesh", "kind": "batsman"}
    ]

    for x in players:
        
        player = Player(x["name"],x["country"],x["hand"], x["kind"])
        print(player.name)
        print(player.describe)
       