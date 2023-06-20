from django.shortcuts import render


def index(request):
    context = {
        "title": "Store"
    }
    return render(request, "products/index.html", context)


def products(request):
    context = {
        "title": "Catalog",
        "products": [
            {
                "name": "Худи черного цвета с монограммами adidas Originals",
                "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
                "image": "/static/vendor/img/products/Adidas-hoodie.png",
                "price": 4500
            },
            {
                "name": "Синяя куртка The North Face",
                "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
                "image": "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
                "price": 3900
            },
            {
                "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
                "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
                "image": "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
                "price": 7800
            },
        ]
    }
    return render(request, "products/products.html", context)
