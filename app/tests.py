from django.test import TestCase
from django.urls import reverse
from .models import Stock



class StockTestCase(TestCase):
    def setUp(self):
        # Create some sample data for testing
        Stock.objects.create(date="2022-01-01", open_price=100.0, close_price=110.0)
        Stock.objects.create(date="2022-01-02", open_price=200.0, close_price=210.0)

    def test_search_stock(self):
        # Perform a search for "Apple"
        response = self.client.get(reverse('stock_list'), {'search': 'Apple'})
        
        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)
        
        # Check if the search results contain the expected data
        self.assertContains(response, 100.0)
        # self.assertNotContains(response, "2022-01-02")
