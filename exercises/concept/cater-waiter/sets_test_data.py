# pylint: disable-all
# flake8: noqa,
from sets_categories_data import (VEGAN_INTERSECTIONS,
                                  VEGETARIAN_INTERSECTIONS,
                                  PALEO_INTERSECTIONS,
                                  KETO_INTERSECTIONS,
                                  OMNIVORE_INTERSECTIONS)


###################################
# Data for test_clean_ingredients #
###################################

recipes_with_duplicates  =  [('Kisir with Warm Pita', ['bulgur', 'pomegranate molasses', 'chopped parsley', 'lemon juice', 'tomato', 'persian cucumber', 'tomato paste', 'spring onion', 'water', 'olive oil', 'bulgur', 'bulgur', 'pomegranate molasses', 'pomegranate molasses', 'pomegranate molasses', 'chopped parsley', 'lemon juice', 'tomato', 'tomato', 'persian cucumber', 'tomato paste', 'tomato paste', 'tomato paste']),
                             ('Shakshuka', ['vegan unsweetened yoghurt', 'yellow onion', 'firm tofu', 'smoked paprika', 'tomatoes', 'tomato paste', 'sugar', 'cloves', 'cumin', "za'atar", 'olive oil', 'harissa', 'red bell pepper']),
                             ('Vegetarian Khoresh Bademjan', ['yellow split peas', 'tomato paste', 'black pepper', 'pomegranate concentrate', 'yellow onions', 'slivered almonds', 'ground turmeric', 'barberries', 'basmati rice', 'lemon juice', 'hot water', 'cayenne pepper', 'chinese eggplants', 'salt', 'orange juice', 'saffron powder', 'vegan butter', 'orange zest', 'kosher salt', 'yellow split peas', 'yellow split peas', 'tomato paste', 'tomato paste', 'tomato paste', 'black pepper']),
                             ('Baked Kelewele', ['smoked paprika', 'black peppercorn', 'red onion', 'grains of selim', 'cayenne pepper', 'calabash nutmeg', 'coconut oil', 'cloves', 'fresh ginger', 'salt', 'ripe plantains', 'smoked paprika', 'black peppercorn', 'black peppercorn', 'red onion', 'grains of selim', 'grains of selim', 'grains of selim']),
                             ('Waakye', ['baking soda', 'sorghum stems', 'coconut oil', 'black-eyed peas', 'water', 'salt', 'white rice', 'baking soda', 'baking soda', 'sorghum stems', 'sorghum stems', 'sorghum stems', 'coconut oil']),
                             ('Georgian Eggplant Rolls with Walnuts', ['pomegranate seeds', 'oil', 'coriander', 'garlic', 'khmeli suneli', 'eggplants', 'black pepper', 'vinegar', 'walnuts', 'water', 'salt']),
                             ('Burmese Tofu with Garlic, Ginger and Chili Sauce', ['soy sauce', 'oil', 'chili flakes', 'garlic', 'brown sugar', 'ginger', 'peanuts', 'rice vinegar', 'spring onions', 'water', 'turmeric', 'salt', 'chickpea flour', 'soy sauce', 'soy sauce', 'oil', 'oil', 'oil', 'chili flakes', 'garlic', 'brown sugar', 'brown sugar', 'ginger', 'peanuts', 'peanuts', 'peanuts']),
                             ('Celeriac Schnitzel', ['soy sauce', 'parsley', 'lemon', 'sunflower oil', 'black pepper', 'celeriac', 'breadcrumbs', 'water', 'salt', 'flour', 'chickpea flour']),
                             ('Sticky Lemon Tofu', ['soy sauce', 'vegetable stock', 'tofu', 'cornstarch', 'lemon juice', 'lemon zest', 'garlic', 'ginger', 'black pepper', 'sugar', 'water', 'salt', 'vegetable oil', 'soy sauce', 'soy sauce', 'vegetable stock', 'vegetable stock', 'vegetable stock', 'tofu']),
                             ('Vegan Carbonara', ['soy sauce', 'smoked tofu', 'lemon juice', 'nutritional yeast', 'mixed herbs', 'garlic', 'black pepper', 'silken tofu', 'turmeric', 'salt', 'olive oil', 'spaghetti', 'soy sauce', 'smoked tofu', 'smoked tofu', 'lemon juice', 'nutritional yeast', 'nutritional yeast', 'nutritional yeast']),
                             ('Vegan Pizza with Caramelized Onions', ['mushrooms', 'rosemary', 'garlic', 'red pepper flakes', 'yeast', 'barley malt', 'water', 'olive oil', 'garlic powder', 'oregano', 'honey', 'nutritional yeast', 'red onion', 'tomatoes', 'cashews', 'sugar', 'bell pepper', 'flour', 'salt', 'fresh basil', 'mushrooms', 'mushrooms', 'rosemary', 'rosemary', 'rosemary', 'garlic']),
                             ('Cheela with Spicy Mango Chutney', ['clove powder', 'oil', 'cinnamon powder', 'nigella seeds', 'curry leaves', 'coriander seeds', 'garlic', 'mangoes', 'mashed potatoes', 'cardamom powder', 'vinegar', 'water', 'mustard seeds', 'coriander powder', 'cumin powder', 'mango powder', 'garam masala', 'red chili powder', 'hing', 'garlic paste', 'turmeric powder', 'cilantro', 'sugar', 'onion', 'serrano chili', 'fresh ginger', 'turmeric', 'salt', 'fresh red chili', 'chickpea flour']),
                             ('Sweet and Spicy Crispy Green Beans', ['soy sauce', 'pomegranate molasses', 'sesame oil', 'green beans', 'sunflower oil', 'scallions', 'garlic', 'carrot', 'ginger', 'sesame seeds', 'tomato paste', 'bell pepper', 'siracha', 'soy sauce', 'soy sauce', 'pomegranate molasses', 'pomegranate molasses', 'pomegranate molasses', 'sesame oil', 'green beans', 'sunflower oil', 'sunflower oil', 'scallions', 'garlic', 'garlic', 'garlic']),
                             ('Vegan Mini Savory Mince Pies', ['mushrooms', 'cinnamon powder', 'rosemary', 'corn flour', 'ginger', 'brown sugar', 'carrot', 'black pepper', 'raisins', 'butternut squash', 'vegetarian worcestershire sauce', 'parev shortcrust pastry', 'olive oil', 'vegetable stock', 'dried cherries', 'lemon juice', 'lemon zest', 'figs', 'dried cranberries', 'apples', 'pecans', 'onion', 'orange juice', 'currants', 'dried blueberries', 'salt', 'brandy', 'orange zest', 'allspice powder']),
                             ('Roasted Corn and Zucchini Salad', ['green onions', 'lemon juice', 'lemon zest', 'dill', 'corn', 'tomatoes', 'black pepper', 'zucchini', 'olive oil', 'green onions', 'green onions', 'lemon juice', 'lemon juice', 'lemon juice', 'lemon zest']),
                             ('Golden Potato Salad', ['mustard seeds', 'cumin seeds', 'lemon juice', 'garlic', 'black pepper', 'balsamic vinegar', 'yukon gold potato', 'chives', 'turmeric', 'salt', 'olive oil', 'mustard seeds', 'cumin seeds', 'cumin seeds', 'lemon juice', 'garlic', 'garlic', 'garlic']),
                             ('Carrot Puff Pastry Tart', ['olive oil', 'lemon', 'lemon juice', 'pareve puff pastry', 'brown sugar', 'red onion', 'carrot', 'garlic', 'black pepper', 'thyme', 'vegan butter', 'water', 'salt', 'ground almonds', 'olive oil', 'olive oil', 'lemon', 'lemon', 'lemon', 'lemon juice']),

                             ('Mushroom Lasagna', ['nutmeg', 'garlic', 'black pepper', 'onions', 'butter', 'parmesan cheese', 'portobello mushrooms', 'flour', 'dried lasagna noodles', 'olive oil', 'milk', 'kosher salt']),
                             ('Nut Wellington', ['sage', 'puff pastry sheets', 'hazelnuts', 'almonds', 'black pepper', 'thyme', 'marmite', 'breadcrumbs', 'walnuts', 'dates', 'eggs', 'olive oil', 'brazil nuts', 'leeks', 'chestnuts', 'cashews', 'apples', 'pecans', 'butter', 'salt', 'sage', 'sage', 'puff pastry sheets', 'puff pastry sheets', 'puff pastry sheets', 'hazelnuts', 'almonds', 'black pepper', 'black pepper', 'thyme', 'marmite', 'marmite', 'marmite']),
                             ('White Cheddar Scalloped Potatoes', ['shallots', 'garlic', 'cream', 'thyme', 'breadcrumbs', 'sharp white cheddar', 'yukon gold potato', 'milk', 'kosher salt']),
                             ('Winter Cobb Salad', ['smoked tofu', 'shiitake mushrooms', 'red wine vinegar', 'garlic', 'tomatoes', 'black pepper', 'avocados', 'blue cheese', 'onion', 'lacinato kale', 'eggs', 'olive oil', 'smoked tofu', 'smoked tofu', 'shiitake mushrooms', 'shiitake mushrooms', 'shiitake mushrooms', 'red wine vinegar']),
                             ('Roast Pumpkin and Lentil Salad with Roasted Lemon Dressing', ['honey', 'lemon', 'dijon mustard', 'feta cheese', 'red wine vinegar', 'red onion', 'watercress', 'green lentils', 'currants', 'capers', 'pepitas', 'fresh pumpkin', 'olive oil', 'honey', 'lemon', 'lemon', 'dijon mustard', 'feta cheese', 'feta cheese', 'feta cheese']),
                             ('Cambodian-Style Vegetable Spring Rolls', ['lime juice', 'toasted peanuts', 'firm tofu', 'garlic', 'corn flour', 'bean sprouts', 'carrot', 'palm sugar', 'shallots', 'red chili', 'vermicelli noodles', 'wombok', 'soy sauce', 'sunflower oil', 'spring roll wrappers', 'vegetarian fish sauce', 'lime juice', 'lime juice', 'toasted peanuts', 'toasted peanuts', 'toasted peanuts', 'firm tofu']),
                             ('Summer Minestrone Cups', ['fresh peas', 'rosemary', 'garlic', 'chickpeas', 'carrot', 'leek', 'green lentils', 'red chili', 'olive oil', 'croutons', 'fresh corn', 'lemon zest', 'green beans', 'parmesan rind', 'basil', 'tomatoes', 'vegetable bullion', 'parmesan cheese', 'celery', 'mint']),
                             ('Fried Zucchini with Balsamic and Chili Dressing', ['honey', 'lemon juice', 'garlic', 'red onion', 'red thai chili', 'pomegranate', 'balsamic vinegar', 'mint leaves', 'zucchini', 'olive oil', 'honey', 'honey', 'lemon juice', 'lemon juice', 'lemon juice', 'garlic', 'red onion', 'red thai chili', 'red thai chili', 'pomegranate', 'balsamic vinegar', 'balsamic vinegar', 'balsamic vinegar']),
                             ('Barley Risotto', ['sage', 'beets', 'pearl barley', 'brussel sprouts', 'rosemary', 'garlic', 'carrot', 'red onion', 'black pepper', 'thyme', 'butternut squash', 'vegetable bullion', 'parmesan cheese', 'olive oil', 'white wine']),
                             ('Cherry Tomato, Watercress and Fava Bean Salad', ['fresh peas', 'fresh cherry tomatoes', 'garlic', 'watercress', 'balsamic vinegar', 'fresh or frozen fava beans', 'fresh cherry bocconcini', 'salt', 'olive oil', 'fresh peas', 'fresh peas', 'fresh cherry tomatoes', 'fresh cherry tomatoes', 'fresh cherry tomatoes', 'garlic']),
                             ('Fresh Garden Peas over Cauliflower Almond Puree', ['red onions', 'lemon', 'fresh peas', 'garlic', 'grated nutmeg', 'cream', 'cauliflower', 'blanched almonds', 'fresh pea tendrils', 'olive oil', 'vegetable oil', 'red onions', 'lemon', 'lemon', 'fresh peas', 'garlic', 'garlic', 'garlic']),
                             ('Walnut Ravioli with Artichokes and Tomatoes', ['pine nuts', 'oil marinated artichokes', 'olives', 'rosemary', 'fresh tomatoes', 'ricotta cheese', 'black pepper', 'fresh artichoke hearts', 'walnuts', 'pasta sheets', 'lemon juice', 'lemon zest', 'basil', 'red onion', 'butter', 'salt', 'pine nuts', 'pine nuts', 'oil marinated artichokes', 'oil marinated artichokes', 'oil marinated artichokes', 'olives']),
                             ('Asparagus Puffs', ['eggs', 'asparagus', 'lemon juice', 'red onion', 'ricotta cheese', 'black pepper', 'thyme', 'salt', 'parmesan cheese', 'puff pastry', 'chives']),
                             ('Grilled Tofu Tacos', ['cotija cheese', 'masa', 'fresh cilantro leaves', 'jalapeño chili', 'chipotle chili', 'firm tofu', 'garlic', 'carrot', 'roasted corn', 'tomatillos', 'pepitas', 'ancho chili', 'crema', 'red onions', 'pasilla chili', 'lemon', 'hot water', 'lemon juice', 'tomatoes', 'avocado', 'cumin', 'red cabbage', 'limes', 'black beans', 'cotija cheese', 'cotija cheese', 'masa', 'masa', 'masa', 'fresh cilantro leaves', 'jalapeño chili', 'chipotle chili', 'chipotle chili', 'firm tofu', 'garlic', 'garlic', 'garlic']),

                             ('Zucchini Fritters with Lemon-Thyme Coconut Yogurt', ['baking soda', 'coconut flour', 'lemon juice', 'lemon zest', 'eggs', 'coconut yogurt', 'black pepper', 'fresh thai chili', 'coconut oil', 'chives', 'zucchini', 'salt']),
                             ('Avocado Deviled Eggs', ['lime juice', 'fresh cilantro leaves', 'eggs', 'seranno chili', 'avocado', 'pepitas', 'salt', 'garlic powder', 'lime juice', 'lime juice', 'fresh cilantro leaves', 'fresh cilantro leaves', 'fresh cilantro leaves', 'eggs']),
                             ('Grilled Flank Steak with Caesar Salad', ['pine nuts', 'white vinegar', 'chipotle chili', 'scallions', 'garlic', 'paleo parmesan cheese', 'black pepper', 'avocado oil', 'treviso', 'olive oil', 'radishes', 'flank steak', 'dijon mustard', 'castelfranco radicchio', 'worcestershire sauce', 'fresh parsley', 'cherry tomatoes', 'salt', 'avocado mayonnaise', 'pine nuts', 'white vinegar', 'white vinegar', 'chipotle chili', 'scallions', 'scallions', 'scallions']),
                             ('Pumpkin Bread Crostini', ['coconut flour', 'garlic', 'black pepper', 'cloves', 'eggs', 'olive oil', 'onions', 'honey', 'apple cider vinegar', 'almond butter', 'baking soda', 'nutmeg', 'pumpkin puree', 'cinnamon', 'shrimp', 'basil', 'coconut oil', 'cherry tomatoes', 'salt', 'fresh red chili', 'coconut flour', 'coconut flour', 'garlic', 'garlic', 'garlic', 'black pepper']),
                             ('BLT Bites', ['mustard seed', 'onion', 'kale', 'cherry tomatoes', 'bacon', 'paleo mayonnaise']),
                             ('Roasted Chicken with Roasted Tomatoes, Avocado, and Sweet Potatoes', ['purple sweet potato', 'chiles de árbol', 'garlic', 'tomatoes', 'safflower oil', 'black pepper', 'mexican oregano', 'avocados', 'shallots', 'cumin', 'olive oil', 'lemons', 'whole chicken', 'limes', 'kosher salt', 'purple sweet potato', 'purple sweet potato', 'chiles de árbol', 'chiles de árbol', 'chiles de árbol', 'garlic', 'tomatoes', 'safflower oil', 'safflower oil', 'black pepper', 'mexican oregano', 'mexican oregano', 'mexican oregano']),
                             ('Chicken with Tamarind and Apricot Sauce', ['garlic', 'black pepper', 'dried apricots', 'roma tomatoes', 'water', 'olive oil', 'honey', 'cinnamon', 'ground cumin', 'cider vinegar', 'chili powder', 'safflower oil', 'homemade tamarind concentrate', 'white chicken', 'allspice', 'chipotles', 'salt', 'homemade apricot honey preserves', 'kosher salt']),
                             ('Grilled Fish Tacos with Cauliflower Tortillas', ['green onions', 'serrano chili', 'shredded red cabbage', 'smoked paprika', 'mango', 'eggs', 'black pepper', 'cilantro', 'cauliflower', 'avocado', 'lime', 'cumin', 'salt', 'tilapia', 'green onions', 'green onions', 'serrano chili', 'serrano chili', 'serrano chili', 'shredded red cabbage']),
                             ('Grilled Pork Chops with Mango Pineapple Salsa', ['cilantro leaves', 'lime', 'pineapple', 'chipotle chili', 'garlic', 'mangoes', 'cauliflower', 'avocado', 'serrano chili', 'pork chops', 'lime zest', 'lacinato kale', 'onions', 'cilantro leaves', 'lime', 'lime', 'pineapple', 'chipotle chili', 'chipotle chili', 'chipotle chili']),
                             ('Grilled Shrimp and Pesto over Zucchini Noodles', ['pine nuts', 'shrimp', 'green bell pepper', 'lemon juice', 'basil', 'lemon zest', 'garlic', 'tomatoes', 'cashews', 'yellow bell pepper', 'cumin', 'zucchini', 'salt', 'olive oil', 'red bell pepper', 'pine nuts', 'pine nuts', 'shrimp', 'shrimp', 'shrimp', 'green bell pepper']),

                             ('Cauliflower Pizza with Roasted Tomatoes and Chicken', ['parmesan', 'almond meal', 'rosemary', 'mozzarella cheese', 'roasted chicken', 'tomato paste', 'cauliflower', 'cherry tomatoes', 'eggs', 'fresh basil', 'olive oil']),
                             ('Flank Steak with Chimichurri and Asparagus', ['white vinegar', 'asparagus', 'flank steak', 'chipotle chili', 'scallions', 'garlic', 'black pepper', 'cauliflower', 'sour cream', 'fresh parsley', 'salt', 'olive oil', 'white vinegar', 'white vinegar', 'asparagus', 'asparagus', 'asparagus', 'flank steak', 'chipotle chili', 'scallions', 'scallions', 'garlic', 'black pepper', 'black pepper', 'black pepper']),
                             ('Kingfish Lettuce Cups', ['soy sauce', 'watermelon radishes', 'lime juice', 'fish sauce', 'mirin', 'little gem lettuce heads', 'peanut oil', 'garlic', 'sesame seeds', 'oyster sauce', 'spring onions', 'avocado', 'grilled king fish', 'red cabbage']),
                             ('Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney', ['clove powder', 'curry leaves', 'coriander seeds', 'ginger', 'cardamom powder', 'vinegar', 'mustard seeds', 'mango powder', 'garam masala', 'red chili powder', 'chicken', 'hing', 'turmeric powder', 'tomatoes', 'ginger garlic paste', 'fresh greek yogurt', 'fresh ginger', 'monk fruit', 'turmeric', 'cashew nuts', 'salt', 'fresh red chili', 'cinnamon powder', 'nigella seeds', 'whole small crimini mushrooms', 'brussel sprouts', 'garlic', 'mangoes', 'heavy cream', 'cloves', 'coriander powder', 'cumin powder', 'cardamom', 'green chili', 'cinnamon', 'garlic paste', 'red chili flakes', 'lemon juice', 'cilantro', 'butter', 'dried fenugreek leaves', 'boned chicken', 'clove powder', 'clove powder', 'curry leaves', 'curry leaves', 'curry leaves', 'coriander seeds']),
                             ('Prawn and Herb Omelette', ['green onions', 'parsley', 'sesame seeds', 'black pepper', 'chives', 'eggs', 'fennel bulb', 'tahini', 'olive oil', 'harissa', 'shrimp', 'lemon juice', 'dill', 'butter', 'onion', 'fresh cucumber', 'monk fruit', 'salt', 'green onions', 'parsley', 'parsley', 'sesame seeds', 'black pepper', 'black pepper', 'black pepper']),
                             ('Satay Steak Skewers', ['sriacha', 'apple cider vinegar', 'lime juice', 'fish sauce', 'red and green thai chili', 'flank steak', 'carrot', 'peanuts', 'cucumbers', 'roasted peanuts', 'crunchy peanut butter', 'kecap manis', 'monk fruit', 'micro cilantro', 'olive oil', 'sriacha', 'sriacha', 'apple cider vinegar', 'apple cider vinegar', 'apple cider vinegar', 'lime juice']),
                             ('Parmesan Crackers and Spinach Crackers with Salmon Pate', ['spinach', 'parmesan cheese', 'coconut flour', 'chili flakes', 'garlic', 'black pepper', 'cream cheese', 'ghee', 'lemon juice', 'flaxmeal', 'red onion', 'salt', 'salmon fillets', 'pecans', 'almond flour', 'cumin', 'fresh cucumber', 'cherry tomatoes', 'chives', 'avocado mayonnaise']),
                             ('Pork Chops with Grilled Castelfranco Radicchio and Asparagus', ['rosemary', 'garlic', 'black pepper', 'thyme', 'avocado oil', 'eggs', 'oregano', 'asparagus', 'lemon', 'dijon mustard', 'basil', 'castelfranco radicchio', 'dill', 'butter', 'pork chops', 'monk fruit', 'salt', 'avocado mayonnaise', 'rosemary', 'rosemary', 'garlic', 'garlic', 'garlic', 'black pepper', 'thyme', 'avocado oil', 'avocado oil', 'eggs', 'oregano', 'oregano', 'oregano']),
                             ('Seared Salmon with Pickled Vegetable and Watercress Salad', ['lime juice', 'caster sugar', 'toasted buckwheat', 'lemon juice', 'red wine vinegar', 'red onion', 'dutch carrot', 'salmon steaks', 'watercress', 'pink peppercorns', 'shallots', 'fennel seeds', 'red cabbage', 'radishes']),
                             ('Braised Pork Belly with Apple Salad', ['cilantro leaves', 'green cabbage', 'lemon juice', 'pork belly', 'dark soy sauce', 'granny smith apples', 'ginger', 'light soy sauce', 'sesame seeds', 'black pepper', 'cinnamon sticks', 'spring onions', 'star anise', 'monk fruit', 'olive oil', 'cilantro leaves', 'cilantro leaves', 'green cabbage', 'green cabbage', 'green cabbage', 'lemon juice']),

                             ('Beachside Snapper', ['lime juice', 'salsa', 'green bell pepper', 'anaheim chili', 'black pepper', 'olive oil', 'yellow mustard', 'red bell pepper', 'soy sauce', 'mexican crema', 'mayonnaise', 'white onion', 'garlic cloves', 'fresh corn tortillas', 'red onion', 'tomatoes', 'limes', 'worcestershire sauce', 'butter', 'yellow bell pepper', 'salt', 'red snapper', 'lime juice', 'salsa', 'salsa', 'green bell pepper', 'anaheim chili', 'anaheim chili', 'anaheim chili']),
                             ('Governor Shrimp Tacos', ['lime juice', 'poblano chili', 'tomato paste', 'black pepper', 'chipotle adobo sauce', 'chile manzano', 'roma tomatoes', 'pepitas', 'oaxaca cheese', 'white onion', 'shelled large shrimp', 'garlic cloves', 'fresh corn tortillas', 'red onion', 'worcestershire sauce', 'avocado', 'butter', 'kosher salt', 'lime juice', 'lime juice', 'poblano chili', 'poblano chili', 'poblano chili', 'tomato paste']),
                             ('Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', ['fresh tortillas', 'shrimp', 'garlic', 'chickpeas', 'black pepper', 'slivered almonds', 'guajillo chile', 'bacon', 'sea salt', 'butter', 'onion', 'avocado', 'olive oil']),
                             ('Burnt Masala Wings with Classic Coleslaw', ['lime juice', 'green cabbage', 'chiles de árbol', 'green cardamom', 'ginger', 'carrot', 'sriracha', 'black pepper', 'cinnamon sticks', 'celery seeds', 'cloves', 'black cardamom', 'olive oil', 'chicken wings', 'apple cider vinegar', 'mayonnaise', 'honey', 'black peppercorns', 'lemon juice', 'garlic cloves', 'tamarind concentrate', 'cilantro', 'butter', 'serrano chili', 'red cabbage', 'kosher salt', 'lime juice', 'lime juice', 'green cabbage', 'green cabbage', 'green cabbage', 'chiles de árbol', 'green cardamom', 'ginger', 'ginger', 'carrot', 'sriracha', 'sriracha', 'sriracha']),
                             ('Dahi Puri with Black Chickpeas', ['whole-milk yogurt', 'chaat masala', 'ginger', 'pani puri', 'scallion chutney', 'yukon gold potato', 'black chickpeas', 'thin sev', 'date syrup', 'red onion', 'roasted chicken', 'chili powder', 'tamarind concentrate', 'cumin', 'turmeric', 'mint']),
                             ('Brisket with Grilled Rhubarb, Onions, and Fennel', ['white vinegar', 'parsley', 'yellow onion', 'rhubarb', 'garlic', 'brown sugar', 'black pepper', 'thyme', 'crushed red pepper flakes', 'fennel bulbs', 'beer', 'marjoram', 'vegetable oil', 'soy sauce', 'oregano', 'lemon', 'red onion', 'chili powder', 'cilantro', 'beef brisket', 'balsamic vinegar', 'worcestershire sauce', 'celery', 'mint', 'kosher salt', 'white vinegar', 'white vinegar', 'parsley', 'parsley', 'parsley', 'yellow onion']),
                             ('Roast Leg of Lamb with Crispy Moroccan Carrots & Couscous', ['oranges', 'rosemary', 'garlic', 'anchovy fillets', 'couscous', 'carrot', 'sesame seeds', 'fresh thyme', 'vinegar', 'olive oil', 'tahini', 'harissa', 'onions', 'honey', 'fresh mint', 'leg of lamb', 'tomatoes', 'baby carrot', 'vegetable bullion', 'filo pastry', 'celery', 'bay leaves', 'yoghurt', 'oranges', 'rosemary', 'rosemary', 'garlic', 'anchovy fillets', 'anchovy fillets', 'anchovy fillets']),
                             ('Baked Chicken Jollof Rice', ['tomato puree', 'garlic', 'ginger', 'tomato', 'carrot', 'thyme', 'white pepper', 'water', 'maggi cubes', 'chicken', 'rice', 'coriander', 'scotch bonnet pepper', 'bell pepper', 'onion', 'turmeric', 'salt', 'tomato puree', 'tomato puree', 'garlic', 'garlic', 'garlic', 'ginger']),
                             ('Seafood Risotto', ['garlic', 'tomato paste', 'baby scallops', 'mussels', 'water', 'crab legs', 'olive oil', 'baby squid', 'fish stock', 'lemon juice', 'white onion', 'arborio risotto rice', 'clams', 'parmesan cheese', 'flat-leaf parsley', 'cherry tomatoes', 'prawns', 'white wine']),
                             ('Lamb over Marinated Summer Squash with Hazelnuts and Ricotta', ['toasted bread', 'rosemary', 'hazelnuts', 'anchovy fillets', 'garlic', 'carrot', 'summer squash', 'black pepper', 'red pepper flakes', 'vinegar', 'sea salt', 'zucchini', 'olive oil', 'onions', 'white wine vinegar', 'fresh mint', 'leg of lamb', 'lemon', 'fresh ricotta', 'sugar', 'celery', 'bay leaves', 'kosher salt', 'toasted bread', 'toasted bread', 'rosemary', 'rosemary', 'rosemary', 'hazelnuts', 'anchovy fillets', 'garlic', 'garlic', 'carrot', 'summer squash', 'summer squash', 'summer squash'])
                             ]

