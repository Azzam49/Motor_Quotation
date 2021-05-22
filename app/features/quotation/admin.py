from django.contrib import admin
from .models import Quotation

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    change_list_template = 'admin/snippets/snippets_change_list.html'

    def __str__(self):
        return self.name
