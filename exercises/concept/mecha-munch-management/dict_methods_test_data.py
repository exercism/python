##add_item test cases##
add_item_inputs = [
    ({"Apple": 1, "Banana": 4}, ("Apple", "Banana", "Orange")),
    (
        {"Orange": 1, "Raspberry": 1, "Blueberries": 10},
        ["Raspberry", "Blueberries", "Raspberry"],
    ),
    (
        {"Broccoli": 1, "Banana": 1},
        ("Broccoli", "Kiwi", "Kiwi", "Kiwi", "Melon", "Apple", "Banana", "Banana"),
    ),
]

add_item_outputs = [
    {"Apple": 2, "Banana": 5, "Orange": 1},
    {"Orange": 1, "Raspberry": 3, "Blueberries": 11},
    {"Broccoli": 2, "Banana": 3, "Kiwi": 3, "Melon": 1, "Apple": 1},
]

add_item_data = zip(add_item_inputs, add_item_outputs)


##read_notes test cases##
read_notes_inputs = [
    ("Apple", "Banana"),
    ("Orange", "Raspberry", "Blueberries"),
    ["Broccoli", "Kiwi", "Melon", "Apple", "Banana"],
]

read_notes_outputs = [
    {"Apple": 1, "Banana": 1},
    {"Orange": 1, "Raspberry": 1, "Blueberries": 1},
    {"Broccoli": 1, "Kiwi": 1, "Melon": 1, "Apple": 1, "Banana": 1},
]

read_notes_data = zip(read_notes_inputs, read_notes_outputs)


##update_recipes test cases##
update_recipes_inputs = [
    (
        {
            "Banana Bread": {
                "Banana": 1,
                "Apple": 1,
                "Walnuts": 1,
                "Flour": 1,
                "Eggs": 2,
                "Butter": 1,
            },
            "Raspberry Pie": {
                "Raspberry": 1,
                "Orange": 1,
                "Pie Crust": 1,
                "Cream Custard": 1,
            },
        },
        (
            (
                "Banana Bread",
                {
                    "Banana": 4,
                    "Walnuts": 2,
                    "Flour": 1,
                    "Butter": 1,
                    "Milk": 2,
                    "Eggs": 3,
                },
            ),
        ),
    ),
    (
        {
            "Apple Pie": {"Apple": 1, "Pie Crust": 1, "Cream Custard": 1},
            "Blueberry Pie": {"Blueberries": 1, "Pie Crust": 1, "Cream Custard": 1},
        },
        (
            ("Blueberry Pie", {"Blueberries": 2, "Pie Crust": 1, "Cream Custard": 1}),
            ("Apple Pie", {"Apple": 1, "Pie Crust": 1, "Cream Custard": 1}),
        ),
    ),
    (
        {
            "Banana Bread": {
                "Banana": 1,
                "Apple": 1,
                "Walnuts": 1,
                "Flour": 1,
                "Eggs": 2,
                "Butter": 1,
            },
            "Raspberry Pie": {
                "Raspberry": 1,
                "Orange": 1,
                "Pie Crust": 1,
                "Cream Custard": 1,
            },
            "Pasta Primavera": {
                "Eggs": 1,
                "Carrots": 1,
                "Spinach": 2,
                "Tomatoes": 3,
                "Parmesan": 2,
                "Milk": 1,
                "Onion": 1,
            },
        },
        (
            (
                "Raspberry Pie",
                {
                    "Raspberry": 3,
                    "Orange": 1,
                    "Pie Crust": 1,
                    "Cream Custard": 1,
                    "Whipped Cream": 2,
                },
            ),
            (
                "Pasta Primavera",
                {
                    "Eggs": 1,
                    "Mixed Veggies": 2,
                    "Parmesan": 2,
                    "Milk": 1,
                    "Spinach": 1,
                    "Bread Crumbs": 1,
                },
            ),
            (
                "Blueberry Crumble",
                {
                    "Blueberries": 2,
                    "Whipped Creme": 2,
                    "Granola Topping": 2,
                    "Yogurt": 3,
                },
            ),
        ),
    ),
]

