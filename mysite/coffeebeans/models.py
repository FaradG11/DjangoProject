from django.db import models

class Attributes(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class CoffeeKind(Attributes):
    pass


class RoastLevel(Attributes):
    pass


class Origin(Attributes):
    pass


class Coffeebean(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    kind = models.ForeignKey(CoffeeKind, on_delete=models.PROTECT, null=True)
    roast_level = models.ForeignKey(RoastLevel, on_delete=models.PROTECT, null=True)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT, null=True)
    methods = models.ManyToManyField("coffeebeans.Method")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Coffee #{self.id} {self.name!r}>"


class Method(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name
