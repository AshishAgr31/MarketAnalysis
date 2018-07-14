from django.db import models


class Company(models.Model):
    """
    Name of company
    """
    name = models.CharField(max_length=50, verbose_name="Name of the company wrf moneyControl")
    url_id = models.CharField(max_length=15, verbose_name="url param needed for further call")


class QuarterDate(models.Model):
    """
    quarter wise date
    """
    date = models.CharField(max_length=50, verbose_name=" quarter wise date wrf moneyControl")


class Stats(models.Model):
    """
    profit in the particular quarter for particular company
    """
    profit = models.FloatField(verbose_name="profit in the particular quarter for particular company")
    company_id = models.ForeignKey(Company.pk)
    quarter_id = models.ForeignKey(QuarterDate.pk)
