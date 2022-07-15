from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import models
from django.forms.models import model_to_dict


# Create your models here.

from shop_unit.validator import Validator

unit_types = (
    ("OFFER", "Товар"),
    ("CATEGORY", "Категория"),
)
class ShopUnit(models.Model):
    id = models.CharField(primary_key=True, max_length=36, unique=True, null=False)
    parentId = models.CharField(max_length=36, unique=False, null=True, blank=True)
    type = models.CharField(max_length=100, choices=unit_types, null=False)
    name = models.CharField(max_length=100, null=False)
    date = models.DateTimeField()
    price = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            Validator.check_uuid(self.id)
            Validator.check_date(self.date)

            if not self.type or len(self.type) == 0:
                raise ValidationError("Validation Failed")
            else:
                try:
                    unit = ShopUnit.objects.get(pk=self.id)
                    if unit.type != self.type:
                        raise ValidationError("Validation Failed")

                    if self.parentId:
                        parent = ShopUnit.objects.get(parentId=self.parentId)
                        if parent.type != "CATEGORY":
                            raise ValidationError("Validation Failed")
                except ObjectDoesNotExist:
                    pass

            if not self.name or len(self.name) == 0:
                raise ValidationError("Validation Failed")

        except ValidationError as e:
            raise ValidationError("Validation Failed")
        else:
            super(ShopUnit, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категории и товары'
        verbose_name_plural = 'Категория или товар'