recipes_without_duplicates  =  [('kisir_with_warm_pita', 'Kisir with Warm Pita', {'water', 'chopped parsley', 'pomegranate molasses', 'spring onion', 'lemon juice', 'olive oil', 'bulgur', 'tomato paste', 'tomato', 'persian cucumber'}),
                                ('shakshuka', 'Shakshuka', {'smoked paprika', 'tomatoes', 'cumin', 'firm tofu', 'olive oil', 'harissa', 'yellow onion', 'sugar', "za'atar", 'tomato paste', 'cloves', 'red bell pepper', 'vegan unsweetened yoghurt'}),
                                ('vegetarian_khoresh_bademjan', 'Vegetarian Khoresh Bademjan', {'pomegranate concentrate', 'saffron powder', 'cayenne pepper', 'barberries', 'salt', 'yellow onions', 'yellow split peas', 'slivered almonds', 'ground turmeric', 'orange zest', 'lemon juice', 'kosher salt', 'hot water', 'basmati rice', 'black pepper', 'orange juice', 'tomato paste', 'vegan butter', 'chinese eggplants'}),
                                ('baked_kelewele', 'Baked Kelewele', {'salt', 'coconut oil', 'smoked paprika', 'cayenne pepper', 'red onion', 'fresh ginger', 'calabash nutmeg', 'grains of selim', 'black peppercorn', 'cloves', 'ripe plantains'}),
                                ('waakye', 'Waakye', {'salt', 'coconut oil', 'water', 'white rice', 'sorghum stems', 'black-eyed peas', 'baking soda'}),
                                ('georgian_eggplant_rolls_with_walnuts', 'Georgian Eggplant Rolls with Walnuts', {'salt', 'coriander', 'pomegranate seeds', 'oil', 'water', 'vinegar', 'garlic', 'eggplants', 'black pepper', 'khmeli suneli', 'walnuts'}),
                                ('burmese_tofu_with_garlic,_ginger_and_chili_sauce', 'Burmese Tofu with Garlic, Ginger and Chili Sauce', {'salt', 'rice vinegar', 'oil', 'water', 'turmeric', 'chili flakes', 'spring onions', 'brown sugar', 'garlic', 'chickpea flour', 'ginger', 'soy sauce', 'peanuts'}),
                                ('celeriac_schnitzel', 'Celeriac Schnitzel', {'salt', 'parsley', 'water', 'sunflower oil', 'flour', 'breadcrumbs', 'lemon', 'celeriac', 'chickpea flour', 'soy sauce', 'black pepper'}),
                                ('sticky_lemon_tofu', 'Sticky Lemon Tofu', {'salt', 'water', 'tofu', 'cornstarch', 'vegetable stock', 'vegetable oil', 'lemon juice', 'garlic', 'black pepper', 'ginger', 'soy sauce', 'sugar', 'lemon zest'}),
                                ('vegan_carbonara', 'Vegan Carbonara', {'salt', 'turmeric', 'spaghetti', 'lemon juice', 'olive oil', 'garlic', 'black pepper', 'nutritional yeast', 'soy sauce', 'smoked tofu', 'silken tofu', 'mixed herbs'}),
                                ('vegan_pizza_with_caramelized_onions', 'Vegan Pizza with Caramelized Onions', {'red pepper flakes', 'garlic', 'cashews', 'fresh basil', 'flour', 'tomatoes', 'red onion', 'oregano', 'nutritional yeast', 'rosemary', 'water', 'bell pepper', 'honey', 'barley malt', 'olive oil', 'salt', 'garlic powder', 'mushrooms', 'yeast', 'sugar'}),
                                ('cheela_with_spicy_mango_chutney', 'Cheela with Spicy Mango Chutney', {'hing', 'curry leaves', 'mangoes', 'garlic', 'nigella seeds', 'garlic paste', 'coriander seeds', 'oil', 'turmeric', 'red chili powder', 'coriander powder', 'cardamom powder', 'turmeric powder', 'clove powder', 'water', 'cumin powder', 'fresh ginger', 'vinegar', 'cinnamon powder', 'cilantro', 'chickpea flour', 'onion', 'salt', 'mango powder', 'fresh red chili', 'mashed potatoes', 'mustard seeds', 'serrano chili', 'garam masala', 'sugar'}),
                                ('sweet_and_spicy_crispy_green_beans', 'Sweet and Spicy Crispy Green Beans', {'sesame oil', 'siracha', 'sunflower oil', 'pomegranate molasses', 'sesame seeds', 'green beans', 'carrot', 'scallions', 'garlic', 'ginger', 'soy sauce', 'tomato paste', 'bell pepper'}),
                                ('vegan_mini_savory_mince_pies', 'Vegan Mini Savory Mince Pies', {'apples', 'brandy', 'pecans', 'raisins', 'brown sugar', 'lemon zest', 'dried blueberries', 'vegetarian worcestershire sauce', 'orange zest', 'butternut squash', 'corn flour', 'rosemary', 'vegetable stock', 'carrot', 'figs', 'cinnamon powder', 'olive oil', 'orange juice', 'black pepper', 'onion', 'dried cherries', 'salt', 'dried cranberries', 'parev shortcrust pastry', 'mushrooms', 'allspice powder', 'lemon juice', 'ginger', 'currants'}),
                                ('roasted_corn_and_zucchini_salad', 'Roasted Corn and Zucchini Salad', {'zucchini', 'tomatoes', 'green onions', 'corn', 'lemon juice', 'olive oil', 'black pepper', 'lemon zest', 'dill'}),
                                ('golden_potato_salad', 'Golden Potato Salad', {'salt', 'yukon gold potato', 'turmeric', 'balsamic vinegar', 'cumin seeds', 'lemon juice', 'olive oil', 'garlic', 'mustard seeds', 'black pepper', 'chives'}),
                                ('carrot_puff_pastry_tart', 'Carrot Puff Pastry Tart', {'salt', 'water', 'lemon', 'thyme', 'red onion', 'carrot', 'lemon juice', 'pareve puff pastry', 'ground almonds', 'brown sugar', 'olive oil', 'garlic', 'black pepper', 'vegan butter'}),

                                ('mushroom_lasagna', 'Mushroom Lasagna', {'dried lasagna noodles', 'portobello mushrooms', 'nutmeg', 'flour', 'kosher salt', 'milk', 'olive oil', 'garlic', 'onions', 'butter', 'black pepper', 'parmesan cheese'}),
                                ('nut_wellington', 'Nut Wellington', {'apples', 'eggs', 'hazelnuts', 'pecans', 'thyme', 'dates', 'cashews', 'breadcrumbs', 'almonds', 'marmite', 'sage', 'leeks', 'olive oil', 'black pepper', 'walnuts', 'salt', 'chestnuts', 'brazil nuts', 'butter', 'puff pastry sheets'}),
                                ('white_cheddar_scalloped_potatoes', 'White Cheddar Scalloped Potatoes', {'yukon gold potato', 'shallots', 'cream', 'thyme', 'breadcrumbs', 'sharp white cheddar', 'kosher salt', 'milk', 'garlic'}),
                                ('winter_cobb_salad', 'Winter Cobb Salad', {'lacinato kale', 'eggs', 'red wine vinegar', 'shiitake mushrooms', 'tomatoes', 'avocados', 'olive oil', 'blue cheese', 'garlic', 'black pepper', 'onion', 'smoked tofu'}),
                                ('roast_pumpkin_and_lentil_salad_with_roasted_lemon_dressing', 'Roast Pumpkin and Lentil Salad with Roasted Lemon Dressing', {'red wine vinegar', 'dijon mustard', 'lemon', 'honey', 'red onion', 'feta cheese', 'olive oil', 'capers', 'pepitas', 'fresh pumpkin', 'watercress', 'green lentils', 'currants'}),
                                ('cambodian-style_vegetable_spring_rolls', 'Cambodian-Style Vegetable Spring Rolls', {'sunflower oil', 'vegetarian fish sauce', 'shallots', 'vermicelli noodles', 'wombok', 'firm tofu', 'lime juice', 'corn flour', 'palm sugar', 'bean sprouts', 'spring roll wrappers', 'garlic', 'red chili', 'soy sauce', 'toasted peanuts', 'carrot'}),
                                ('summer_minestrone_cups', 'Summer Minestrone Cups', {'leek', 'garlic', 'lemon zest', 'tomatoes', 'red chili', 'chickpeas', 'rosemary', 'carrot', 'vegetable bullion', 'fresh corn', 'fresh peas', 'green beans', 'olive oil', 'parmesan cheese', 'croutons', 'celery', 'mint', 'basil', 'green lentils', 'parmesan rind'}),
                                ('fried_zucchini_with_balsamic_and_chili_dressing', 'Fried Zucchini with Balsamic and Chili Dressing', {'zucchini', 'balsamic vinegar', 'honey', 'red onion', 'lemon juice', 'olive oil', 'mint leaves', 'garlic', 'red thai chili', 'pomegranate'}),
                                ('barley_risotto', 'Barley Risotto', {'beets', 'white wine', 'thyme', 'red onion', 'carrot', 'butternut squash', 'olive oil', 'sage', 'garlic', 'brussel sprouts', 'rosemary', 'black pepper', 'parmesan cheese', 'pearl barley', 'vegetable bullion'}),
                                ('cherry_tomato,_watercress_and_fava_bean_salad', 'Cherry Tomato, Watercress and Fava Bean Salad', {'salt', 'fresh or frozen fava beans', 'fresh peas', 'balsamic vinegar', 'olive oil', 'garlic', 'watercress', 'fresh cherry bocconcini', 'fresh cherry tomatoes'}),
                                ('fresh_garden_peas_over_cauliflower_almond_puree', 'Fresh Garden Peas over Cauliflower Almond Puree', {'grated nutmeg', 'red onions', 'lemon', 'fresh peas', 'cream', 'vegetable oil', 'olive oil', 'garlic', 'blanched almonds', 'cauliflower', 'fresh pea tendrils'}),
                                ('walnut_ravioli_with_artichokes_and_tomatoes', 'Walnut Ravioli with Artichokes and Tomatoes', {'salt', 'fresh tomatoes', 'ricotta cheese', 'lemon zest', 'olives', 'red onion', 'lemon juice', 'black pepper', 'rosemary', 'butter', 'basil', 'fresh artichoke hearts', 'pasta sheets', 'pine nuts', 'walnuts', 'oil marinated artichokes'}),
                                ('asparagus_puffs', 'Asparagus Puffs', {'salt', 'asparagus', 'ricotta cheese', 'thyme', 'puff pastry', 'red onion', 'eggs', 'lemon juice', 'black pepper', 'parmesan cheese', 'chives'}),
                                ('grilled_tofu_tacos', 'Grilled Tofu Tacos', {'carrot', 'red cabbage', 'ancho chili', 'limes', 'hot water', 'garlic', 'roasted corn', 'masa', 'pasilla chili', 'lemon', 'tomatoes', 'cumin', 'fresh cilantro leaves', 'chipotle chili', 'red onions', 'pepitas', 'tomatillos', 'black beans', 'cotija cheese', 'crema', 'firm tofu', 'lemon juice', 'jalapeño chili', 'avocado'}),

                                ('zucchini_fritters_with_lemon-thyme_coconut_yogurt', 'Zucchini Fritters with Lemon-Thyme Coconut Yogurt', {'salt', 'coconut oil', 'eggs', 'fresh thai chili', 'coconut yogurt', 'zucchini', 'lemon juice', 'black pepper', 'coconut flour', 'chives', 'lemon zest', 'baking soda'}),
                                ('avocado_deviled_eggs', 'Avocado Deviled Eggs', {'salt', 'eggs', 'garlic powder', 'seranno chili', 'avocado', 'lime juice', 'pepitas', 'fresh cilantro leaves'}),
                                ('grilled_flank_steak_with_caesar_salad', 'Grilled Flank Steak with Caesar Salad', {'flank steak', 'avocado oil', 'treviso', 'scallions', 'garlic', 'cherry tomatoes', 'pine nuts', 'white vinegar', 'chipotle chili', 'dijon mustard', 'olive oil', 'avocado mayonnaise', 'black pepper', 'paleo parmesan cheese', 'castelfranco radicchio', 'fresh parsley', 'salt', 'worcestershire sauce', 'radishes'}),
                                ('pumpkin_bread_crostini', 'Pumpkin Bread Crostini', {'eggs', 'nutmeg', 'cinnamon', 'garlic', 'pumpkin puree', 'apple cider vinegar', 'cherry tomatoes', 'onions', 'coconut flour', 'cloves', 'shrimp', 'coconut oil', 'honey', 'olive oil', 'black pepper', 'almond butter', 'salt', 'fresh red chili', 'basil', 'baking soda'}),
                                ('blt_bites', 'BLT Bites', {'paleo mayonnaise', 'bacon', 'kale', 'cherry tomatoes', 'mustard seed', 'onion'}),
                                ('roasted_chicken_with_roasted_tomatoes,_avocado,_and_sweet_potatoes', 'Roasted Chicken with Roasted Tomatoes, Avocado, and Sweet Potatoes', {'safflower oil', 'shallots', 'whole chicken', 'lemons', 'tomatoes', 'purple sweet potato', 'avocados', 'limes', 'kosher salt', 'olive oil', 'mexican oregano', 'garlic', 'black pepper', 'cumin', 'chiles de árbol'}),
                                ('chicken_with_tamarind_and_apricot_sauce', 'Chicken with Tamarind and Apricot Sauce', {'cinnamon', 'garlic', 'cider vinegar', 'chipotles', 'homemade tamarind concentrate', 'roma tomatoes', 'white chicken', 'ground cumin', 'water', 'safflower oil', 'allspice', 'dried apricots', 'honey', 'olive oil', 'black pepper', 'salt', 'homemade apricot honey preserves', 'kosher salt', 'chili powder'}),
                                ('grilled_fish_tacos_with_cauliflower_tortillas', 'Grilled Fish Tacos with Cauliflower Tortillas', {'salt', 'eggs', 'smoked paprika', 'shredded red cabbage', 'mango', 'green onions', 'lime', 'cumin', 'tilapia', 'cilantro', 'black pepper', 'serrano chili', 'cauliflower', 'avocado'}),
                                ('grilled_pork_chops_with_mango_pineapple_salsa', 'Grilled Pork Chops with Mango Pineapple Salsa', {'pork chops', 'lacinato kale', 'chipotle chili', 'serrano chili', 'lime zest', 'pineapple', 'lime', 'garlic', 'onions', 'mangoes', 'cauliflower', 'avocado', 'cilantro leaves'}),
                                ('grilled_shrimp_and_pesto_over_zucchini_noodles', 'Grilled Shrimp and Pesto over Zucchini Noodles', {'salt', 'green bell pepper', 'cashews', 'zucchini', 'tomatoes', 'red bell pepper', 'cumin', 'lemon juice', 'yellow bell pepper', 'olive oil', 'garlic', 'pine nuts', 'basil', 'lemon zest', 'shrimp'}),

                                ('cauliflower_pizza_with_roasted_tomatoes_and_chicken', 'Cauliflower Pizza with Roasted Tomatoes and Chicken', {'roasted chicken', 'eggs', 'fresh basil', 'olive oil', 'almond meal', 'cherry tomatoes', 'rosemary', 'cauliflower', 'mozzarella cheese', 'tomato paste', 'parmesan'}),
                                ('flank_steak_with_chimichurri_and_asparagus', 'Flank Steak with Chimichurri and Asparagus', {'fresh parsley', 'salt', 'asparagus', 'chipotle chili', 'flank steak', 'scallions', 'olive oil', 'garlic', 'black pepper', 'cauliflower', 'white vinegar', 'sour cream'}),
                                ('kingfish_lettuce_cups', 'Kingfish Lettuce Cups', {'oyster sauce', 'fish sauce', 'spring onions', 'sesame seeds', 'grilled king fish', 'little gem lettuce heads', 'mirin', 'red cabbage', 'lime juice', 'peanut oil', 'garlic', 'watermelon radishes', 'soy sauce', 'avocado'}),
                                ('butter_chicken_with_grilled_mushrooms,_brussel_sprouts_and_mango_chutney', 'Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney', {'hing', 'curry leaves', 'cashew nuts', 'green chili', 'cinnamon', 'mangoes', 'garlic', 'nigella seeds', 'garlic paste', 'coriander seeds', 'turmeric', 'ginger garlic paste', 'tomatoes', 'red chili powder', 'coriander powder', 'cardamom powder', 'turmeric powder', 'clove powder', 'cloves', 'heavy cream', 'cardamom', 'fresh greek yogurt', 'monk fruit', 'fresh ginger', 'cumin powder', 'vinegar', 'cinnamon powder', 'cilantro', 'brussel sprouts', 'whole small crimini mushrooms', 'salt', 'boned chicken', 'red chili flakes', 'mango powder', 'fresh red chili', 'lemon juice', 'garam masala', 'butter', 'ginger', 'mustard seeds', 'chicken', 'dried fenugreek leaves'}),
                                ('prawn_and_herb_omelette', 'Prawn and Herb Omelette', {'salt', 'parsley', 'eggs', 'fresh cucumber', 'sesame seeds', 'green onions', 'monk fruit', 'lemon juice', 'olive oil', 'tahini', 'harissa', 'black pepper', 'butter', 'onion', 'fennel bulb', 'chives', 'shrimp', 'dill'}),
                                ('satay_steak_skewers', 'Satay Steak Skewers', {'flank steak', 'red and green thai chili', 'kecap manis', 'fish sauce', 'monk fruit', 'micro cilantro', 'carrot', 'apple cider vinegar', 'sriacha', 'lime juice', 'olive oil', 'cucumbers', 'roasted peanuts', 'crunchy peanut butter', 'peanuts'}),
                                ('parmesan_crackers_and_spinach_crackers_with_salmon_pate', 'Parmesan Crackers and Spinach Crackers with Salmon Pate', {'fresh cucumber', 'pecans', 'ghee', 'garlic', 'chives', 'flaxmeal', 'chili flakes', 'almond flour', 'salmon fillets', 'red onion', 'cherry tomatoes', 'coconut flour', 'cumin', 'spinach', 'cream cheese', 'avocado mayonnaise', 'black pepper', 'parmesan cheese', 'salt', 'lemon juice'}),
                                ('pork_chops_with_grilled_castelfranco_radicchio_and_asparagus', 'Pork Chops with Grilled Castelfranco Radicchio and Asparagus', {'pork chops', 'salt', 'asparagus', 'eggs', 'dijon mustard', 'avocado oil', 'lemon', 'thyme', 'monk fruit', 'oregano', 'avocado mayonnaise', 'garlic', 'black pepper', 'rosemary', 'butter', 'basil', 'castelfranco radicchio', 'dill'}),
                                ('seared_salmon_with_pickled_vegetable_and_watercress_salad', 'Seared Salmon with Pickled Vegetable and Watercress Salad', {'red wine vinegar', 'caster sugar', 'salmon steaks', 'radishes', 'shallots', 'red onion', 'pink peppercorns', 'toasted buckwheat', 'lemon juice', 'lime juice', 'red cabbage', 'watercress', 'fennel seeds', 'dutch carrot'}),
                                ('braised_pork_belly_with_apple_salad', 'Braised Pork Belly with Apple Salad', {'spring onions', 'dark soy sauce', 'light soy sauce', 'pork belly', 'monk fruit', 'green cabbage', 'star anise', 'sesame seeds', 'lemon juice', 'olive oil', 'black pepper', 'ginger', 'cinnamon sticks', 'granny smith apples', 'cilantro leaves'}),

                                ('beachside_snapper', 'Beachside Snapper', {'yellow mustard', 'mayonnaise', 'limes', 'white onion', 'red snapper', 'fresh corn tortillas', 'tomatoes', 'red onion', 'lime juice', 'soy sauce', 'mexican crema', 'salsa', 'garlic cloves', 'green bell pepper', 'olive oil', 'black pepper', 'salt', 'yellow bell pepper', 'worcestershire sauce', 'anaheim chili', 'butter', 'red bell pepper'}),
                                ('governor_shrimp_tacos', 'Governor Shrimp Tacos', {'chile manzano', 'worcestershire sauce', 'oaxaca cheese', 'garlic cloves', 'red onion', 'avocado', 'lime juice', 'kosher salt', 'white onion', 'chipotle adobo sauce', 'poblano chili', 'fresh corn tortillas', 'butter', 'black pepper', 'pepitas', 'tomato paste', 'roma tomatoes', 'shelled large shrimp'}),
                                ('shrimp,_bacon_and_crispy_chickpea_tacos_with_salsa_de_guacamole', 'Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', {'fresh tortillas', 'slivered almonds', 'bacon', 'sea salt', 'chickpeas', 'olive oil', 'guajillo chile', 'garlic', 'butter', 'black pepper', 'onion', 'shrimp', 'avocado'}),
                                ('burnt_masala_wings_with_classic_coleslaw', 'Burnt Masala Wings with Classic Coleslaw', {'mayonnaise', 'carrot', 'red cabbage', 'green cabbage', 'apple cider vinegar', 'lime juice', 'cloves', 'cinnamon sticks', 'sriracha', 'celery seeds', 'chicken wings', 'garlic cloves', 'honey', 'olive oil', 'cilantro', 'black pepper', 'chiles de árbol', 'tamarind concentrate', 'green cardamom', 'black cardamom', 'lemon juice', 'kosher salt', 'serrano chili', 'ginger', 'black peppercorns', 'butter'}),
                                ('dahi_puri_with_black_chickpeas', 'Dahi Puri with Black Chickpeas', {'roasted chicken', 'scallion chutney', 'yukon gold potato', 'turmeric', 'black chickpeas', 'whole-milk yogurt', 'chili powder', 'red onion', 'pani puri', 'ginger', 'mint', 'thin sev', 'date syrup', 'cumin', 'chaat masala', 'tamarind concentrate'}),
                                ('brisket_with_grilled_rhubarb,_onions,_and_fennel', 'Brisket with Grilled Rhubarb, Onions, and Fennel', {'crushed red pepper flakes', 'rhubarb', 'thyme', 'yellow onion', 'garlic', 'brown sugar', 'beer', 'lemon', 'red onion', 'oregano', 'soy sauce', 'white vinegar', 'beef brisket', 'parsley', 'marjoram', 'balsamic vinegar', 'vegetable oil', 'fennel bulbs', 'cilantro', 'black pepper', 'worcestershire sauce', 'celery', 'kosher salt', 'mint', 'chili powder'}),
                                ('roast_leg_of_lamb_with_crispy_moroccan_carrots_&_couscous', 'Roast Leg of Lamb with Crispy Moroccan Carrots & Couscous', {'bay leaves', 'fresh thyme', 'carrot', 'tahini', 'garlic', 'baby carrot', 'oranges', 'filo pastry', 'tomatoes', 'harissa', 'onions', 'rosemary', 'leg of lamb', 'vegetable bullion', 'sesame seeds', 'honey', 'anchovy fillets', 'vinegar', 'olive oil', 'couscous', 'fresh mint', 'celery', 'yoghurt'}),
                                ('baked_chicken_jollof_rice', 'Baked Chicken Jollof Rice', {'coriander', 'salt', 'white pepper', 'water', 'bell pepper', 'turmeric', 'rice', 'scotch bonnet pepper', 'chicken', 'thyme', 'maggi cubes', 'garlic', 'ginger', 'onion', 'tomato', 'carrot', 'tomato puree'}),
                                ('seafood_risotto', 'Seafood Risotto', {'white wine', 'water', 'clams', 'crab legs', 'baby squid', 'lemon juice', 'parmesan cheese', 'olive oil', 'white onion', 'garlic', 'arborio risotto rice', 'fish stock', 'mussels', 'flat-leaf parsley', 'tomato paste', 'prawns', 'baby scallops', 'cherry tomatoes'}),
                                ('lamb_over_marinated_summer_squash_with_hazelnuts_and_ricotta', 'Lamb over Marinated Summer Squash with Hazelnuts and Ricotta', {'red pepper flakes', 'hazelnuts', 'zucchini', 'bay leaves', 'carrot', 'garlic', 'white wine vinegar', 'toasted bread', 'lemon', 'onions', 'rosemary', 'leg of lamb', 'summer squash', 'sea salt', 'anchovy fillets', 'vinegar', 'olive oil', 'black pepper', 'fresh mint', 'celery', 'kosher salt', 'fresh ricotta', 'sugar'})
                                ]

