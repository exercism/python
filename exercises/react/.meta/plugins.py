def add_callbacks(case):
    observers = []
    callbacks = []
    operations = [op for op in case["input"]["operations"] if op["type"] == "add_callback"]

    if not operations:
        return '', {}

    suffix = ''
    if len(operations) > 1:
        suffix = 'cb{i}_'
    for i, op in enumerate(operations):
        callbacks.append(op["name"])
        observers.append(f'{suffix.format(i=i + 1)}observer')

    assignment_block = f'\n        {", ".join(observers)} = {", ".join(len(callbacks) * ["[]"])}\n'
    for callback, observer in zip(callbacks, observers):
        assignment_block += f'        {callback} = self.callback_factory({observer})\n'

    return assignment_block, dict(zip(callbacks, observers))
