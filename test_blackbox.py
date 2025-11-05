import unittest
from io import StringIO
from datetime import datetime
from app import app

class TestBlackBox(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)

    def test_add_feedback_valid(self):
        data = {"student_name": "John", "subject": "Math", "rating": 5, "comments": "Excellent"}
        response = self.client.post('/add_feedback', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Feedback added successfully", response.data)

    def test_add_feedback_invalid_rating(self):
        data = {"student_name": "Alice", "subject": "Science", "rating": 8}
        response = self.client.post('/add_feedback', json=data)
        self.assertIn(b"Rating must be between 1 and 5", response.data)


if __name__ == '__main__':
    # Capture test results
    buffer = StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBlackBox)

    # Run the tests
    result = runner.run(suite)

    # Save to log file
    with open("blackbox_test_results.txt", "a") as f:
        f.write("\n" + "=" * 60 + "\n")
        f.write(f"Black Box Test Run on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
        f.write(buffer.getvalue())
        f.write(f"Ran {result.testsRun} tests\n")
        f.write(f"Failures: {len(result.failures)} | Errors: {len(result.errors)}\n")
        f.write("-" * 60 + "\n\n")

    # Print test results to console too
    print(buffer.getvalue())
