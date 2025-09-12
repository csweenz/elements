from django.db import models

class Element(models.Model):
    atomic_number = models.PositiveSmallIntegerField(primary_key=True)
    symbol = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=64)
    class Meta:
        db_table = "elements"
    def __str__(self): return f"{self.symbol} ({self.atomic_number})"

class PriceSource(models.Model):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=512, null=True, blank=True)
    class Meta:
        db_table = "price_sources"

class Feedstock(models.Model):
    feedstock_id = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128)
    class Meta:
        db_table = "feedstocks"

class ElementFeedstockWeight(models.Model):
    element = models.ForeignKey(Element, to_field="atomic_number", db_column="atomic_number", on_delete=models.CASCADE)
    feedstock = models.ForeignKey(Feedstock, to_field="feedstock_id", db_column="feedstock_id", on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=16, decimal_places=8, null=True, blank=True)
    class Meta:
        db_table = "element_feedstock_weights"
        unique_together = (("element","feedstock"),)

class ElementPrice(models.Model):
    element = models.ForeignKey(Element, to_field="atomic_number", db_column="atomic_number", on_delete=models.CASCADE)
    ts = models.DateTimeField()
    price = models.DecimalField(max_digits=18, decimal_places=6)
    currency = models.CharField(max_length=3, default="USD")
    unit = models.CharField(max_length=32, default="USD/unit")
    source = models.ForeignKey(PriceSource, null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        db_table = "element_prices"
        constraints = [
            models.UniqueConstraint(fields=["element","ts"], name="uq_element_ts")
        ]
        indexes = [
            models.Index(fields=["ts","element"]),
        ]

class FeedstockPrice(models.Model):
    feedstock = models.ForeignKey(Feedstock, to_field="feedstock_id", db_column="feedstock_id", on_delete=models.CASCADE)
    ts = models.DateTimeField()
    price = models.DecimalField(max_digits=18, decimal_places=6)
    currency = models.CharField(max_length=3, default="USD")
    unit = models.CharField(max_length=32, default="USD/unit")
    source = models.ForeignKey(PriceSource, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "feedstock_prices"
        constraints = [
            models.UniqueConstraint(fields=["feedstock","ts"], name="uq_feedstock_ts")
        ]
        indexes = [
            models.Index(fields=["ts","feedstock"]),
        ]
