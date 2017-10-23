from django.db import models


class Table1Qs(models.QuerySet):
    def field1_a(self):
        return self.filter(fileld1='a')


class Table1Manager(models.Manager):
    def get_queryset(self):
        return Table1Qs(self.model, using=self.db)

class Table1(models.Model):
    name = models.CharField(max_length=255, null=False)
    value = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Value')
    field1 = models.CharField(max_length=20, null=False, unique=True)
    # tables4 = models.ManyToManyField('Table4', through='Table1_4', through_fields=['table1', 'table4'])
    tables4 = models.ManyToManyField('Table4')

    objects = models.Manager()
    objects2 = Table1Manager()

    class Meta:
        # app_label = 'main'
        # db_table = 'table1'
        ordering = ['name']
        # index_together = [('name','value')]
        # verbose_name = 'Table 1'
        # verbose_name_plural = 'Tables 1'
        # abstract = True


class Table2(models.Model):
    date = models.DateField()
    table1 = models.ForeignKey('Table1', related_name='tables2', null=False)


class Table3(models.Model):
    date = models.DateField()
    table1 = models.OneToOneField('Table1', related_name='table3', null=False)


# class Table1_4(models.Model):
#     table1 = models.ForeignKey('Table1')
#     table4 = models.ForeignKey('Table4')
#     table4_alt = models.ForeignKey('Table4')
#
#     class Meta:
#         unique_together = [('table1', 'table4')]


class Table4(models.Model):
    text = models.TextField()


