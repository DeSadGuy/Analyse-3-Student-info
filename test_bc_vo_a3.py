import unittest
from unittest.mock import MagicMock
from bc_vo_a3 import YourClassName

class TestAddNewStudentWithoutStudentNumber(unittest.TestCase):
    def setUp(self):
        self.db = YourClassName()  # replace with your actual class name
        self.db.querydatabase = MagicMock()
        self.db.Database = MagicMock()

    def test_add_new_student_without_studentnumber(self):
        self.db.querydatabase.fetchall.return_value = []
        self.db.add_new_student_without_studentnumber('John', 'Doe', 'New York', '2000-01-01', 'Class1')
        self.db.querydatabase.execute.assert_called()
        self.db.Database.commit.assert_called()

    def test_add_new_student_without_studentnumber_existing(self):
        self.db.querydatabase.fetchall.return_value = [('09', 'John', 'Doe', 'New York', '2000-01-01', 'Class1')]
        self.db.add_new_student_without_studentnumber('John', 'Doe', 'New York', '2000-01-01', 'Class1')
        self.db.querydatabase.execute.assert_called()

if __name__ == '__main__':
    unittest.main()