update_recipes_outputs = [
    {
        "Banana Bread": {
            "Banana": 4,
            "Walnuts": 2,
            "Flour": 1,
            "Butter": 1,
            "Milk": 2,
            "Eggs": 3,
        },
        "Raspberry Pie": {
            "Raspberry": 1,
            "Orange": 1,
            "Pie Crust": 1,
            "Cream Custard": 1,
        },
    },
    {
        "Apple Pie": {"Apple": 1, "Pie Crust": 1, "Cream Custard": 1},
        "Blueberry Pie": {"Blueberries": 2, "Pie Crust": 1, "Cream Custard": 1},
    },
    {
        "Banana Bread": {
            "Banana": 1,
            "Apple": 1,
            "Walnuts": 1,
            "Flour": 1,
            "Eggs": 2,
            "Butter": 1,
        },
        "Raspberry Pie": {
            "Raspberry": 3,
            "Orange": 1,
            "Pie Crust": 1,
            "Cream Custard": 1,
            "Whipped Cream": 2,
        },
        "Pasta Primavera": {
            "Eggs": 1,
            "Mixed Veggies": 2,
            "Parmesan": 2,
            "Milk": 1,
            "Spinach": 1,
            "Bread Crumbs": 1,
        },
        "Blueberry Crumble": {
            "Blueberries": 2,
            "Whipped Creme": 2,
            "Granola Topping": 2,
            "Yogurt": 3,
        },
    },
]

update_recipes_data = zip(update_recipes_inputs, update_recipes_outputs)


##sort_entries test cases##
sort_entries_inputs = [
    {"Banana": 4, "Apple": 2, "Orange": 1, "Pear": 12},
    {"Apple": 3, "Orange": 5, "Banana": 1, "Avocado": 2},
    {"Orange": 3, "Banana": 2, "Apple": 1},
    {
        "Apple": 2,
        "Raspberry": 2,
        "Blueberries": 5,
        "Broccoli": 2,
        "Kiwi": 1,
        "Melon": 4,
    },
]

sort_entries_outputs = [
    {"Apple": 2, "Banana": 4, "Orange": 1, "Pear": 12},
    {"Apple": 3, "Avocado": 2, "Banana": 1, "Orange": 5},
    {"Apple": 1, "Banana": 2, "Orange": 3},
    {
        "Apple": 2,
        "Blueberries": 5,
        "Broccoli": 2,
        "Kiwi": 1,
        "Melon": 4,
        "Raspberry": 2,
    },
]


sort_entries_data = zip(sort_entries_inputs, sort_entries_outputs)


##send_to_store test cases##
send_to_store_inputs = [
    (
        {"Banana": 3, "Apple": 2, "Orange": 1, "Milk": 2},
        {
            "Banana": ["Aisle 5", False],
            "Apple": ["Aisle 4", False],
            "Orange": ["Aisle 4", False],
            "Milk": ["Aisle 2", True],
        },
    ),
    (
        {"Kiwi": 3, "Juice": 5, "Yoghurt": 2, "Milk": 5},
        {
            "Kiwi": ["Aisle 6", False],
            "Juice": ["Aisle 5", False],
            "Yoghurt": ["Aisle 2", True],
            "Milk": ["Aisle 2", True],
        },
    ),
    (
        {
            "Apple": 2,
            "Raspberry": 2,
            "Blueberries": 5,
            "Broccoli": 2,
            "Kiwi": 1,
            "Melon": 4,
        },
        {
            "Apple": ["Aisle 1", False],
            "Raspberry": ["Aisle 6", False],
            "Blueberries": ["Aisle 6", False],
            "Broccoli": ["Aisle 3", False],
            "Kiwi": ["Aisle 6", False],
            "Melon": ["Aisle 6", False],
        },
    ),
    (
        {"Orange": 1},
        {
            "Banana": ["Aisle 5", False],
            "Apple": ["Aisle 4", False],
            "Orange": ["Aisle 4", False],
            "Milk": ["Aisle 2", True],
        },
    ),
    (
        {"Banana": 3, "Apple": 2, "Orange": 1},
        {
            "Banana": ["Aisle 5", False],
            "Apple": ["Aisle 4", False],
            "Orange": ["Aisle 4", False],
            "Milk": ["Aisle 2", True],
        },
    ),
]

