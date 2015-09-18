import datetime
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils.translation import ugettext as _
from project.models import Project


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=254, null=True, blank=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Inventory Categories'


class InventoryAccount(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100)
    account_no = models.PositiveIntegerField()
    current_balance = models.FloatField(default=0)
    opening_balance = models.FloatField(default=0)

    def __unicode__(self):
        return str(self.account_no) + ' [' + self.name + ']'

    def get_absolute_url(self):
        return '/inventory_account/' + str(self.id)

    @staticmethod
    def get_next_account_no():
        from django.db.models import Max

        max_voucher_no = InventoryAccount.objects.all().aggregate(Max('account_no'))['account_no__max']
        if max_voucher_no:
            return max_voucher_no + 1
        else:
            return 1

    def get_category(self):
        try:
            item = self.item
        except:
            return None
        try:
            category = item.category
        except:
            return None
        return category

    def add_category(self, category):
        category_instance, created = Category.objects.get_or_create(name=category)
        self.category = category_instance

    def get_all_categories(self):
        return self.category.get_ancestors(include_self=True)

    categories = property(get_all_categories)


class Item(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    account = models.OneToOneField(InventoryAccount, related_name='item', null=True)
    type_choices = [('consumable', _('Consumable')), ('non-consumable', _('Non-Consumable'))]
    type = models.CharField(choices=type_choices, max_length=15, default='consumable')
    unit = models.CharField(max_length=50, default=_('pieces'))


class Demand(models.Model):
    purpose = models.CharField(max_length=254)
    date = models.DateField(default=datetime.datetime.today)
    site = models.ForeignKey(Project, related_name='demands')

    def __unicode__(self):
        return "{0}, {1}, {2}".format(self.site.name, self.date, self.purpose)


class DemandRow(models.Model):
    purpose = models.CharField(max_length=100, null=True, blank=True)
    item = models.ForeignKey(Item)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    fulfilled_quantity = models.FloatField()
    status = models.BooleanField(default=False)
    demand = models.ForeignKey(Demand, related_name='rows')

    def __unicode__(self):
        return "{0}".format(self.item)