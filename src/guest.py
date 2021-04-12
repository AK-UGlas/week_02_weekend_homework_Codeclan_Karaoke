class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def pay(self, amount):
        self.wallet -= amount

    def woop_obnoxiously(self, playlist):
        if self.favourite_song in playlist:
            return f"YAAAASSSS!!!!, they've got {self.favourite_song.name}!"

    def can_afford_item(self, amount):
        return self.wallet >= amount
