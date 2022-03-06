"""
In order to efficiently complete this task, I first define the problem.

Problem: understanding how much time it takes to prepare and bake lasagna. 
    Given Information :
        Expected Baking Time : 40 minutes
        Expected Preparation Time Per Layer : 2 minutes
        
Then, I decompose the problem into its constituent parts.

FunctionA: Time Needed to Bake Lasagna

FunctionB: Time Needed to Prepare Lasagna


Next, I consider the scenario.

We are asked to solve a problem in-media-res. The person has already started cooking the lasagna. Like a timer, we will tell the person the amount of time 
remaining needed to bake the lasagna.  


////

Notes for Those Who Tried to Apply This to a Real World Scenario:

a. Yes, the expected amount of time for baking ~ should change ~ based on the number of layers created.
    i. another implementation : 
                New Constant : 
                EXPECTED_BAKING_TIME_PER_LAYER : 20 minutes (guess)
                New Function: 
                def expected_bake_time(num_layers):
                        return num_layers * EXPECTED_BAKING_TIME_PER_LAYER
                        
b. We do not have to consider the temperature of the cooking environment (oven, grill, open-fire), nor do we have to consider the elevation of the environment
c. We do not consider the amount of time required to setup (i.e grab ingredients, setup kitchen space, etc)
                


"""

# upper-case to designate constant (do not change)
EXPECTED_BAKE_TIME = 40

#       equal to the time it takes to prepare a single layer
#upper-case to designate constant (do not change)
PREPARATION_TIME_PER_LAYER = 2
 
           

def bake_time_remaining(elapsed_bake_time):
    """
    Goal : Calculate the bake time remaining.

    To calculate the bake-time remaining, let's simplify it with a narrative.
    
    Jay is cooking his grandma's famous lasagna. 
    According to his grandma's recipe, Lasagna takes X minutes to cook (EXPECTED_BAKE_TIME).
    Jay put the lasagna in the oven Y minutes ago (Elapsed_Bake_Time).
    If we subtract the Elapsed_Bake_Time from EXPECTED_BAKE_TIME, our answer should tell us that the lasagna needs to cook for Z minutes more.   
    """
    
    lasagna_willbe_ready = EXPECTED_BAKE_TIME - elapsed_bake_time
    return lasagna_willbe_ready
    print('The Lasagna will be finished in', lasagna_willbe_ready, 'minutes')
    

def preparation_time_in_minutes(num_layers, elapsed_bake_time):
    
    """
    Goal: to calculate the amount of preparation time needed to cook lasagna
    In a similar pattern, we continue with Jay's quest make his grandma's favorite lasagna.
    
    Jay is preparing to make his grandma's famous lasagna. According to the recipe, 
    for every additional layer of lasagna he adds, he will have to spend an extra 2 minutes to solidly prepare it.
    Example : 2 layers of lasagna, 2 minutes per layer, 
              (2 minutes = 1 layer of lasagna) + (2 minutes = 1 layer of lasagna) = 4 minutes = 2 layers of lasagna
    
    """
     return num_layers * PREPARATION_TIME_PER_LAYER
    

def elapsed_time_in_minutes(preparation_time_in_minutes, elapsed_bake_time):
    """
   Goal: to determine the total amount of time spent both preparing and baking lasagna
   
   To continue our pattern, we will return to our narrative.
   
   Jay wants to know how much time he's spent preparing and baking lasagna.
   
   Example: 4 minutes of preparation time + 20 minutes (amount of time lasagna has been baking in oven)
   
    """
    return preparation_time_in_minutes(num_layers) + elapsed_bake_time
    
