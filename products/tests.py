from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse("index")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store")
        self.assertTemplateUsed(response, "products/index.html")


class ProductsListViewTestCase(TestCase):
    fixtures = ["categories.json", "products.json"]

    def setUp(self):
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse("products")
        response = self.client.get(path)

        products = list(self.products[:3])

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Каталог")
        self.assertTemplateUsed(response, "products/products.html")
        self.assertEqual(list(response.context_data["object_list"]), products)

    def test_list_category(self):
        category = ProductCategory.objects.first()
        path = reverse("category", kwargs={"category_id": category.id})
        response = self.client.get(path)

        products = self.products.filter(category_id=category.id)
        products = list(products[:3])

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Каталог")
        self.assertTemplateUsed(response, "products/products.html")
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(products)
        )
