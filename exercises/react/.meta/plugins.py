def add_callbacks(operations, cells):
    observers = []
    callbacks = []
    add_operations = [op for op in operations if op["type"] == "add_callback"]
    set_operations = [op for op in operations if op["type"] == "set_value"]

    if not add_operations:
        return '', {}, {}

    callbacks_values = {}
    activated_callbacks = []
    for op in operations:
        if op['type'] == 'add_callback':
            if not op['name'] in activated_callbacks:
                activated_callbacks.append(op['name'])
            callbacks_values[op['name']] = {'values': [], 'cell': op['cell']}
        elif op['type'] == 'remove_callback':
            if op['name'] in activated_callbacks:
                activated_callbacks.remove(op['name'])
        elif op['type'] == 'set_value':
            for callback in callbacks_values:
                cell = [cell for cell in cells if cell['name'] == callbacks_values[callback]['cell']][0]
                if callback in activated_callbacks and op['cell'] in cell['inputs']:
                    callbacks_values[callback]['values'].append(op['value'] + 1)

    has_prefix = len(add_operations) > 1
    for i, op in enumerate(add_operations):
        callbacks.append(op["name"])
        observers.append((f"cb{i + 1}_" if has_prefix else "") + "observer")

    assignment_block = f'{", ".join(observers)} = {", ".join(len(callbacks) * ["[]"])}'
    return assignment_block, dict(zip(callbacks, observers)), callbacks_values
