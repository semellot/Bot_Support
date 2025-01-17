from django.db import models


class Tariff(models.Model):
    title = models.CharField('Название тарифа', max_length=200)
    max_requests = models.IntegerField('Максимальное кол-во обращений в месяц')
    max_time_for_ansver = models.TimeField('Максимальное время ответа на заявку')
    booking_the_developer = models.BooleanField('Возможность закрепить Подрядчика')
    developer_contact = models.BooleanField('Возможность получить контакты Подрядчика')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField('Название компании', max_length=200)
    phone = models.CharField('Телефон', max_length=200)
    tariff = models.ForeignKey(Tariff, related_name='users', on_delete=models.PROTECT)
    paid_to = models.DateField('Оплачено до:')
    # Поле должно быть высчитываемым, но пока не знаю как сделать, оставлю просто число.
    orders_paid = models.IntegerField('Оплаченных заказов осталось')

    def __str__(self):
        return self.name

class User(models.Model):
    company = models.ForeignKey(Company, related_name='users', on_delete=models.PROTECT)
    name = models.CharField('ФИО пользователя', max_length=200)
    phone = models.CharField('Телефон', max_length=200, null=True, blank=True)
    telegram = models.CharField('Телеграм', max_length=200)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField('ФИО разработчика', max_length=200)
    phone = models.CharField('Телефон', max_length=200, null=True, blank=True)
    telegram = models.CharField('Телеграм', max_length=200)
    access_to_orders = models.BooleanField('Есть ли доступ к заказам')

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField('ФИО менеджера', max_length=200)
    phone = models.CharField('Телефон', max_length=200, null=True, blank=True)
    telegram = models.CharField('Телеграм', max_length=200)

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField('ФИО пользователя', max_length=200)
    phone = models.CharField('Телефон', max_length=200, null=True, blank=True)
    telegram = models.CharField('Телеграм', max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.PROTECT)
    description = models.TextField('Описание заказа')
    order_time = models.DateTimeField('Время получения заказ', auto_now_add=True)
    # Должно ставиться автоматически при приеме в работу
    answer_time = models.DateTimeField('Время ответа на заказ')
    developer = models.ForeignKey(Developer, related_name='orders', on_delete=models.PROTECT)
    complet = models.BooleanField('Выполнен ли заказ')
    # Должно ставиться автоматичеки при завершении заказа
    comleted_time = models.DateTimeField('Время выполнения')


class Conversions(models.Model):
    order = models.ForeignKey(Order, related_name='conversations', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='details', on_delete=models.PROTECT)
    developer = models.ForeignKey(Developer, related_name='questions', on_delete=models.PROTECT)



