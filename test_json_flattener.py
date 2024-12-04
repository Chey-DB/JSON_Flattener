import json
import os
import unittest
from json_flattener import get_value_by_path, extract_keys_from_json, load_json, save_json


class TestJsonFlattener(unittest.TestCase):
    def setUp(self):
        """
        Set up test data for all the tests.
        """
        self.test_json = {
            "key1": {
                "key2": "value1"
            },
            "key3": [
                {
                    "key4": "value2",
                    "key5": "value3"
                }
            ]
        }
        self.keys_to_extract = [
            "key1.key2",
            "key3.key4",
            "key3.key5"
        ]
        self.expected_flattened = {
            "key1.key2": "value1",
            "key3.key4": "value2",
            "key3.key5": "value3"
        }

    def test_get_value_by_path(self):
        """
        Test the function to get a value by a dot-separated key path.
        """
        # Test key1.key2
        value = get_value_by_path(self.test_json, "key1.key2")
        self.assertEqual(value, "value1")

        # Test key3.key4
        value = get_value_by_path(self.test_json, "key3.key4")
        self.assertEqual(value, "value2")

        # Test key3.key5
        value = get_value_by_path(self.test_json, "key3.key5")
        self.assertEqual(value, "value3")

        # Test non-existent key
        value = get_value_by_path(self.test_json, "key3.key6")
        self.assertIsNone(value)

    def test_extract_keys_from_json(self):
        """
        Test the extraction of specific keys from a nested JSON structure.
        """
        flattened = extract_keys_from_json(self.test_json, self.keys_to_extract)
        self.assertEqual(flattened, self.expected_flattened)

    def test_load_json(self):
        """
        Test loading JSON from a file.
        """
        with open("test.json", "w") as f:
            json.dump(self.test_json, f)

        loaded_data = load_json("test.json")
        self.assertEqual(loaded_data, self.test_json)

    def test_save_json(self):
        """
        Test saving JSON to a file.
        """
        save_json(self.expected_flattened, "flattened_test.json")

        with open("flattened_test.json", "r") as f:
            saved_data = json.load(f)

        self.assertEqual(saved_data, self.expected_flattened)

    def tearDown(self):
        """
        Clean up any temporary files created during testing.
        """
        
        if os.path.exists("test.json"):
            os.remove("test.json")
        if os.path.exists("flattened_test.json"):
            os.remove("flattened_test.json")


if __name__ == "__main__":
    unittest.main()
