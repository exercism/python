def add_callbacks(case):
    observers = []
    callbacks = []
    operations = list(filter(lambda op: op["type"] == "add_callback", case["input"]["operations"]))

    if len(operations) == 0:
        return '', {}

    sufix = ''
    if len(operations) > 1:
        sufix = 'cb{i}_'
    for i, op in enumerate(operations):
        callbacks.append(op["name"])
        observers.append(f'{sufix.format(i=i + 1)}observer')

    super_string = f'\n        {", ".join(observers)} = {", ".join(len(callbacks) * ["[]"])}\n'
    for callback, observer in zip(callbacks, observers):
        super_string += f'        {callback} = self.callback_factory({observer})\n'

    return super_string, dict(zip(callbacks, observers))
