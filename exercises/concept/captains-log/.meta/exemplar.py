import random


def random_planet_class():
    planetary_classes = ("D", "H", "J", "K", "L", "M", "N", "R", "T", "Y")
    return random.choice(planetary_classes)


def random_ship_registry_number():
    registry_number = random.randint(1000, 9999)
    return f"NCC-{registry_number}"


def random_stardate():
    return random.uniform(41000.0, 42000.0)
