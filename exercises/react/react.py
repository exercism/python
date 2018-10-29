class InputCell(object):
    def __init__(self, initial_value):
        self.value = None


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.value = None

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass

    def expect_callback_values(self, callback):
        pass
