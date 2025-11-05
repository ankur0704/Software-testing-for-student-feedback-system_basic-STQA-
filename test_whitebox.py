import unittest
from io import StringIO
import sys
from datetime import datetime
from models import add_feedback, get_all_feedback, init_db

class TestWhiteBox(unittest.TestCase):
    def setUp(self):
        init_db()

    def test_rating_boundary(self):
        result_low = add_feedback("Test1", "Math", 1, "Lowest rating")
        result_high = add_feedback("Test2", "Science", 5, "Highest rating")
        self.assertIn("message", result_low)
        self.assertIn("message", result_high)

    def test_invalid_rating(self):
        result = add_feedback("Test3", "English", 0, "Invalid rating")
        self.assertIn("error", result)

    
    def test_data_retrieval(self):
        add_feedback("Ravi", "Physics", 4, "Good")
        feedbacks = get_all_feedback()
        self.assertTrue(len(feedbacks) > 0)


if __name__ == '__main__':
    # Capture output to both console and file
    buffer = StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestWhiteBox)

    # Run the tests
    result = runner.run(suite)

    # Write results to log file
    with open("test_results.txt", "a") as f:
        f.write("\n" + "=" * 60 + "\n")
        f.write(f"Test Run on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
        f.write(buffer.getvalue())
        f.write(f"Ran {result.testsRun} tests\n")
        f.write(f"Failures: {len(result.failures)} | Errors: {len(result.errors)}\n")
        f.write("-" * 60 + "\n\n")

    # Also print to console
    print(buffer.getvalue())
