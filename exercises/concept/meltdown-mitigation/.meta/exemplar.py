def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature less than 800.
    - The number of neutrons emitted per second greater than 500.
    - The product of temperature and neutrons emitted per second less than 500000.
    """
    output = temperature * neutrons_emitted
    balanced = False

    if (temperature < 800 and neutrons_emitted > 500) and output < 500000:
        balanced = True

    return balanced


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percentage_range = (generated_power / theoretical_max_power) * 100
    efficiency_level = 'unknown'

    if 80 <= percentage_range <= 100:
        efficiency_level = 'green'
    elif 60 <= percentage_range <= 79:
        efficiency_level = 'orange'
    elif 30 <= percentage_range <= 59:
        efficiency_level = 'red'
    else:
        efficiency_level = 'black'

    return efficiency_level


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return safety range.

    :param temperature:
    :param neutrons_produced_per_second:
    :param threshold:
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """
    output = temperature * neutrons_produced_per_second
    operational_percentage = int((output / threshold) * 100)
    safety_range = 'UNKNOWN'

    if operational_percentage < 40:
        safety_range = 'LOW'
    elif 90 <= operational_percentage <= 110:
        safety_range = 'NORMAL'
    else:
        safety_range = 'DANGER'

    return safety_range
