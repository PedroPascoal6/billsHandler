from django.db import models


class Bill(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    billDate = models.DateTimeField(default='1999-01-01T00:00:00.000000Z')
    amount = models.FloatField(default=0.0)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    owner = models.ForeignKey('auth.User', related_name='bills', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="bills/images/", null=True, blank=True)

    class Meta:
        ordering = ('created',)


class BillImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='billsImages', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="bills/images/", null=True, blank=True)

