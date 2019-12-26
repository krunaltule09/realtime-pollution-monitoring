from django.db import models

class phdb(models.Model):
    value=models.DecimalField(max_digits=4,decimal_places=2)
    timestamp=models.DateTimeField()

    def __str__(self):
        return "time:-{}, ph:-{}".format(self.timestamp,self.value)

class sounddb(models.Model):
    value=models.DecimalField(max_digits=4,decimal_places=2)
    timestamp=models.DateTimeField()

    def __str__(self):
        return "time:-{}, sound:-{}".format(self.timestamp,self.value)


class gasdb(models.Model):
    value=models.DecimalField(max_digits=4,decimal_places=2)
    timestamp=models.DateTimeField()

    def __str__(self):
        return "time:-{}, gas:-{}".format(self.timestamp,self.value)