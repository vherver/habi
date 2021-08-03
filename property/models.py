from django.db import models


class Property(models.Model):
    """Model used to represent Properties"""

    address = models.CharField(max_length=120, null=False)
    city = models.CharField(max_length=30, null=False)
    price = models.BigIntegerField(null=False)
    description = models.TextField()
    year = models.IntegerField()

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"Property-{self.pk}"


class Status(models.Model):
    """Model used to represent property status"""

    name = models.CharField(max_length=32, null=False)
    label = models.CharField(max_length=64, null=False)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return f"Status-{self.name}"


class StatusHistory(models.Model):
    """Model used to store every property status changes"""

    update_date = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "StatusHistory"
        verbose_name_plural = "StatusHistory"
