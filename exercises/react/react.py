class Cell(object):
    def set_value(value):
        pass

    def add_watcher(self, watcher_callback):
        pass

    def remove_watcher(self, watcher_callback):
        pass


class Reactor(object):
    def create_input_cell(self, value):
        pass

    def create_compute_cell(self, dependencies, updater_callback):
        pass
