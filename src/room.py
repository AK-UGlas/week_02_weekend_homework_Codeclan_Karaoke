class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        
        self.guest_list = []
        self.songs = []

        self.room_fee = 5
        self.till = 0
        
    def check_in(self, guest):
        # check guest isn't already in the room
        if self.guest_in_room(guest):
            return f"{guest.name} has already checked in"

        # check room has adequate capacity for another guest
        if len(self.guest_list) < self.capacity:
            # check guest has money to pay room fee
            if self.guest_can_pay(guest):
                guest.pay(self.room_fee)
                self.add_to_till(self.room_fee)
                self.guest_list.append(guest)
                return f"{guest.name} checked in to {self.name}"
        
        return "Cannot add guest: Room is full"
        
    def check_out(self, guest):
        if self.guest_in_room(guest):
            self.guest_list.remove(guest)
            return f"{guest.name} has left {self.name}"
        
        return f"{guest.name} is not in {self.name}"

    def guest_in_room(self, guest):
        return guest in self.guest_list

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def add_to_till(self, amount):
        self.till += amount

    def guest_can_pay(self, guest):
        return guest.wallet >= self.room_fee


            