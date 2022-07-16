from django.test import TestCase
from django.urls import reverse

from coffeebeans.models import Coffeebean

# using fixtures
class CoffeeTestCase(TestCase):
    fixtures = [
        "coffeebeans.fixture_new.json",
        "coffeekinds.fixture_new.json",
        "coffeeorigin.fixture_new.json",
        "coffeemethod.fixture_new.json",
        "coffeeroastlevel.fixture_new.json",
        "attributes.fixture_new.json"
    ]

    def test_list_coffees(self):
        response = self.client.get(
            reverse("coffeebeans:list")
        )

        self.assertEqual(response.status_code, 200)

        coffee_list = Coffeebean.objects.all()
        coffees_in_context = response.context["coffeebeans"]
        self.assertEqual(len(coffee_list), len(coffees_in_context))

# using setUp
class CoffeeDetailsTestCase(TestCase):
    def setUp(self):
        Coffeebean.objects.create(
            pk="33",
            name="testcoffee",
            description="123",
            price=1000,
        )

    def test_details_view(self):
        test_coffee_instance = Coffeebean.objects.get(pk="33")
        response = self.client.get(
            reverse("coffeebeans:details", kwargs={'pk': '33'})
        )
        self.assertEqual(response.status_code, 200)
        details_in_context = response.context["coffee_details"]

        self.assertEqual(details_in_context.name, test_coffee_instance.name)
        self.assertEqual(details_in_context.price, test_coffee_instance.price)


