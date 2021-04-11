class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.songs = []
        
    def check_in(self, guest):
        if len(self.guest_list) < self.capacity:
            self.guest_list.append(guest)
            return f"{guest.name} checked in to {self.name}"
        
        return "Cannot add guest. Room is full"
        
    def check_out(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)
            return f"{guest.name} has left {self.name}"

    def add_song(song):
        if song not in self.songs:
            self.songs.append(song)

            