from django.db import models
from django.core.validators import MinValueValidator


class Bouqet(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название букета')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена',
                                db_index=True,
                                max_digits=10,
                                decimal_places=3,
                                validators=[MinValueValidator(0)])
    size = models.CharField(max_length=100, verbose_name='Размер Букета')
    flowers = models.TextField(verbose_name='Состав букета')
    picture = models.CharField(max_length=200,verbose_name='Ссылка на изображение')
    event = models.ForeignKey('Event',
                              on_delete=models.CASCADE,
                              related_name='bouqets',
                              verbose_name='Событие',
                              null=True, blank=True)

    class Meta:
        verbose_name = 'Bouqet'
        verbose_name_plural = 'Bouqets'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название события')

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class Customer(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Имя клиента')
    phone_number = models.CharField(max_length=20, verbose_name='Телефонный номер')

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'


class Order(models.Model):
    TIME = [
        ('1', '10:00-12:00'),
        ('2', '12:00-14:00'),
        ('3', '14:00-16:00'),
        ('4', '16:00-18:00'),
        ('5', '18:00-20:00'),
        ('now', 'Как можно скорее')
    ]
    ORDER_STATUS = [
        ('UNPROCESSED', 'Ожидает оплаты'),
        ('SUCCESS', 'Оплачено'),
        ('CANCELLED', 'Отменен')
    ]
    address = models.CharField('Адрес доставки букета', max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_time = models.CharField(max_length=20,
                                  choices=TIME,
                                  db_index=True,
                                  verbose_name='Время доставки',
                                  default='now')
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        db_index=True,
        verbose_name='Статус Заказа',
        default='UNPROCESSED')
    payment_id = models.CharField(max_length=200,
                                  null=True,
                                  blank=True,
                                  db_index=True,
                                  verbose_name='Идентиф-р платежа')

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.order_items.all())
        return total_cost

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.address} - {self.customer}"


class OrderItem(models.Model):
    bouqet = models.ForeignKey(Bouqet, on_delete=models.CASCADE, related_name='order_items', verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', verbose_name='Заказ')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        db_index=True,
        default=0,
        verbose_name='Общая стоимость товара'
    )

    def get_cost(self):
        return self.price


    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = "Order items"

    def __str__(self):
        return f"{self.bouqet} - {self.order}"





# Create your models here.
