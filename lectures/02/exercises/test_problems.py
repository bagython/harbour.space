"""Auto-tests for lecture 02 exercises.

Default target module: problems
Override with: SOLUTIONS_MODULE=reference_solutions
"""

from __future__ import annotations

import io
import importlib
import os
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

MODULE_NAME = os.getenv("SOLUTIONS_MODULE", "problems")
problems = importlib.import_module(MODULE_NAME)


class Lecture02CoreProblemsTest(unittest.TestCase):
    def test_user(self) -> None:
        user = problems.User("Ana")
        self.assertEqual(user.name, "Ana")
        out = io.StringIO()
        with redirect_stdout(out):
            user.say_hi()
        self.assertEqual(out.getvalue().strip(), "Hello, I am Ana")

    def test_bank_account(self) -> None:
        acc = problems.BankAccount("Ana", 100.0)
        acc.deposit(25.0)
        acc.withdraw(20.0)
        self.assertEqual(acc.balance, 105.0)
        acc.withdraw(1000.0)
        self.assertEqual(acc.balance, 105.0)
        acc.deposit(-5.0)
        self.assertEqual(acc.balance, 105.0)
        acc2 = problems.BankAccount("Bo", -10.0)
        self.assertEqual(acc2.balance, 0.0)

    def test_team_no_shared_mutable_state(self) -> None:
        t1 = problems.Team()
        t2 = problems.Team()
        t1.add("Alice")
        self.assertEqual(t1.members, ["Alice"])
        self.assertEqual(t2.members, [])
        self.assertEqual(len(t1), 1)

    def test_queue_state(self) -> None:
        q = problems.QueueState()
        q.push("a")
        q.push("b")
        self.assertEqual(q.pop(), "a")
        self.assertEqual(q.pop(), "b")
        self.assertIsNone(q.pop())

    def test_wallet(self) -> None:
        w = problems.Wallet(10.0)
        w.top_up(5.0)
        w.pay(5.0)
        self.assertEqual(w.balance, 10.0)
        with self.assertRaises(problems.InsufficientFunds):
            w.pay(100.0)

    def test_shopping_cart(self) -> None:
        cart = problems.ShoppingCart()
        cart.add_item("Book", 10.0, qty=2)
        cart.add_item("Pen", 1.5)
        cart.add_item("Invalid", -1.0, qty=1)
        cart.add_item("Invalid qty", 5.0, qty=0)
        self.assertEqual(cart.total_items(), 3)
        self.assertAlmostEqual(cart.total_price(), 21.5)
        self.assertIn("ShoppingCart", repr(cart))

    def test_classroom(self) -> None:
        original_name = problems.Classroom.school_name
        try:
            g1 = problems.Classroom("G1")
            g2 = problems.Classroom("G2")
            g1.add_student("Ana")
            g1.add_student("Bo")
            self.assertEqual(len(g1), 2)
            g1.set_school_name("HS Python")
            self.assertEqual(problems.Classroom.school_name, "HS Python")
            self.assertEqual(g2.school_name, "HS Python")
        finally:
            problems.Classroom.school_name = original_name

    def test_rectangle(self) -> None:
        r = problems.Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
        self.assertEqual(r.perimeter(), 14)
        self.assertIn("Rectangle", repr(r))
        r2 = problems.Rectangle(-3, 4)
        self.assertEqual(r2.area(), 12)
        self.assertEqual(r2.perimeter(), 14)

    def test_playlist(self) -> None:
        pl = problems.Playlist()
        pl.add("Song A")
        pl.add("Song B")
        self.assertEqual(len(pl), 2)
        self.assertIn("Song A", pl)
        self.assertEqual(list(pl), ["Song A", "Song B"])

    def test_product(self) -> None:
        p = problems.Product("Keyboard", 100.0)
        self.assertAlmostEqual(p.get_price(), 100.0)
        p.apply_discount(10)
        self.assertAlmostEqual(p.get_price(), 90.0)
        p.apply_discount(200)
        self.assertAlmostEqual(p.get_price(), 0.0)
        p.set_price(-1)
        self.assertAlmostEqual(p.get_price(), 0.0)

    def test_student_inheritance(self) -> None:
        p = problems.Person("Ana")
        s = problems.Student("Bo", "G2")
        self.assertEqual(p.describe(), "Person(name=Ana)")
        self.assertEqual(s.describe(), "Student(name=Bo, group=G2)")

    def test_point2d(self) -> None:
        p1 = problems.Point2D(0, 0)
        p2 = problems.Point2D(3, 4)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)
        self.assertEqual(problems.Point2D(1, 2), problems.Point2D(1, 2))
        self.assertEqual(repr(problems.Point2D(1, 2)), "Point2D(1, 2)")

    def test_inventory(self) -> None:
        inv = problems.Inventory()
        inv.add("pen", 3)
        inv.add("book", 1)
        inv.remove("pen", 2)
        self.assertEqual(inv.count("pen"), 1)
        self.assertIn("pen", inv)
        inv.remove("pen", 1)
        self.assertNotIn("pen", inv)
        self.assertEqual(len(inv), 1)
        inv.remove("pen", 1)
        self.assertEqual(inv.count("pen"), 0)
        inv.add("book", 0)
        self.assertEqual(inv.count("book"), 1)

    def test_course_catalog(self) -> None:
        catalog = problems.CourseCatalog()
        catalog.add_course("PY-102", "Classes")
        catalog.add_course("PY-101", "Intro")
        self.assertEqual(catalog.get_title("PY-101"), "Intro")
        self.assertEqual(list(catalog), [("PY-101", "Intro"), ("PY-102", "Classes")])
        self.assertEqual(len(catalog), 2)

    def test_default_dict(self) -> None:
        dd_int = problems.DefaultDict(int)
        self.assertEqual(dd_int["missing"], 0)
        dd_int["missing"] += 5
        self.assertEqual(dd_int["missing"], 5)
        self.assertIn("missing", dd_int)
        self.assertEqual(len(dd_int), 1)

        dd_list = problems.DefaultDict(list)
        dd_list["letters"].append("a")
        dd_list["letters"].append("b")
        self.assertEqual(dd_list["letters"], ["a", "b"])

        dd_none = problems.DefaultDict()
        self.assertIsNone(dd_none["unknown"])

        dd_invalid = problems.DefaultDict(123)
        self.assertIsNone(dd_invalid["unknown"])


if __name__ == "__main__":
    unittest.main()
