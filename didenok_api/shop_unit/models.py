from django.db import models

# Create your models here.
from shop_unit.validator import Validator as Val

unit_types = (
    ("OFFER", "Товар"),
    ("CATEGORY", "Категория"),
)
class ShopUnit(models.Model):
    id = models.CharField(primary_key=True, max_length=36, unique=True, null=False, validators=[Val.check_uuid])
    parentId = models.CharField(max_length=36, unique=False, null=True, blank=True, validators=[Val.check_uuid])
    type = models.CharField(max_length=100, choices=unit_types)
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(validators=[Val.check_date])
    price = models.IntegerField(null=True, blank=True)