##############################
# Data for test_check_drinks #
##############################


all_drinks  =  [('Amaretto Sour', ['almond liqueur', 'bourbon', 'cherries', 'egg white', 'lemon juice', 'lemon twist', 'simple syrup']),
                ('Aperol Spritz', ['aperol', 'prosecco', 'soda water']),
                ('Bannana Punch', ['banana', 'ginger ale', 'lemonade', 'orange juice', 'pineapple juice', 'sugar', 'water']),
                ('Beet Sumac Soda', ['beet', 'club soda', 'fresh lemon juice', 'sugar', 'sumac']),
                ('Better Than Celery Juice', ['apple cider vinegar', 'black pepper', 'celery stalks', 'club soda', 'granny smith apples', 'kosher salt', 'parsley']),
                ('Black & Blue Berries', ['blackberries', 'blueberries', 'honey', 'lemon juice', 'soda water']),
                ('Bloody Mary', ['celery', 'celery salt', 'lemon juice', 'pepper', 'tomato juice', 'vodka', 'worcestershire sauce']),
                ('Bloody Shame', ['V8 juice', 'black pepper', 'celery', 'salt', 'tabasco sauce']),
                ('Chai Blossom', ['chai tea bags', 'club soda', 'fresh lime juice', 'lemon twists', 'start anise pods', 'sugar']),
                ('Chile-lime Pineapple Soda', ['chiles de árbol', 'club soda', 'fresh pineapple juice', 'kosher salt', 'lime juice', 'lime wedges', 'pink peppercorns', 'sugar']),
                ('Citrus Fizz', ['organic marmalade cordial', 'seedlip grove 42', 'sparkling water']),
                ('Dry Martini', ['dry vermouth', 'gin', 'lemon twist', 'olives']),
                ('Espresso Martini', ['coffee liqueur', 'espresso', 'sugar syrup', 'vodka']),
                ('Fermented Grape Soda', ['red seedless grapes', 'sugar', 'washed organic ginger']),
                ('French 75', ['champagne', 'gin', 'lemon juice', 'sugar syrup']),
                ('Gimlet', ['gin', 'lime juice', 'sugar syrup']),
                ('Gin Fizz', ['gin', 'lemon juice', 'soda water', 'sugar syrup']),
                ('Huckleberry Shrub', ['club soda', 'huckleberries', 'sugar', 'white wine vinegar']),
                ('Mai Tai', ['cherries', 'lime juice', 'lime wedge', 'mint leaves', 'orange curacao', 'orgeat syrup', 'rum', 'sugar syrup']),
                ('Mango Mule', ['cucumber', 'fresh lime juice', 'ginger beer', 'honey syrup', 'ice', 'mango puree']),
                ('Manhattan', ['bitters', 'cherry', 'rye', 'sweet vermouth']),
                ('Maple-Ginger Cider Switchel', ['apple cider vinegar', 'club soda', 'fresh ginger', 'fresh lime juice', 'maple syrup', 'mint sprigs']),
                ('Margarita', ['lime juice', 'salt', 'simple syrup', 'tequila', 'triple sec']),
                ('Mojito', ['lime', 'mint leaves', 'soda water', 'sugar syrup', 'white rum']),
                ('Moscow Mule', ['ginger beer', 'lime', 'lime juice', 'vodka']),
                ('Negroni', ['bitters', 'gin', 'sweet vermouth']),
                ('Old Fashioned', ['bitters', 'bourbon', 'orange juice', 'orange slices', 'sugar']),
                ('PG13 Singapore Sling', ['fresh lime juice', 'mango juice', 'mint sprigs', 'pineapple juice', 'pomegranate juice', 'tonic water']),
                ('Penicillin', ['ginger', 'honey simple syrup', 'lemon juice', 'scotch']),
                ('Pina Colada', ['cherries', 'coconut milk', 'cream of coconut', 'dark rum', 'fresh pineapple', 'lime juice', 'white rum']),
                ('Raspberry Almond Soda', ['almonds', 'club soda', 'kosher salt', 'limes', 'ripe raspberries', 'sugar']),
                ('Salted Meyer Lemon and Sage Presse', ['club soda meyer lemons', 'kosher salt', 'sage leaves', 'simple syrup']),
                ('Salted Watermelon Juice', ['cubed watermelon', 'kosher salt', 'lime wedges']),
                ('Shirley Tonic', ['cinnamon sticks', 'club soda', 'ginger', 'lemon twists', 'pomegranate juice', 'sugar', 'whole cloves']),
                ('Shirley ginger', ['brooklyn crafted lemon lime ginger beer', 'club soda', 'grenadine', 'lime juice']),
                ('Spiced Hibiscus Tea', ['cinnamon sticks', 'dried hibiscus flowers', 'ginger', 'honey', 'lemon juice', 'lemon wheels', 'whole allspice']),
                ('Turmeric Tonic', ['agave syrup', 'cayenne pepper', 'lemon', 'peeled ginger', 'peeled turmeric', 'sparkling water']),
                ('Virgin Cucumber Gimlet', [';ime juice', 'club soda', 'muddled cucumber', 'simple syrup']),
                ('Whiskey Sour', ['cherry', 'lemon juice', 'lemon slices', 'superfine sugar', 'whiskey'])
                ]

