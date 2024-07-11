import unittest
from unittest.mock import patch

# https://habr.com/ru/companies/otus/articles/741676/

def remote_sum(a, b):
    # just imagine that this calculates on the remote server
    return a + b

def do_remote_sum(a, b):
    return remote_sum(a, b)

class TestMultiply(unittest.TestCase):
    @patch('task_test_mocking.remote_sum')
    def test_do_remote_sum(self, mock_sum):
        mock_sum.return_value = 4
        return_sum = do_remote_sum(2, 2)
        self.assertEqual(return_sum, 4)

    def test_remote_sum(self):
        expected = 4
        return_sum = remote_sum(2, 2)
        self.assertEqual(return_sum, expected)

if __name__ == "__main__":
    unittest.main()
