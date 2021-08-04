from django.db import models


class Property(models.Model):
    """Model used to represent Properties"""

    address = models.CharField(max_length=120)
    city = models.CharField(max_length=32)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "property"
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"Property-{self.pk}"

    @property
    def get_status_name(self):
        last_status = self.statushistory_set.last()
        if last_status:
            return self.statushistory_set.last().status.name
        return ""


class Status(models.Model):
    """Model used to represent property status"""

    name = models.CharField(unique=True, max_length=32)
    label = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = "status"
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __str__(self):
        return f"Status-{self.name}"


class StatusHistory(models.Model):
    """Model used to store every property status changes"""

    property = models.ForeignKey(Property, models.DO_NOTHING)
    status = models.ForeignKey(Status, models.DO_NOTHING)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "status_history"
        verbose_name = "StatusHistory"
        verbose_name_plural = "StatusHistory"