drink_names = ['Amaretto Sour Cocktail','Aperol Spritz Cocktail','Bannana Punch Mocktail','Beet Sumac Soda Mocktail',
               'Better Than Celery Juice Mocktail','Black & Blue Berries Mocktail','Bloody Mary Cocktail',
               'Bloody Shame Mocktail','Chai Blossom Mocktail','Chile-lime Pineapple Soda Mocktail',
               'Citrus Fizz Mocktail','Dry Martini Cocktail','Espresso Martini Cocktail','Fermented Grape Soda Mocktail',
               'French 75 Cocktail','Gimlet Cocktail','Gin Fizz Cocktail','Huckleberry Shrub Mocktail',
               'Mai Tai Cocktail','Mango Mule Mocktail','Manhattan Cocktail','Maple-Ginger Cider Switchel Mocktail',
               'Margarita Cocktail','Mojito Cocktail','Moscow Mule Cocktail','Negroni Cocktail',
               'Old Fashioned Cocktail','PG13 Singapore Sling Mocktail','Penicillin Cocktail','Pina Colada Cocktail',
               'Raspberry Almond Soda Mocktail','Salted Meyer Lemon and Sage Presse Mocktail',
               'Salted Watermelon Juice Mocktail','Shirley Tonic Mocktail','Shirley ginger Mocktail',
               'Spiced Hibiscus Tea Mocktail','Turmeric Tonic Mocktail','Virgin Cucumber Gimlet Mocktail',
               'Whiskey Sour Cocktail']


