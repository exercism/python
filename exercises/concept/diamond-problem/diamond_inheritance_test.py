import unittest, pytest
import diamond_inheritance as diamond


class InventoryTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_our_classes_are_there(self):
        classes = dir(diamond)
        self.assertIn("ClassA", classes, msg = "Class A not present.")
        self.assertIn("ClassB", classes, msg = "Class B not present.")
        self.assertIn("ClassC", classes, msg = "Class C not present.")
        self.assertIn("ClassD", classes, msg = "Class D not present.")
        self.assertIn("ClassE", classes, msg = "Class E not present.")

    @pytest.mark.task(taskno=2)
    def test_ClassB_inheritance(self):
        error = "Check the class B inheritance."
        self.assertTrue(issubclass(diamond.ClassB, diamond.ClassA), msg = error)
    
    @pytest.mark.task(taskno=3)
    def test_ClassC_inheritance(self):
        error = "Check the class C inheritance."
        self.assertTrue(issubclass(diamond.ClassC, diamond.ClassA), msg = error)
    
    @pytest.mark.task(taskno=4)
    def test_ClassD_inheritance(self):
        error = "Check the class D inheritance."
        self.assertTrue(issubclass(diamond.ClassD, diamond.ClassA), msg = error)
    
    @pytest.mark.task(taskno=5)
    def test_ClassE_inheritance(self):
        error = "Seems class E doesn't inherit class "
        self.assertTrue(issubclass(diamond.ClassE, diamond.ClassA), msg = error+"A.")
        self.assertTrue(issubclass(diamond.ClassE, diamond.ClassB), msg = error+"B.")
        self.assertTrue(issubclass(diamond.ClassE, diamond.ClassC), msg = error+"C.")
        self.assertTrue(issubclass(diamond.ClassE, diamond.ClassD), msg = error+"D.")

    @pytest.mark.task(taskno=6)
    def test_class_inheritance_order(self):
        e = diamond.ClassE()
        error = "The constructor calls seem to be in the wrong order."
        self.assertEquals("ADBCE", e.sequence, msg = error)

    @pytest.mark.task(taskno=7)
    def test_ClassB_sequence_as_tuple_method(self):
        error = "Method <sequence_as_tuple> not working correctly for class B."
        b = diamond.ClassB()
        self.assertTupleEqual(('A', 'B'), b.sequence_as_tuple())
    
    @pytest.mark.task(taskno=8)
    def test_ClassC_sequence_as_tuple_method(self):
        error = "Method <sequence_as_tuple> not working correctly for class C."
        c = diamond.ClassC()
        self.assertTupleEqual(('A', 'C'), c.sequence_as_tuple())
    
    @pytest.mark.task(taskno=9)
    def test_ClassD_sequence_as_tuple_method(self):
        error = "Method <sequence_as_tuple> not working correctly for class D."
        d = diamond.ClassD()
        self.assertTupleEqual(('A', 'D'), d.sequence_as_tuple())
    
    @pytest.mark.task(taskno=10)
    def test_ClassE_sequence_as_tuple_method(self):
        error = "Method <sequence_as_tuple> not working correctly for class E."
        e = diamond.ClassE()
        self.assertTupleEqual(('A', 'D', 'B', 'C', 'E'), e.sequence_as_tuple())

        


if __name__ == "__main__":
    unittest.main()