send_to_store_outputs = [
    {
        "Orange": [1, "Aisle 4", False],
        "Milk": [2, "Aisle 2", True],
        "Banana": [3, "Aisle 5", False],
        "Apple": [2, "Aisle 4", False],
    },
    {
        "Yoghurt": [2, "Aisle 2", True],
        "Milk": [5, "Aisle 2", True],
        "Kiwi": [3, "Aisle 6", False],
        "Juice": [5, "Aisle 5", False],
    },
    {
        "Raspberry": [2, "Aisle 6", False],
        "Melon": [4, "Aisle 6", False],
        "Kiwi": [1, "Aisle 6", False],
        "Broccoli": [2, "Aisle 3", False],
        "Blueberries": [5, "Aisle 6", False],
        "Apple": [2, "Aisle 1", False],
    },
    {"Orange": [1, "Aisle 4", False]},
    {
        "Orange": [1, "Aisle 4", False],
        "Banana": [3, "Aisle 5", False],
        "Apple": [2, "Aisle 4", False],
    },
]

send_to_store_data = zip(send_to_store_inputs, send_to_store_outputs)


##update_store_inventory test cases##
update_store_inventory_inputs = [
    (
        {
            "Orange": [1, "Aisle 4", False],
            "Milk": [2, "Aisle 2", True],
            "Banana": [3, "Aisle 5", False],
            "Apple": [2, "Aisle 4", False],
        },
        {
            "Banana": [15, "Aisle 5", False],
            "Apple": [12, "Aisle 4", False],
            "Orange": [1, "Aisle 4", False],
            "Milk": [4, "Aisle 2", True],
        },
    ),
    (
        {"Kiwi": [3, "Aisle 6", False]},
        {
            "Kiwi": [3, "Aisle 6", False],
            "Juice": [5, "Aisle 5", False],
            "Yoghurt": [2, "Aisle 2", True],
            "Milk": [5, "Aisle 2", True],
        },
    ),
    (
        {
            "Kiwi": [1, "Aisle 6", False],
            "Melon": [4, "Aisle 6", False],
            "Apple": [2, "Aisle 1", False],
            "Raspberry": [2, "Aisle 6", False],
            "Blueberries": [5, "Aisle 6", False],
            "Broccoli": [1, "Aisle 3", False],
        },
        {
            "Apple": [2, "Aisle 1", False],
            "Raspberry": [5, "Aisle 6", False],
            "Blueberries": [10, "Aisle 6", False],
            "Broccoli": [4, "Aisle 3", False],
            "Kiwi": [1, "Aisle 6", False],
            "Melon": [8, "Aisle 6", False],
        },
    ),
]

update_store_inventory_outputs = [
    {
        "Banana": [12, "Aisle 5", False],
        "Apple": [10, "Aisle 4", False],
        "Orange": ["Out of Stock", "Aisle 4", False],
        "Milk": [2, "Aisle 2", True],
    },
    {
        "Juice": [5, "Aisle 5", False],
        "Yoghurt": [2, "Aisle 2", True],
        "Milk": [5, "Aisle 2", True],
        "Kiwi": ["Out of Stock", "Aisle 6", False],
    },
    {
        "Kiwi": ["Out of Stock", "Aisle 6", False],
        "Melon": [4, "Aisle 6", False],
        "Apple": ["Out of Stock", "Aisle 1", False],
        "Raspberry": [3, "Aisle 6", False],
        "Blueberries": [5, "Aisle 6", False],
        "Broccoli": [3, "Aisle 3", False],
    },
]

update_store_inventory_data = zip(
    update_store_inventory_inputs, update_store_inventory_outputs
)
