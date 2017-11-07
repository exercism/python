class Cell(object):
    def __init__(self, reactor, value=0, dependencies=set(),
                 updater=None):
        self.reactor = reactor
        self.index = len(reactor.cells)
        reactor.cells.append(self)
        self.value = value
        self.dirty = False
        self.dependencies = dependencies
        self.dependents = set()
        self.updater = updater
        self.watchers = set()
        if updater is not None:
            self.update()
            self.notify()

    def add_watcher(self, watcher):
        self.watchers.add(watcher)

    def remove_watcher(self, watcher):
        self.watchers.remove(watcher)

    def set_value(self, value, top=True):
        self.value = value
        for d in self.dependents:
            d.update()
        if top:
            self.reactor.notify()

    def update(self):
        if self.updater is not None:
            values = [d.value for d in self.dependencies]
            value = self.updater(values)
            if self.value != value:
                self.set_value(value, False)
                self.dirty = True

    def notify(self):
        if self.dirty:
            for watcher in self.watchers:
                watcher(self, self.value)
            self.dirty = False

    def __hash__(self):
        return self.index


class Reactor(object):
    def __init__(self):
        self.cells = []

    def create_input_cell(self, value):
        return Cell(self, value=value)

    def create_compute_cell(self, dependencies, updater):
        cell = Cell(self,
                    dependencies=dependencies,
                    updater=updater)
        for d in dependencies:
            d.dependents.add(cell)
        return cell

    def notify(self):
        for cell in self.cells:
            cell.notify()
