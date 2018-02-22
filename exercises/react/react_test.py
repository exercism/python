import unittest

from react import InputCell, ComputeCell, Callback


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class ReactTests(unittest.TestCase):
    def test_input_cells_have_a_value(self):
        input_ = InputCell(10)
        self.assertEqual(input_.value, 10)

    def test_can_set_input_cell_value(self):
        input_ = InputCell(4)
        input_.value = 20
        self.assertEqual(input_.value, 20)

    def test_compute_cells_calculate_initial_value(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], lambda inputs: inputs[0] + 1)
        self.assertEqual(output.value, 2)

    def test_compute_cells_take_inputs_in_right_order(self):
        one = InputCell(1)
        two = InputCell(2)
        output = ComputeCell(
            [one, two],
            lambda inputs: inputs[0] + inputs[1]*10
        )
        self.assertEqual(output.value, 21)

    def test_compute_cells_update_value_when_dependencies_are_changed(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], lambda inputs: inputs[0] + 1)

        input_.value = 3
        self.assertEqual(output.value, 4)

    def test_compute_cells_can_depend_on_other_compute_cells(self):
        input_ = InputCell(1)
        times_two = ComputeCell([input_], lambda inputs: inputs[0] * 2)
        times_thirty = ComputeCell([input_], lambda inputs: inputs[0] * 30)
        output = ComputeCell(
            [times_two, times_thirty],
            lambda inputs: inputs[0] + inputs[1]
        )

        self.assertEqual(output.value, 32)
        input_.value = 3
        self.assertEqual(output.value, 96)

    def test_compute_cells_fire_callbacks(self):
        input_ = InputCell(1)
        output = ComputeCell([input_], lambda inputs: inputs[0] + 1)
        callback1 = Callback()

        output.add_callback(callback1)
        input_.value = 3
        self.assertEqual(callback1.values, [4])

    def test_callback_cells_only_fire_on_change(self):
        input_ = InputCell(1)
        output = ComputeCell(
            [input_],
            lambda inputs: 111 if inputs[0] < 3 else 222
        )
        callback1 = Callback()

        output.add_callback(callback1)
        input_.value = 2
        self.assertEqual(callback1.values, [])
        input_.value = 4
        self.assertEqual(callback1.values, [222])

    def test_callbacks_can_be_added_and_removed(self):
        input_ = InputCell(11)
        output = ComputeCell([input_], lambda inputs: inputs[0] + 1)
        callback1 = Callback()
        callback2 = Callback()
        callback3 = Callback()

        output.add_callback(callback1)
        output.add_callback(callback2)
        input_.value = 31
        output.remove_callback(callback1)
        output.add_callback(callback3)
        input_.value = 41

        self.assertEqual(callback1.values, [32])
        self.assertEqual(callback2.values, [32, 42])
        self.assertEqual(callback3.values, [42])

    def test_removing_a_callback_multiple_times(self):
        """Guard against incorrect implementations which store their
        callbacks in an array."""
        input_ = InputCell(1)
        output = ComputeCell([input_], lambda inputs: inputs[0] + 1)
        callback1 = Callback()
        callback2 = Callback()

        output.add_callback(callback1)
        output.add_callback(callback2)
        output.remove_callback(callback1)
        output.remove_callback(callback1)
        output.remove_callback(callback1)
        input_.value = 2

        self.assertEqual(callback1.values, [])
        self.assertEqual(callback2.values, [3])

    def test_callbacks_should_only_be_called_once(self):
        """Guard against incorrect implementations which call a callback
        function multiple times when multiple dependencies change."""
        input_ = InputCell(1)
        plus_one = ComputeCell([input_], lambda inputs: inputs[0] + 1)
        minus_one1 = ComputeCell([input_], lambda inputs: inputs[0] - 1)
        minus_one2 = ComputeCell([minus_one1], lambda inputs: inputs[0] - 1)
        output = ComputeCell(
            [plus_one, minus_one2],
            lambda inputs: inputs[0] * inputs[1]
        )
        callback1 = Callback()

        output.add_callback(callback1)
        input_.value = 4
        self.assertEqual(callback1.values, [10])

    def test_callbacks_not_called_so_long_as_output_not_changed(self):
        """Guard against incorrect implementations which call callbacks
        if dependencies change but output value doesn't change."""
        input_ = InputCell(1)
        plus_one = ComputeCell([input_], lambda inputs: inputs[0] + 1)
        minus_one = ComputeCell([input_], lambda inputs: inputs[0] - 1)
        always_two = ComputeCell(
            [plus_one, minus_one],
            lambda inputs: inputs[0] - inputs[1]
        )
        callback1 = Callback()

        always_two.add_callback(callback1)
        input_.value = 2
        input_.value = 3
        input_.value = 4
        input_.value = 5
        self.assertEqual(callback1.values, [])


if __name__ == '__main__':
    unittest.main()
