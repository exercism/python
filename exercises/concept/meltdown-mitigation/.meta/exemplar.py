def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: Union[int,float] temperature
    :param neutrons_emitted: Union[int,float] number of neutrons emitted per second
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    output = temperature * neutrons_emitted
    balanced = False

    if (temperature < 800 and neutrons_emitted > 500) and output < 500000:
        balanced = True

    return balanced


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: Union[int,float] voltage
    :param current: Union[int,float] current
    :param theoretical_max_power: Union[int,float] power that corresponds to a 100% efficiency
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percentage_range = (generated_power / theoretical_max_power) * 100
    efficiency_level = 'unknown'

    if 80 <= percentage_range <= 100:
        efficiency_level = 'green'
    elif 60 <= percentage_range < 80:
        efficiency_level = 'orange'
    elif 30 <= percentage_range < 60:
        efficiency_level = 'red'
    else:
        efficiency_level = 'black'

    return efficiency_level


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return safety range.

    :param temperature: Union[int,float]
    :param neutrons_produced_per_second: Union[int,float]
    :param threshold: Union[int,float]
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    """
    output = temperature * neutrons_produced_per_second
    operational_percentage = (output / threshold) * 100
    safety_range = 'UNKNOWN'
    print(operational_percentage)

    if operational_percentage < 40:
        safety_range = 'LOW'
    elif 90 <= operational_percentage <= 110:
        safety_range = 'NORMAL'
    else:
        safety_range = 'DANGER'

    return safety_range
