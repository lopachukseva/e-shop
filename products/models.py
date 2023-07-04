from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="products_images")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(item.sum() for item in self)

    def total_quantity(self):
        return sum(item.quantity for item in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"Корзина для {self.user.username}, Категория: {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity

    def to_json(self):
        basket_item = {
            "product_name": self.product.name,
            "quantity": self.quantity,
            "price": float(self.product.price),
            "sum": float(self.sum()),
        }
        return basket_item

    @classmethod
    def create_or_update(cls, product_id, user):
        basket = Basket.objects.filter(user=user, product_id=product_id)

        if not basket.exists():
            obj = Basket.objects.create(user=user, product_id=product_id, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = basket.first()
            basket.quantity += 1
            basket.save()
            is_created = False
            return basket, is_created