#################################
# Data for test_categorize_dish #
#################################

all_dishes = recipes_without_duplicates

dishes_categorized  =  ['Zucchini Fritters with Lemon-Thyme Coconut Yogurt: PALEO',
                        'Winter Cobb Salad: VEGETARIAN',
                        'White Cheddar Scalloped Potatoes: VEGETARIAN',
                        'Walnut Ravioli with Artichokes and Tomatoes: VEGETARIAN',
                        'Waakye: VEGAN',
                        'Vegetarian Khoresh Bademjan: VEGAN',
                        'Vegan Pizza with Caramelized Onions: VEGAN',
                        'Vegan Mini Savory Mince Pies: VEGAN',
                        'Vegan Carbonara: VEGAN',
                        'Sweet and Spicy Crispy Green Beans: VEGAN',
                        'Summer Minestrone Cups: VEGETARIAN',
                        'Sticky Lemon Tofu: VEGAN',
                        'Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole: OMNIVORE',
                        'Shakshuka: VEGAN',
                        'Seared Salmon with Pickled Vegetable and Watercress Salad: KETO',
                        'Seafood Risotto: OMNIVORE',
                        'Satay Steak Skewers: KETO',
                        'Roasted Corn and Zucchini Salad: VEGAN',
                        'Roasted Chicken with Roasted Tomatoes, Avocado, and Sweet Potatoes: PALEO',
                        'Roast Pumpkin and Lentil Salad with Roasted Lemon Dressing: VEGETARIAN',
                        'Roast Leg of Lamb with Crispy Moroccan Carrots & Couscous: OMNIVORE',
                        'Pumpkin Bread Crostini: PALEO',
                        'Prawn and Herb Omelette: KETO',
                        'Pork Chops with Grilled Castelfranco Radicchio and Asparagus: KETO',
                        'Parmesan Crackers and Spinach Crackers with Salmon Pate: KETO',
                        'Nut Wellington: VEGETARIAN',
                        'Mushroom Lasagna: VEGETARIAN',
                        'Lamb over Marinated Summer Squash with Hazelnuts and Ricotta: OMNIVORE',
                        'Kisir with Warm Pita: VEGAN',
                        'Kingfish Lettuce Cups: KETO',
                        'Grilled Tofu Tacos: VEGETARIAN',
                        'Grilled Shrimp and Pesto over Zucchini Noodles: PALEO',
                        'Grilled Pork Chops with Mango Pineapple Salsa: PALEO',
                        'Grilled Flank Steak with Caesar Salad: PALEO',
                        'Grilled Fish Tacos with Cauliflower Tortillas: PALEO',
                        'Governor Shrimp Tacos: OMNIVORE',
                        'Golden Potato Salad: VEGAN',
                        'Georgian Eggplant Rolls with Walnuts: VEGAN',
                        'Fried Zucchini with Balsamic and Chili Dressing: VEGETARIAN',
                        'Fresh Garden Peas over Cauliflower Almond Puree: VEGETARIAN',
                        'Flank Steak with Chimichurri and Asparagus: KETO',
                        'Dahi Puri with Black Chickpeas: OMNIVORE',
                        'Chicken with Tamarind and Apricot Sauce: PALEO',
                        'Cherry Tomato, Watercress and Fava Bean Salad: VEGETARIAN',
                        'Cheela with Spicy Mango Chutney: VEGAN',
                        'Celeriac Schnitzel: VEGAN',
                        'Cauliflower Pizza with Roasted Tomatoes and Chicken: KETO',
                        'Carrot Puff Pastry Tart: VEGAN',
                        'Cambodian-Style Vegetable Spring Rolls: VEGETARIAN',
                        'Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney: KETO',
                        'Burnt Masala Wings with Classic Coleslaw: OMNIVORE',
                        'Burmese Tofu with Garlic, Ginger and Chili Sauce: VEGAN',
                        'Brisket with Grilled Rhubarb, Onions, and Fennel: OMNIVORE',
                        'Braised Pork Belly with Apple Salad: KETO',
                        'BLT Bites: PALEO',
                        'Beachside Snapper: OMNIVORE',
                        'Barley Risotto: VEGETARIAN',
                        'Baked Kelewele: VEGAN',
                        'Baked Chicken Jollof Rice: OMNIVORE',
                        'Avocado Deviled Eggs: PALEO',
                        'Asparagus Puffs: VEGETARIAN']


#########################################
# Data for test_tag_special_ingredients #
#########################################


dupes =  ['Baked Kelewele', 'Barley Risotto', 'Burmese Tofu with Garlic, Ginger and Chili Sauce',
          'Cambodian-Style Vegetable Spring Rolls', 'Fried Zucchini with Balsamic and Chili Dressing',
          'Kisir with Warm Pita', 'Shakshuka', 'Summer Minestrone Cups', 'Vegetarian Khoresh Bademjan']

nondupes = ['Brisket with Grilled Rhubarb, Onions, and Fennel', 'Burnt Masala Wings with Classic Coleslaw',
            'Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney',
            'Cauliflower Pizza with Roasted Tomatoes and Chicken', 'Dahi Puri with Black Chickpeas',
            'Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
            'Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole']

group_1 = [item for item in recipes_with_duplicates if item[0] in dupes]
group_2 = [(item[1], item[2]) for item in recipes_without_duplicates if item[1] in nondupes]

dishes_to_special_label = sorted(group_1 + group_2)

