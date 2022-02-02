import unittest
import os
import time
from utils import load_json, sniff_schema, write_json


class TestSchemaSniffer(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.data_file = 'data/data_1.json'
        cls.output_file = 'result.json'
    
    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(2)
        os.remove(cls.output_file)
        

    def test_load_json_data(self):
        """
        test that a json file can be loaded and that the output is a dict
        """
        data = load_json(TestSchemaSniffer.data_file)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, dict)

    def test_schema_generation(self):
        """
        test that a schema is generated
        """
        data = load_json(TestSchemaSniffer.data_file)
        message = data["message"]
        schema = sniff_schema(message)
        self.assertIsInstance(schema, dict)
        self.assertTrue(len(schema))

    def test_write_json_data(self):
        """
        test that a python dictionary can be saved as a json file with contents intact
        """
        data = load_json(TestSchemaSniffer.data_file)
        message = data["message"]
        schema = sniff_schema(message)
        write_json(schema, TestSchemaSniffer.output_file)
        content = load_json(TestSchemaSniffer.output_file)
        self.assertEqual(content, schema)
        
        

if __name__ == '__main__':
    unittest.main()