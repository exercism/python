class Alien:
    total_aliens_created = 0
    health = 3

    def __init__(self, pos_x, pos_y):
        Alien.total_aliens_created += 1
        self.x = pos_x
        self.y = pos_y

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def collision_detection(self, other):
        pass

def new_alien_list(positions):
    return [Alien(position[0], position[1]) for position in positions]
