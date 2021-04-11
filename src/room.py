class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.songs = []
        
    def check_in(self, guest):
        # ensure guest isn't already in the room
        if self.guest_in_room(guest):
            return f"{guest.name} has already checked in"

        # make sure room has adequate capacity for another guest
        if len(self.guest_list) < self.capacity:
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

            