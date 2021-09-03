import unittest
from bigquery.client_simple_query import create_client, set_my_query


class TestBigQuery(unittest.TestCase):
    def check_client(self):
        client = create_client()
        client_type = type(client)
        self.assertEqual(client_type, "google.cloud.bigquery.client.Client")

    def check_my_query(self):
        my_query = set_my_query()
        self.assertEqual(my_query, 'SELECT * FROM ds_eu.covid LIMIT 10')

if __name__ == '__main__':
    unittest.main()
