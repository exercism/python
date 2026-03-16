import unittest
import pytest

from bake_bake_bake import (
                            receipt_header,
                            receipt_item,
                            receipt_summary,
                            format_message,
                            generate_receipt,
                            )


class BakeBakeBakeTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    def test_receipt_header(self):
        test_data = [
            ("Priya", 40, "-----------Receipt for Priya------------"),
            ("Mei", 34, "---------Receipt for Mei----------"),
            ("Q", 20, "---Receipt for Q----"),
            ("Oluwaseun", 30, "----Receipt for Oluwaseun-----"),
        ]

        for variant, (name, width, expected) in enumerate(test_data, 1):
            with self.subTest(f"variation #{variant}", name=name, width=width, expected=expected):
                actual_result = receipt_header(name, width)
                error_msg = (f"Called receipt_header({name!r}, {width}). "
                             f"The function returned {actual_result!r}, "
                             f"but the test expected {expected!r}.")

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=2)
    def test_receipt_item(self):
        test_data = [
            ("Chocolate Cake", 15.5, 24, 8, "Chocolate Cake..........   15.50"),
            ("Croissant", 3.0, 20, 6, "Croissant...........  3.00"),
            ("Wedding Cake", 145.99, 20, 10, "Wedding Cake........    145.99"),
            ("Espresso", 0.75, 16, 6, "Espresso........  0.75"),
            ("Pain au Chocolat", 4.5, 18, 8, "Pain au Chocolat..    4.50"),
        ]

        for variant, (name, price, item_w, price_w, expected) in enumerate(test_data, 1):
            with self.subTest(f"variation #{variant}", name=name, price=price, expected=expected):
                actual_result = receipt_item(name, price, item_w, price_w)
                error_msg = (f"Called receipt_item({name!r}, {price}, {item_w}, {price_w}). "
                             f"The function returned {actual_result!r}, "
                             f"but the test expected {expected!r}.")

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=3)
    def test_receipt_summary(self):
        test_data = [
            (20.0, 0.05, 40,
             "Subtotal                           20.00\n"
             "Tax (5.0%)                          1.00\n"
             "Total                              21.00"),
            (12.50, 0.085, 26,
             "Subtotal             12.50\n"
             "Tax (8.5%)            1.06\n"
             "Total                13.56"),
            (5.0, 0.0, 30,
             "Subtotal                  5.00\n"
             "Tax (0.0%)                0.00\n"
             "Total                     5.00"),
            (999.99, 0.10, 40,
             "Subtotal                          999.99\n"
             "Tax (10.0%)                       100.00\n"
             "Total                            1099.99"),
        ]

        for variant, (subtotal, tax_rate, width, expected) in enumerate(test_data, 1):
            with self.subTest(f"variation #{variant}", subtotal=subtotal, tax_rate=tax_rate, width=width):
                actual_result = receipt_summary(subtotal, tax_rate, width)
                error_msg = (f"Called receipt_summary({subtotal}, {tax_rate}, {width}). "
                             f"The function returned:\n{actual_result}\n"
                             f"but the test expected:\n{expected}")

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=4)
    def test_gift_message(self):
        test_data = [
            ("Happy Birthday, {name}! Enjoy your {item}. From {sender}.",
             {"name": "Priya", "item": "Chocolate Cake", "sender": "Ravi"},
             "~ Happy Birthday, Priya! Enjoy your Chocolate Cake. From Ravi. ~"),
            ("Dear {name}, thank you for your order! - {sender}",
             {"name": "Amara", "sender": "The Bake Bake Bake Team"},
             "~ Dear Amara, thank you for your order! - The Bake Bake Bake Team ~"),
            ("Congratulations on your special day!",
             {},
             "~ Congratulations on your special day! ~"),
            ("You deserve the best. Happy birthday, {name}! - {sender}",
             {"name": "Liora", "sender": "Eshe"},
             "~ You deserve the best. Happy birthday, Liora! - Eshe ~"),
        ]

        for variant, (template, kwargs, expected) in enumerate(test_data, 1):
            with self.subTest(f"variation #{variant}", template=template, kwargs=kwargs, expected=expected):
                actual_result = format_message(template, **kwargs)
                error_msg = (f"Called format_message({template!r}, **{kwargs}). "
                             f"The function returned {actual_result!r}, "
                             f"but the test expected {expected!r}.")

                self.assertEqual(actual_result, expected, msg=error_msg)

    @pytest.mark.task(taskno=5)
    def test_generate_receipt(self):
        items = ["Strawberry Tart", "Macaron", "Sourdough Loaf"]
        prices = [4.5, 2.5, 6.0]
        expected = (
            "----------Receipt for Amara-----------\n"
            "Strawberry Tart...............    4.50\n"
            "Macaron.......................    2.50\n"
            "Sourdough Loaf................    6.00\n"
            "--------------------------------------\n"
            "Subtotal                         13.00\n"
            "Tax (6.5%)                        0.84\n"
            "Total                            13.85"
        )
        self.assertEqual(generate_receipt("Amara", items, prices, 0.065, 38), expected)

    @pytest.mark.task(taskno=5)
    def test_generate_receipt_large(self):
        items = ["Custom Wedding Cake", "Dozen Cupcakes", "Delivery Fee"]
        prices = [250.0, 35.0, 15.0]
        expected = (
            "------------Receipt for Dara------------\n"
            "Custom Wedding Cake.............  250.00\n"
            "Dozen Cupcakes..................   35.00\n"
            "Delivery Fee....................   15.00\n"
            "----------------------------------------\n"
            "Subtotal                          300.00\n"
            "Tax (8.0%)                         24.00\n"
            "Total                             324.00"
        )
        self.assertEqual(generate_receipt("Dara", items, prices, 0.08, 40), expected)

    @pytest.mark.task(taskno=5)
    def test_generate_receipt_single_item(self):
        items = ["Baguette"]
        prices = [2.0]
        expected = (
            "-----Receipt for Mei------\n"
            "Baguette..........    2.00\n"
            "--------------------------\n"
            "Subtotal              2.00\n"
            "Tax (5.0%)            0.10\n"
            "Total                 2.10"
        )
        self.assertEqual(generate_receipt("Mei", items, prices, 0.05, 26), expected)

    @pytest.mark.task(taskno=5)
    def test_generate_gift_receipt(self):
        items = ["Chocolate Cake", "Dozen Cookies"]
        prices = [20.0, 12.0]
        gift = format_message(
            "For {name}, with love from {sender}.",
            name="Noor", sender="Aisha"
        )
        expected = (
            "------------Receipt for Noor------------\n"
            "Chocolate Cake\n"
            "Dozen Cookies\n"
            "----------------------------------------\n"
            "  ~ For Noor, with love from Aisha. ~   "
        )
        self.assertEqual(generate_receipt("Noor", items, prices, 0.05, 40, gift), expected)
