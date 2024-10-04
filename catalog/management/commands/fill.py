from django.core.management.base import BaseCommand
from catalog.models import Category, Product, Release


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'Велосипеды', 'description': 'новые велосипеды'},
            {'category_name': 'Самокаты', 'description': 'новые самокаты'},
            {'category_name': 'Ролики', 'description': 'ролики, коньки'}
        ] 
        
        # Создаем категории
        category_for_create = []
        categories = {}
        for category in category_list:
            category_for_create.append(Category(**category))
        Category.objects.bulk_create(category_for_create)
        for category in category_list:
            categories[category.get('category_name')] = Category.objects.filter(category_name=category.get('category_name'))[0]
        

        products_list = [
            {'product_name': 'Велосипед', 'product_description': 'новый', 'price': 5000.00, 'category': categories.get('Велосипеды')},
            {'product_name': 'Самокат', 'product_description': 'б/у', 'price': 3000.00, 'category': categories.get('Самокаты')},
            {'product_name': 'Ролики', 'product_description': 'новые', 'price': 3500.00, 'category': categories.get('Ролики')},
            {'product_name': 'Коньки', 'product_description': 'б/у, но как живые', 'price': 500.00, 'category': categories.get('Ролики')},
            {'product_name': 'Велосипед', 'product_description': 'новый/детский', 'price': 5000.00, 'category': categories.get('Велосипеды')},
        ]

        # Создаем продукты
        product_for_create = []
        release_for_create = []
        for product in products_list:
            product_for_create.append(Product(**product))
            release_for_create.append(Release(product = product_for_create[-1]))

        Product.objects.bulk_create(product_for_create)
        Release.objects.bulk_create(release_for_create)
        