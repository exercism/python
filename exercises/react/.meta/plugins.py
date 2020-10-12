def add_callbacks(operations):
    observers = []
    callbacks = []
    add_operations = [op for op in operations if op["type"] == "add_callback"]

    if not add_operations:
        return '', {}

    has_prefix = len(add_operations) > 1
    for i, op in enumerate(add_operations):
        callbacks.append(op["name"])
        observers.append((f"cb{i + 1}_" if has_prefix else "") + "observer")

    assignment_block = f'{", ".join(observers)} = {", ".join(len(callbacks) * ["[]"])}'
    return assignment_block, dict(zip(callbacks, observers))
