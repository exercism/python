import unittest

from react import Reactor


class CallbackManager(object):
    counter = 0
    observed1 = []
    observed2 = []

    @staticmethod
    def reset():
        CallbackManager.counter = 0
        CallbackManager.observed1 = []
        CallbackManager.observed2 = []

    @staticmethod
    def count(sender, value):
        CallbackManager.counter += 1

    @staticmethod
    def observe1(sender, value):
        CallbackManager.observed1.append(value)

    @staticmethod
    def observe2(sender, value):
        CallbackManager.observed2.append(value)


def increment(values):
    return values[0] + 1


def decrement(values):
    return values[0] - 1


def product(values):
    return values[0] * values[1]


def minimum_of_2(values):
    return values[0] + 1 if values[0] > 2 else 2


class ReactTest(unittest.TestCase):
    def test_setting_input_changes_value(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        self.assertEqual(inputCell1.value, 1)
        inputCell1.set_value(2)
        self.assertEqual(inputCell1.value, 2)

    def test_computed_cell_determined_by_dependencies(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        computeCell1 = reactor.create_compute_cell({inputCell1}, increment)

        self.assertEqual(computeCell1.value, 2)
        inputCell1.set_value(2)
        self.assertEqual(computeCell1.value, 3)

    def test_compute_cells_determined_by_other_compute_cells(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        computeCell1 = reactor.create_compute_cell({inputCell1}, increment)
        computeCell2 = reactor.create_compute_cell({inputCell1}, decrement)
        computeCell3 = reactor.create_compute_cell({computeCell1,
                                                    computeCell2},
                                                   product)
        self.assertEqual(computeCell3.value, 0)
        inputCell1.set_value(3)
        self.assertEqual(computeCell3.value, 8)

    def test_compute_cells_can_have_callbacks(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        computeCell1 = reactor.create_compute_cell({inputCell1}, increment)
        observed = []
        computeCell1.add_watcher(lambda sender, value: observed.append(value))
        self.assertEqual(observed, [])
        inputCell1.set_value(2)
        self.assertEqual(observed, [3])

    def test_callbacks__only_trigger_on_change(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        computeCell1 = reactor.create_compute_cell({inputCell1}, minimum_of_2)

        CallbackManager.reset()
        computeCell1.add_watcher(CallbackManager.count)

        inputCell1.set_value(1)
        self.assertEqual(CallbackManager.counter, 0)
        inputCell1.set_value(2)
        self.assertEqual(CallbackManager.counter, 0)
        inputCell1.set_value(3)
        self.assertEqual(CallbackManager.counter, 1)

    def test_callbacks_can_be_removed(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        computeCell1 = reactor.create_compute_cell({inputCell1}, increment)

        CallbackManager.reset()
        computeCell1.add_watcher(CallbackManager.observe1)
        computeCell1.add_watcher(CallbackManager.observe2)

        inputCell1.set_value(2)
        self.assertEqual(CallbackManager.observed1, [3])
        self.assertEqual(CallbackManager.observed2, [3])

        computeCell1.remove_watcher(CallbackManager.observe1)
        inputCell1.set_value(3)
        self.assertEqual(CallbackManager.observed1, [3])
        self.assertEqual(CallbackManager.observed2, [3, 4])

    def test_callbacks_only_called_once(self):
        reactor = Reactor()
        inputCell1 = reactor.create_input_cell(1)
        computeCell1 = reactor.create_compute_cell({inputCell1}, increment)
        computeCell2 = reactor.create_compute_cell({inputCell1}, decrement)
        computeCell3 = reactor.create_compute_cell({computeCell2}, decrement)
        computeCell4 = reactor.create_compute_cell({computeCell1,
                                                    computeCell3},
                                                   product)

        CallbackManager.reset()
        computeCell4.add_watcher(CallbackManager.count)

        inputCell1.set_value(3)
        self.assertEqual(CallbackManager.counter, 1)


if __name__ == '__main__':
    unittest.main()