dishes_labeled =  [('Baked Kelewele', {'red onion'}),
                   ('Barley Risotto', {'garlic', 'red onion', 'parmesan cheese'}),
                   ('Brisket with Grilled Rhubarb, Onions, and Fennel', {'soy sauce', 'garlic', 'red onion', 'yellow onion'}),
                   ('Burmese Tofu with Garlic, Ginger and Chili Sauce', {'soy sauce', 'garlic', 'peanuts'}),
                   ('Burnt Masala Wings with Classic Coleslaw', {'honey', 'butter', 'garlic cloves'}),
                   ('Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney', {'heavy cream', 'garlic', 'butter', 'tomatoes'}),
                   ('Cambodian-Style Vegetable Spring Rolls', {'soy sauce', 'firm tofu', 'garlic', 'toasted peanuts'}),
                   ('Cauliflower Pizza with Roasted Tomatoes and Chicken', {'parmesan', 'mozzarella cheese', 'tomato paste', 'cherry tomatoes', 'eggs'}),
                   ('Dahi Puri with Black Chickpeas', {'red onion', 'whole-milk yogurt'}),
                   ('Flank Steak with Chimichurri and Asparagus', {'garlic'}),
                   ('Fried Zucchini with Balsamic and Chili Dressing', {'honey', 'garlic', 'red onion'}),
                   ('Kingfish Lettuce Cups', {'soy sauce', 'oyster sauce', 'garlic', 'grilled king fish'}),
                   ('Kisir with Warm Pita', {'bulgur', 'tomato paste'}),
                   ('Shakshuka', {'tomatoes', 'tomato paste', 'firm tofu', 'yellow onion'}),
                   ('Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', {'shrimp', 'garlic', 'butter', 'slivered almonds', 'bacon'}),
                   ('Summer Minestrone Cups', {'garlic', 'tomatoes', 'parmesan cheese'}),
                   ('Vegetarian Khoresh Bademjan', {'slivered almonds', 'tomato paste'})]


#####################################
# Data for test_compile_ingredients #
#####################################


ingredients_only = [[{'bulgur', 'pomegranate molasses', 'chopped parsley', 'lemon juice', 'tomato', 'persian cucumber', 'tomato paste', 'spring onion', 'water', 'olive oil'},
                     {'vegan unsweetened yoghurt', 'yellow onion', 'firm tofu', 'smoked paprika', 'tomatoes', 'tomato paste', 'sugar', 'cloves', 'cumin', "za'atar", 'olive oil', 'harissa', 'red bell pepper'},
                     {'yellow split peas', 'tomato paste', 'black pepper', 'pomegranate concentrate', 'yellow onions', 'slivered almonds', 'ground turmeric', 'barberries', 'basmati rice', 'lemon juice', 'hot water', 'cayenne pepper', 'chinese eggplants', 'salt', 'orange juice', 'saffron powder', 'vegan butter', 'orange zest', 'kosher salt'},
                     {'smoked paprika', 'black peppercorn', 'red onion', 'grains of selim', 'cayenne pepper', 'calabash nutmeg', 'coconut oil', 'cloves', 'fresh ginger', 'salt', 'ripe plantains'},
                     {'baking soda', 'sorghum stems', 'coconut oil', 'black-eyed peas', 'water', 'salt', 'white rice'},
                     {'pomegranate seeds', 'oil', 'coriander', 'garlic', 'khmeli suneli', 'eggplants', 'black pepper', 'vinegar', 'walnuts', 'water', 'salt'},
                     {'soy sauce', 'oil', 'chili flakes', 'garlic', 'brown sugar', 'ginger', 'peanuts', 'rice vinegar', 'spring onions', 'water', 'turmeric', 'salt', 'chickpea flour'},
                     {'soy sauce', 'parsley', 'lemon', 'sunflower oil', 'black pepper', 'celeriac', 'breadcrumbs', 'water', 'salt', 'flour', 'chickpea flour'},
                     {'soy sauce', 'vegetable stock', 'tofu', 'cornstarch', 'lemon juice', 'lemon zest', 'garlic', 'ginger', 'black pepper', 'sugar', 'water', 'salt', 'vegetable oil'},
                     {'soy sauce', 'smoked tofu', 'lemon juice', 'nutritional yeast', 'mixed herbs', 'garlic', 'black pepper', 'silken tofu', 'turmeric', 'salt', 'olive oil', 'spaghetti'},
                     {'mushrooms', 'rosemary', 'garlic', 'red pepper flakes', 'yeast', 'barley malt', 'water', 'olive oil', 'garlic powder', 'oregano', 'honey', 'nutritional yeast', 'red onion', 'tomatoes', 'cashews', 'sugar', 'bell pepper', 'flour', 'salt', 'fresh basil'},
                     {'clove powder', 'oil', 'cinnamon powder', 'nigella seeds', 'curry leaves', 'coriander seeds', 'garlic', 'mangoes', 'mashed potatoes', 'cardamom powder', 'vinegar', 'water', 'mustard seeds', 'coriander powder', 'cumin powder', 'mango powder', 'garam masala', 'red chili powder', 'hing', 'garlic paste', 'turmeric powder', 'cilantro', 'sugar', 'onion', 'serrano chili', 'fresh ginger', 'turmeric', 'salt', 'fresh red chili', 'chickpea flour'},
                     {'soy sauce', 'pomegranate molasses', 'sesame oil', 'green beans', 'sunflower oil', 'scallions', 'garlic', 'carrot', 'ginger', 'sesame seeds', 'tomato paste', 'bell pepper', 'siracha'},
                     {'mushrooms', 'cinnamon powder', 'rosemary', 'corn flour', 'ginger', 'brown sugar', 'carrot', 'black pepper', 'raisins', 'butternut squash', 'vegetarian worcestershire sauce', 'parev shortcrust pastry', 'olive oil', 'vegetable stock', 'dried cherries', 'lemon juice', 'lemon zest', 'figs', 'dried cranberries', 'apples', 'pecans', 'onion', 'orange juice', 'currants', 'dried blueberries', 'salt', 'brandy', 'orange zest', 'allspice powder'},
                     {'green onions', 'lemon juice', 'lemon zest', 'dill', 'corn', 'tomatoes', 'black pepper', 'zucchini', 'olive oil'},
                     {'mustard seeds', 'cumin seeds', 'lemon juice', 'garlic', 'black pepper', 'balsamic vinegar', 'yukon gold potato', 'chives', 'turmeric', 'salt', 'olive oil'},
                     {'olive oil', 'lemon', 'lemon juice', 'pareve puff pastry', 'brown sugar', 'red onion', 'carrot', 'garlic', 'black pepper', 'thyme', 'vegan butter', 'water', 'salt', 'ground almonds'}
                     ],

                     [{'nutmeg', 'garlic', 'black pepper', 'onions', 'butter', 'parmesan cheese', 'portobello mushrooms', 'flour', 'dried lasagna noodles', 'olive oil', 'milk', 'kosher salt'},
                     {'sage', 'puff pastry sheets', 'hazelnuts', 'almonds', 'black pepper', 'thyme', 'marmite', 'breadcrumbs', 'walnuts', 'dates', 'eggs', 'olive oil', 'brazil nuts', 'leeks', 'chestnuts', 'cashews', 'apples', 'pecans', 'butter', 'salt'},
                     {'shallots', 'garlic', 'cream', 'thyme', 'breadcrumbs', 'sharp white cheddar', 'yukon gold potato', 'milk', 'kosher salt'},
                     {'smoked tofu', 'shiitake mushrooms', 'red wine vinegar', 'garlic', 'tomatoes', 'black pepper', 'avocados', 'blue cheese', 'onion', 'lacinato kale', 'eggs', 'olive oil'},
                     {'honey', 'lemon', 'dijon mustard', 'feta cheese', 'red wine vinegar', 'red onion', 'watercress', 'green lentils', 'currants', 'capers', 'pepitas', 'fresh pumpkin', 'olive oil'},
                     {'lime juice', 'toasted peanuts', 'firm tofu', 'garlic', 'corn flour', 'bean sprouts', 'carrot', 'palm sugar', 'shallots', 'red chili', 'vermicelli noodles', 'wombok', 'soy sauce', 'sunflower oil', 'spring roll wrappers', 'vegetarian fish sauce'},
                     {'fresh peas', 'rosemary', 'garlic', 'chickpeas', 'carrot', 'leek', 'green lentils', 'red chili', 'olive oil', 'croutons', 'fresh corn', 'lemon zest', 'green beans', 'parmesan rind', 'basil', 'tomatoes', 'vegetable bullion', 'parmesan cheese', 'celery', 'mint'},
                     {'honey', 'lemon juice', 'garlic', 'red onion', 'red thai chili', 'pomegranate', 'balsamic vinegar', 'mint leaves', 'zucchini', 'olive oil'},
                     {'sage', 'beets', 'pearl barley', 'brussel sprouts', 'rosemary', 'garlic', 'carrot', 'red onion', 'black pepper', 'thyme', 'butternut squash', 'vegetable bullion', 'parmesan cheese', 'olive oil', 'white wine'},
                     {'fresh peas', 'fresh cherry tomatoes', 'garlic', 'watercress', 'balsamic vinegar', 'fresh or frozen fava beans', 'fresh cherry bocconcini', 'salt', 'olive oil'},
                     {'red onions', 'lemon', 'fresh peas', 'garlic', 'grated nutmeg', 'cream', 'cauliflower', 'blanched almonds', 'fresh pea tendrils', 'olive oil', 'vegetable oil'},
                     {'pine nuts', 'oil marinated artichokes', 'olives', 'rosemary', 'fresh tomatoes', 'ricotta cheese', 'black pepper', 'fresh artichoke hearts', 'walnuts', 'pasta sheets', 'lemon juice', 'lemon zest', 'basil', 'red onion', 'butter', 'salt'},
                     {'egg', 'asparagus', 'lemon juice', 'red onion', 'ricotta cheese', 'black pepper', 'thyme', 'salt', 'parmesan cheese', 'puff pastry', 'chives'},
                     {'cotija cheese', 'masa', 'fresh cilantro leaves', 'jalapeño chili', 'chipotle chili', 'firm tofu', 'garlic', 'carrot', 'roasted corn', 'tomatillos', 'pepitas', 'ancho chili', 'crema', 'red onions', 'pasilla chili', 'lemon', 'hot water', 'lemon juice', 'tomatoes', 'avocado', 'cumin', 'red cabbage', 'limes', 'black beans'}
                     ],

                     [{'baking soda', 'coconut flour', 'lemon juice', 'lemon zest', 'eggs', 'coconut yogurt', 'black pepper', 'fresh thai chili', 'coconut oil', 'chives', 'zucchini', 'salt'},
                     {'lime juice', 'fresh cilantro leaves', 'eggs', 'seranno chili', 'avocado', 'pepitas', 'salt', 'garlic powder'},
                     {'pine nuts', 'white vinegar', 'chipotle chili', 'scallions', 'garlic', 'paleo parmesan cheese', 'black pepper', 'avocado oil', 'treviso', 'olive oil', 'radishes', 'flank steak', 'dijon mustard', 'castelfranco radicchio', 'worcestershire sauce', 'fresh parsley', 'cherry tomatoes', 'salt', 'avocado mayonnaise'},
                     {'coconut flour', 'garlic', 'black pepper', 'cloves', 'eggs', 'olive oil', 'onions', 'honey', 'apple cider vinegar', 'almond butter', 'baking soda', 'nutmeg', 'pumpkin puree', 'cinnamon', 'shrimp', 'basil', 'coconut oil', 'cherry tomatoes', 'salt', 'fresh red chili'},
                     {'mustard seed', 'onion', 'kale', 'cherry tomatoes', 'bacon', 'paleo mayonnaise'},
                     {'purple sweet potato', 'chiles de árbol', 'garlic', 'tomatoes', 'safflower oil', 'black pepper', 'mexican oregano', 'avocados', 'shallots', 'cumin', 'olive oil', 'lemons', 'whole chicken', 'limes', 'kosher salt'},
                     {'garlic', 'black pepper', 'dried apricots', 'roma tomatoes', 'water', 'olive oil', 'honey', 'cinnamon', 'ground cumin', 'cider vinegar', 'chili powder', 'safflower oil', 'homemade tamarind concentrate', 'white chicken', 'allspice', 'chipotles', 'salt', 'homemade apricot honey preserves', 'kosher salt'},
                     {'green onions', 'serrano chili', 'shredded red cabbage', 'smoked paprika', 'mango', 'eggs', 'black pepper', 'cilantro', 'cauliflower', 'avocado', 'lime', 'cumin', 'salt', 'tilapia'},
                     {'cilantro leaves', 'lime', 'pineapple', 'chipotle chili', 'garlic', 'mangoes', 'cauliflower', 'avocado', 'serrano chili', 'pork chops', 'lime zest', 'lacinato kale', 'onions'},
                     {'pine nuts', 'shrimp', 'green bell pepper', 'lemon juice', 'basil', 'lemon zest', 'garlic', 'tomatoes', 'cashews', 'yellow bell pepper', 'cumin', 'zucchini', 'salt', 'olive oil', 'red bell pepper'}
                     ],

                     [{'parmesan', 'almond meal', 'rosemary', 'mozzarella cheese', 'roasted chicken', 'tomato paste', 'cauliflower', 'cherry tomatoes', 'eggs', 'fresh basil', 'olive oil'},
                     {'white vinegar', 'asparagus', 'flank steak', 'chipotle chili', 'scallions', 'garlic', 'black pepper', 'cauliflower', 'sour cream', 'fresh parsley', 'salt', 'olive oil'},
                     {'soy sauce', 'watermelon radishes', 'lime juice', 'fish sauce', 'mirin', 'little gem lettuce heads', 'peanut oil', 'garlic', 'sesame seeds', 'oyster sauce', 'spring onions', 'avocado', 'grilled king fish', 'red cabbage'},
                     {'clove powder', 'curry leaves', 'coriander seeds', 'ginger', 'cardamom powder', 'vinegar', 'mustard seeds', 'mango powder', 'garam masala', 'red chili powder', 'chicken', 'hing', 'turmeric powder', 'tomatoes', 'ginger garlic paste', 'fresh greek yogurt', 'fresh ginger', 'monk fruit', 'turmeric', 'cashew nuts', 'salt', 'fresh red chili', 'cinnamon powder', 'nigella seeds', 'whole small crimini mushrooms', 'brussel sprouts', 'garlic', 'mangoes', 'heavy cream', 'cloves', 'coriander powder', 'cumin powder', 'cardamom', 'green chili', 'cinnamon', 'garlic paste', 'red chili flakes', 'lemon juice', 'cilantro', 'butter', 'dried fenugreek leaves', 'boned chicken'},
                     {'green onions', 'parsley', 'sesame seeds', 'black pepper', 'chives', 'eggs', 'fennel bulb', 'tahini', 'olive oil', 'harissa', 'shrimp', 'lemon juice', 'dill', 'butter', 'onion', 'fresh cucumber', 'monk fruit', 'salt'},
                     {'sriacha', 'apple cider vinegar', 'lime juice', 'fish sauce', 'red and green thai chili', 'flank steak', 'carrot', 'peanuts', 'cucumbers', 'roasted peanuts', 'crunchy peanut butter', 'kecap manis', 'monk fruit', 'micro cilantro', 'olive oil'},
                     {'spinach', 'parmesan cheese', 'coconut flour', 'chili flakes', 'garlic', 'black pepper', 'cream cheese', 'ghee', 'lemon juice', 'flaxmeal', 'red onion', 'salt', 'salmon fillets', 'pecans', 'almond flour', 'cumin', 'fresh cucumber', 'cherry tomatoes', 'chives', 'avocado mayonnaise'},
                     {'rosemary', 'garlic', 'black pepper', 'thyme', 'avocado oil', 'eggs', 'oregano', 'asparagus', 'lemon', 'dijon mustard', 'basil', 'castelfranco radicchio', 'dill', 'butter', 'pork chops', 'monk fruit', 'salt', 'avocado mayonnaise'},
                     {'lime juice', 'caster sugar', 'toasted buckwheat', 'lemon juice', 'red wine vinegar', 'red onion', 'dutch carrot', 'salmon steaks', 'watercress', 'pink peppercorns', 'shallots', 'fennel seeds', 'red cabbage', 'radishes'},
                     {'cilantro leaves', 'green cabbage', 'lemon juice', 'pork belly', 'dark soy sauce', 'granny smith apples', 'ginger', 'light soy sauce', 'sesame seeds', 'black pepper', 'cinnamon sticks', 'spring onions', 'star anise', 'monk fruit', 'olive oil'}
                     ],

                     [{'lime juice', 'salsa', 'green bell pepper', 'anaheim chili', 'black pepper', 'olive oil', 'yellow mustard', 'red bell pepper', 'soy sauce', 'mexican crema', 'mayonnaise', 'white onion', 'garlic cloves', 'fresh corn tortillas', 'red onion', 'tomatoes', 'limes', 'worcestershire sauce', 'butter', 'yellow bell pepper', 'salt', 'red snapper'},
                     {'lime juice', 'poblano chili', 'tomato paste', 'black pepper', 'chipotle adobo sauce', 'chile manzano', 'roma tomatoes', 'pepitas', 'oaxaca cheese', 'white onion', 'shelled large shrimp', 'garlic cloves', 'fresh corn tortillas', 'red onion', 'worcestershire sauce', 'avocado', 'butter', 'kosher salt'},
                     {'fresh tortillas', 'shrimp', 'garlic', 'chickpeas', 'black pepper', 'slivered almonds', 'guajillo chile', 'bacon', 'sea salt', 'butter', 'onion', 'avocado', 'olive oil'},
                     {'lime juice', 'green cabbage', 'chiles de árbol', 'green cardamom', 'ginger', 'carrot', 'sriracha', 'black pepper', 'cinnamon sticks', 'celery seeds', 'cloves', 'black cardamom', 'olive oil', 'chicken wings', 'apple cider vinegar', 'mayonnaise', 'honey', 'black peppercorns', 'lemon juice', 'garlic cloves', 'tamarind concentrate', 'cilantro', 'butter', 'serrano chili', 'red cabbage', 'kosher salt'},
                     {'whole-milk yogurt', 'chaat masala', 'ginger', 'pani puri', 'scallion chutney', 'yukon gold potato', 'black chickpeas', 'thin sev', 'date syrup', 'red onion', 'roasted chicken', 'chili powder', 'tamarind concentrate', 'cumin', 'turmeric', 'mint'},
                     {'white vinegar', 'parsley', 'yellow onion', 'rhubarb', 'garlic', 'brown sugar', 'black pepper', 'thyme', 'crushed red pepper flakes', 'fennel bulbs', 'beer', 'marjoram', 'vegetable oil', 'soy sauce', 'oregano', 'lemon', 'red onion', 'chili powder', 'cilantro', 'beef brisket', 'balsamic vinegar', 'worcestershire sauce', 'celery', 'mint', 'kosher salt'},
                     {'oranges', 'rosemary', 'garlic', 'anchovy fillets', 'couscous', 'carrot', 'sesame seeds', 'fresh thyme', 'vinegar', 'olive oil', 'tahini', 'harissa', 'onions', 'honey', 'fresh mint', 'leg of lamb', 'tomatoes', 'baby carrot', 'vegetable bullion', 'filo pastry', 'celery', 'bay leaves', 'yoghurt'},
                     {'tomato puree', 'garlic', 'ginger', 'tomato', 'carrot', 'thyme', 'white pepper', 'water', 'maggi cubes', 'chicken', 'rice', 'coriander', 'scotch bonnet pepper', 'bell pepper', 'onion', 'turmeric', 'salt'},
                     {'garlic', 'tomato paste', 'baby scallops', 'mussels', 'water', 'crab legs', 'olive oil', 'baby squid', 'fish stock', 'lemon juice', 'white onion', 'arborio risotto rice', 'clams', 'parmesan cheese', 'flat-leaf parsley', 'cherry tomatoes', 'prawns', 'white wine'},
                     {'toasted bread', 'rosemary', 'hazelnuts', 'anchovy fillets', 'garlic', 'carrot', 'summer squash', 'black pepper', 'red pepper flakes', 'vinegar', 'sea salt', 'zucchini', 'olive oil', 'onions', 'white wine vinegar', 'fresh mint', 'leg of lamb', 'lemon', 'fresh ricotta', 'sugar', 'celery', 'bay leaves', 'kosher salt'}
                     ]]


