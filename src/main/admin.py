from django.contrib import admin
from main.models import Table1, Table2, Table3


class Table2Line(admin.StackedInline):
    model = Table2
    fields = ('text',)


class Table3Line(admin.TabularInline):
    model = Table3
    fields = ('val',)


class Table1Admin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    inlines = [Table2Line, Table3Line]


admin.site.register(Table1, Table1Admin)
