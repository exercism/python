def egg_count(display_value):
    eggs = 0
    while display_value:
        eggs += display_value % 2
        display_value //= 2
    return eggs