#####################################
# Data for test_separate_appetizers #
#####################################


vegan = ['Kisir with Warm Pita', 'Shakshuka', 'Vegetarian Khoresh Bademjan', 'Baked Kelewele', 'Waakye', 'Georgian Eggplant Rolls with Walnuts', 'Burmese Tofu with Garlic, Ginger and Chili Sauce', 'Celeriac Schnitzel', 'Sticky Lemon Tofu', 'Vegan Carbonara', 'Vegan Pizza with Caramelized Onions', 'Cheela with Spicy Mango Chutney', 'Sweet and Spicy Crispy Green Beans', 'Vegan Mini Savory Mince Pies', 'Roasted Corn and Zucchini Salad', 'Golden Potato Salad', 'Carrot Puff Pastry Tart', 'Kisir with Warm Pita', 'Baked Kelewele', 'Burmese Tofu with Garlic, Ginger and Chili Sauce', 'Vegan Carbonara', 'Sweet and Spicy Crispy Green Beans', 'Golden Potato Salad']
vegan_appetizers = ['Georgian Eggplant Rolls with Walnuts', 'Cheela with Spicy Mango Chutney', 'Vegan Mini Savory Mince Pies', 'Carrot Puff Pastry Tart', 'Georgian Eggplant Rolls with Walnuts', 'Carrot Puff Pastry Tart']
vegan_dishes = ['Golden Potato Salad', 'Roasted Corn and Zucchini Salad', 'Sticky Lemon Tofu', 'Shakshuka', 'Burmese Tofu with Garlic, Ginger and Chili Sauce', 'Vegan Pizza with Caramelized Onions', 'Celeriac Schnitzel', 'Waakye', 'Vegan Carbonara', 'Sweet and Spicy Crispy Green Beans', 'Vegetarian Khoresh Bademjan', 'Baked Kelewele', 'Kisir with Warm Pita']
vegan_appetizer_names = ['Georgian Eggplant Rolls with Walnuts','Cheela with Spicy Mango Chutney','Vegan Mini Savory Mince Pies','Carrot Puff Pastry Tart']


vegetarian = ['Mushroom Lasagna', 'Nut Wellington', 'Roast Pumpkin and Lentil Salad with Roasted Lemon Dressing', 'Cambodian-Style Vegetable Spring Rolls', 'Summer Minestrone Cups', 'Fried Zucchini with Balsamic and Chili Dressing', 'Barley Risotto', 'Cherry Tomato, Watercress and Fava Bean Salad', 'Fresh Garden Peas over Cauliflower Almond Puree', 'Walnut Ravioli with Artichokes and Tomatoes', 'Asparagus Puffs', 'Grilled Tofu Tacos', 'Mushroom Lasagna', 'Cambodian-Style Vegetable Spring Rolls', 'Barley Risotto', 'Walnut Ravioli with Artichokes and Tomatoes']
vegetarian_appetizers = ['Cambodian-Style Vegetable Spring Rolls', 'Summer Minestrone Cups', 'Asparagus Puffs', 'Grilled Tofu Tacos', 'Cambodian-Style Vegetable Spring Rolls', 'Grilled Tofu Tacos']
vegetarian_dishes = ['Walnut Ravioli with Artichokes and Tomatoes', 'Mushroom Lasagna', 'Fried Zucchini with Balsamic and Chili Dressing', 'Barley Risotto', 'Nut Wellington', 'Cherry Tomato, Watercress and Fava Bean Salad', 'Roast Pumpkin and Lentil Salad with Roasted Lemon Dressing', 'Fresh Garden Peas over Cauliflower Almond Puree']
vegetarian_appetizer_names = ['Cambodian-Style Vegetable Spring Rolls','Summer Minestrone Cups','Asparagus Puffs','Grilled Tofu Tacos']


paleo = ['Zucchini Fritters with Lemon-Thyme Coconut Yogurt', 'Avocado Deviled Eggs', 'Grilled Flank Steak with Caesar Salad', 'Pumpkin Bread Crostini', 'BLT Bites', 'Roasted Chicken with Roasted Tomatoes, Avocado, and Sweet Potatoes', 'Chicken with Tamarind and Apricot Sauce', 'Grilled Fish Tacos with Cauliflower Tortillas', 'Grilled Pork Chops with Mango Pineapple Salsa', 'Grilled Shrimp and Pesto over Zucchini Noodles', 'Zucchini Fritters with Lemon-Thyme Coconut Yogurt', 'Pumpkin Bread Crostini', 'Chicken with Tamarind and Apricot Sauce', 'Grilled Shrimp and Pesto over Zucchini Noodles']
paleo_appetizers = ['Zucchini Fritters with Lemon-Thyme Coconut Yogurt', 'Avocado Deviled Eggs', 'Pumpkin Bread Crostini', 'BLT Bites', 'Zucchini Fritters with Lemon-Thyme Coconut Yogurt', 'BLT Bites']
paleo_dishes = ['Roasted Chicken with Roasted Tomatoes, Avocado, and Sweet Potatoes', 'Grilled Flank Steak with Caesar Salad', 'Grilled Fish Tacos with Cauliflower Tortillas', 'Grilled Pork Chops with Mango Pineapple Salsa', 'Grilled Shrimp and Pesto over Zucchini Noodles', 'Chicken with Tamarind and Apricot Sauce']
paleo_appetizer_names = ['Zucchini Fritters with Lemon-Thyme Coconut Yogurt','Avocado Deviled Eggs','Pumpkin Bread Crostini','BLT Bites']


keto = ['Cauliflower Pizza with Roasted Tomatoes and Chicken', 'Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups', 'Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney', 'Prawn and Herb Omelette', 'Satay Steak Skewers', 'Parmesan Crackers and Spinach Crackers with Salmon Pate', 'Pork Chops with Grilled Castelfranco Radicchio and Asparagus', 'Seared Salmon with Pickled Vegetable and Watercress Salad', 'Braised Pork Belly with Apple Salad', 'Cauliflower Pizza with Roasted Tomatoes and Chicken', 'Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney', 'Parmesan Crackers and Spinach Crackers with Salmon Pate', 'Braised Pork Belly with Apple Salad']
keto_appetizers = ['Kingfish Lettuce Cups', 'Prawn and Herb Omelette', 'Satay Steak Skewers', 'Parmesan Crackers and Spinach Crackers with Salmon Pate', 'Kingfish Lettuce Cups', 'Parmesan Crackers and Spinach Crackers with Salmon Pate']
keto_dishes = ['Cauliflower Pizza with Roasted Tomatoes and Chicken', 'Butter Chicken with Grilled Mushrooms, Brussel Sprouts and Mango Chutney', 'Braised Pork Belly with Apple Salad', 'Seared Salmon with Pickled Vegetable and Watercress Salad', 'Pork Chops with Grilled Castelfranco Radicchio and Asparagus', 'Flank Steak with Chimichurri and Asparagus']
keto_appetizer_names = ['Kingfish Lettuce Cups','Prawn and Herb Omelette','Satay Steak Skewers','Parmesan Crackers and Spinach Crackers with Salmon Pate']


omnivore = ['Beachside Snapper', 'Governor Shrimp Tacos', 'Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', 'Burnt Masala Wings with Classic Coleslaw', 'Dahi Puri with Black Chickpeas', 'Brisket with Grilled Rhubarb, Onions, and Fennel', 'Roast Leg of Lamb with Crispy Moroccan Carrots & Couscous', 'Baked Chicken Jollof Rice', 'Seafood Risotto', 'Lamb over Marinated Summer Squash with Hazelnuts and Ricotta', 'Beachside Snapper', 'Burnt Masala Wings with Classic Coleslaw', 'Roast Leg of Lamb with Crispy Moroccan Carrots & Couscous', 'Lamb over Marinated Summer Squash with Hazelnuts and Ricotta']
omnivore_appetizers = ['Governor Shrimp Tacos', 'Burnt Masala Wings with Classic Coleslaw', 'Dahi Puri with Black Chickpeas', 'Seafood Risotto', 'Governor Shrimp Tacos', 'Seafood Risotto']
omnivore_dishes = ['Lamb over Marinated Summer Squash with Hazelnuts and Ricotta', 'Shrimp, Bacon and Crispy Chickpea Tacos with Salsa de Guacamole', 'Brisket with Grilled Rhubarb, Onions, and Fennel', 'Roast Leg of Lamb with Crispy Moroccan Carrots & Couscous', 'Beachside Snapper', 'Baked Chicken Jollof Rice']
omnivore_appetizer_names = ['Governor Shrimp Tacos','Burnt Masala Wings with Classic Coleslaw','Dahi Puri with Black Chickpeas','Seafood Risotto']


dishes_and_appetizers = ((vegan, vegan_appetizers),
                         (vegetarian, vegetarian_appetizers),
                         (paleo, paleo_appetizers),
                         (keto, keto_appetizers),
                         (omnivore, omnivore_appetizers)
                        )

dishes_cleaned = (vegan_dishes,
                  vegetarian_dishes,
                  paleo_dishes,
                  keto_dishes,
                  omnivore_dishes
                  )


#######################################
# Data for test_singleton_ingredients #
#######################################


intersections = (VEGAN_INTERSECTIONS, VEGETARIAN_INTERSECTIONS, PALEO_INTERSECTIONS,
                 KETO_INTERSECTIONS, OMNIVORE_INTERSECTIONS)

dishes_and_overlap = [(item[0], item[1]) for item in zip(ingredients_only, intersections)]
ingredients = (set.union(*group) for group in ingredients_only)
singletons  = (item[0] ^ item[1] for item in zip(ingredients, intersections))

backup_singletons = [{'black-eyed peas', 'coriander', 'cashews', 'yellow split peas', 'pomegranate seeds', 'cumin', 'mangoes', 'pomegranate concentrate', 'red chili powder', 'slivered almonds', 'black peppercorn', 'cornstarch', 'smoked tofu', 'curry leaves', 'zucchini', 'currants', 'dried cranberries', 'yukon gold potato', 'tofu', 'yeast', 'fresh basil', 'hot water', 'ripe plantains', 'calabash nutmeg', 'green beans', 'kosher salt', 'grains of selim', 'vegetarian worcestershire sauce', 'cumin seeds', 'figs', 'ground turmeric', 'white rice', 'harissa', 'garlic powder', 'scallions', 'barberries', 'walnuts', 'basmati rice', 'saffron powder', 'butternut squash', 'thyme', 'tomato', 'chopped parsley', 'hing', 'coriander seeds', 'turmeric powder', 'eggplants', 'sesame oil', "za'atar", 'pareve puff pastry', 'firm tofu', 'yellow onions', 'coriander powder', 'parsley', 'garlic paste', 'rice vinegar', 'sorghum stems', 'spring onions', 'raisins', 'chinese eggplants', 'garam masala', 'ground almonds', 'baking soda', 'clove powder', 'allspice powder', 'parev shortcrust pastry', 'dill', 'nigella seeds', 'dried blueberries', 'cardamom powder', 'cilantro', 'serrano chili', 'breadcrumbs', 'mango powder', 'dried cherries', 'oregano', 'fresh red chili', 'pecans', 'chives', 'spaghetti', 'mixed herbs', 'brandy', 'cumin powder', 'silken tofu', 'yellow onion', 'balsamic vinegar', 'persian cucumber', 'red bell pepper', 'peanuts', 'siracha', 'red pepper flakes', 'spring onion', 'vegan unsweetened yoghurt', 'corn', 'khmeli suneli', 'barley malt', 'green onions', 'apples', 'corn flour', 'honey', 'celeriac', 'bulgur', 'sesame seeds', 'mashed potatoes', 'chili flakes', 'vegetable oil'},
{'vegetarian fish sauce', 'cashews', 'white wine', 'portobello mushrooms', 'marmite', 'dates', 'tomatillos', 'cumin', 'chestnuts', 'beets', 'masa', 'mint', 'smoked tofu', 'fresh pea tendrils', 'puff pastry sheets', 'zucchini', 'currants', 'hazelnuts', 'croutons', 'pearl barley', 'dijon mustard', 'yukon gold potato', 'fresh tomatoes', 'vermicelli noodles', 'fresh cherry tomatoes', 'celery', 'hot water', 'green beans', 'grated nutmeg', 'roasted corn', 'palm sugar', 'ancho chili', 'fresh corn', 'spring roll wrappers', 'cotija cheese', 'parmesan rind', 'pasta sheets', 'brazil nuts', 'cauliflower', 'butternut squash', 'mint leaves', 'fresh cherry bocconcini', 'crema', 'blue cheese', 'chickpeas', 'pasilla chili', 'black beans', 'wombok', 'capers', 'pine nuts', 'egg', 'shiitake mushrooms', 'red thai chili', 'jalapeño chili', 'toasted peanuts', 'brussel sprouts', 'lime juice', 'leeks', 'flour', 'dried lasagna noodles', 'onions', 'limes', 'chipotle chili', 'lacinato kale', 'fresh pumpkin', 'almonds', 'olives', 'onion', 'fresh artichoke hearts', 'leek', 'pecans', 'chives', 'blanched almonds', 'nutmeg', 'fresh or frozen fava beans', 'soy sauce', 'avocados', 'bean sprouts', 'asparagus', 'feta cheese', 'sharp white cheddar', 'apples', 'sunflower oil', 'corn flour', 'avocado', 'puff pastry', 'red cabbage', 'pomegranate', 'fresh cilantro leaves', 'oil marinated artichokes', 'vegetable oil'},
{'treviso', 'cashews', 'mexican oregano', 'pumpkin puree', 'purple sweet potato', 'homemade apricot honey preserves', 'apple cider vinegar', 'homemade tamarind concentrate', 'paleo parmesan cheese', 'pineapple', 'green bell pepper', 'chipotles', 'nutmeg', 'ground cumin', 'coconut yogurt', 'kale', 'mangoes', 'red bell pepper', 'dried apricots', 'garlic powder', 'pepitas', 'white vinegar', 'scallions', 'avocados', 'shredded red cabbage', 'smoked paprika', 'lime juice', 'flank steak', 'fresh parsley', 'shallots', 'chiles de árbol', 'yellow bell pepper', 'white chicken', 'whole chicken', 'chili powder', 'bacon', 'avocado mayonnaise', 'cilantro', 'limes', 'lemons', 'green onions', 'avocado oil', 'cloves', 'lacinato kale', 'lime zest', 'paleo mayonnaise', 'radishes', 'mango', 'dijon mustard', 'mustard seed', 'cider vinegar', 'pork chops', 'castelfranco radicchio', 'water', 'allspice', 'seranno chili', 'cilantro leaves', 'onion', 'tilapia', 'fresh cilantro leaves', 'worcestershire sauce', 'almond butter', 'fresh thai chili', 'fresh red chili', 'chives', 'roma tomatoes'},
{'dried fenugreek leaves', 'apple cider vinegar', 'cinnamon sticks', 'roasted chicken', 'cumin', 'mangoes', 'heavy cream', 'micro cilantro', 'white vinegar', 'red chili powder', 'cinnamon powder', 'mustard seeds', 'red wine vinegar', 'mirin', 'cinnamon', 'green chili', 'avocado oil', 'curry leaves', 'star anise', 'dijon mustard', 'crunchy peanut butter', 'grilled king fish', 'chicken', 'fresh basil', 'cashew nuts', 'pink peppercorns', 'pork belly', 'spinach', 'watercress', 'whole small crimini mushrooms', 'coconut flour', 'fresh ginger', 'fennel bulb', 'harissa', 'tahini', 'mozzarella cheese', 'scallions', 'sriacha', 'fresh parsley', 'thyme', 'light soy sauce', 'cream cheese', 'hing', 'coriander seeds', 'sour cream', 'turmeric powder', 'castelfranco radicchio', 'parmesan', 'toasted buckwheat', 'coriander powder', 'dark soy sauce', 'granny smith apples', 'parsley', 'shrimp', 'garlic paste', 'roasted peanuts', 'turmeric', 'carrot', 'garam masala', 'clove powder', 'cucumbers', 'tomato paste', 'almond meal', 'dutch carrot', 'brussel sprouts', 'red and green thai chili', 'shallots', 'nigella seeds', 'cardamom powder', 'watermelon radishes', 'flaxmeal', 'cilantro', 'fennel seeds', 'chipotle chili', 'ghee', 'parmesan cheese', 'radishes', 'pork chops', 'cilantro leaves', 'fresh greek yogurt', 'cardamom', 'mango powder', 'onion', 'oregano', 'fresh red chili', 'pecans', 'salmon fillets', 'basil', 'green cabbage', 'cumin powder', 'almond flour', 'lemon', 'boned chicken', 'oyster sauce', 'soy sauce', 'little gem lettuce heads', 'peanut oil', 'peanuts', 'caster sugar', 'salmon steaks', 'ginger garlic paste', 'green onions', 'vinegar', 'cloves', 'kecap manis', 'avocado', 'chili flakes', 'red chili flakes', 'tomatoes'},
{'coriander', 'white wine', 'fish stock', 'apple cider vinegar', 'salsa', 'rhubarb', 'beef brisket', 'cinnamon sticks', 'cumin', 'roasted chicken', 'chicken wings', 'white vinegar', 'sriracha', 'slivered almonds', 'fresh thyme', 'scotch bonnet pepper', 'zucchini', 'hazelnuts', 'pani puri', 'yukon gold potato', 'toasted bread', 'chicken', 'yoghurt', 'maggi cubes', 'couscous', 'roma tomatoes', 'celery seeds', 'chaat masala', 'white pepper', 'black cardamom', 'harissa', 'red snapper', 'green cardamom', 'crushed red pepper flakes', 'tahini', 'mexican crema', 'chiles de árbol', 'tomato', 'baby squid', 'mussels', 'chipotle adobo sauce', 'shelled large shrimp', 'tomato puree', 'chickpeas', 'fresh tortillas', 'flat-leaf parsley', 'anaheim chili', 'parsley', 'shrimp', 'chile manzano', 'vegetable bullion', 'prawns', 'cherry tomatoes', 'marjoram', 'beer', 'green bell pepper', 'date syrup', 'guajillo chile', 'baby scallops', 'yellow mustard', 'black chickpeas', 'bell pepper', 'filo pastry', 'thin sev', 'bacon', 'white wine vinegar', 'limes', 'rice', 'serrano chili', 'brown sugar', 'parmesan cheese', 'poblano chili', 'fennel bulbs', 'clams', 'baby carrot', 'arborio risotto rice', 'oregano', 'oaxaca cheese', 'green cabbage', 'yellow onion', 'balsamic vinegar', 'whole-milk yogurt', 'sugar', 'red bell pepper', 'pepitas', 'red pepper flakes', 'oranges', 'yellow bell pepper', 'summer squash', 'cloves', 'red cabbage', 'black peppercorns', 'fresh ricotta', 'crab legs', 'scallion chutney', 'sesame seeds', 'vegetable oil'}]