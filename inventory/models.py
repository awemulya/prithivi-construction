import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils.translation import ugettext as _
from django.db.models import F
from rest_framework.reverse import reverse_lazy
from ledger.models import Account
from project.models import Project
DEFAULT_PROJECT_ID = 2


def none_for_zero(obj):
    if not obj:
        return None
    else:
        return obj


def zero_for_none(obj):
    if obj is None:
        return 0
    else:
        return obj


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
    site = models.ForeignKey(Project, related_name='inventory_account')

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
        return category.name

    def add_category(self, category):
        category_instance, created = Category.objects.get_or_create(name=category)
        self.category = category_instance

    def get_all_categories(self):
        return self.category.get_ancestors(include_self=True)

    categories = property(get_all_categories)


class ConsumptionRow(models.Model):
    sn = models.PositiveIntegerField(default=1)
    account = models.ForeignKey(InventoryAccount, related_name='rows')
    quantity = models.FloatField(default=0.0)
    date = models.DateField(null=True)
    purpose = models.CharField(max_length=254, null=True)


class Item(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, null=True, blank=True)
    account = models.OneToOneField(InventoryAccount, related_name='item', null=True)
    type_choices = [('consumable', _('Consumable')), ('non-consumable', _('Non-Consumable'))]
    type = models.CharField(choices=type_choices, max_length=15, default='consumable')
    unit = models.CharField(max_length=50, default=_('pieces'))
    ledger = models.ForeignKey(Account, null=True)

    def save(self, *args, **kwargs):
        if not self.ledger_id:
            ledger = Account(name=self.name)
            ledger.save()
            self.ledger = ledger
        else:
            if not self.ledger.name == self.name:
                self.ledger.name = self.name
                self.ledger.save()
        super(Item, self).save(*args, **kwargs)


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


class JournalEntry(models.Model):
    date = models.DateField()
    content_type = models.ForeignKey(ContentType, related_name='inventory_journal_entries')
    model_id = models.PositiveIntegerField()
    creator = GenericForeignKey('content_type', 'model_id')

    @staticmethod
    def get_for(source):
        try:
            return JournalEntry.objects.get(content_type=ContentType.objects.get_for_model(source), model_id=source.id)
        except JournalEntry.DoesNotExist:
            return None

    def __str__(self):
        return str(self.content_type) + ': ' + str(self.model_id) + ' [' + str(self.date) + ']'

    class Meta:
        verbose_name_plural = u'InventoryJournal Entries'


class Transaction(models.Model):
    account = models.ForeignKey(InventoryAccount)
    dr_amount = models.FloatField(null=True, blank=True)
    cr_amount = models.FloatField(null=True, blank=True)
    current_balance = models.FloatField(null=True, blank=True)
    journal_entry = models.ForeignKey(JournalEntry, related_name='transactions')

    def __str__(self):
        return str(self.account) + ' [' + str(self.dr_amount) + ' / ' + str(self.cr_amount) + ']'


def alter(account, date, diff):
    Transaction.objects.filter(journal_entry__date__gt=date, account=account).update(
        current_balance=none_for_zero(zero_for_none(F('current_balance')) + zero_for_none(diff)))


def set_transactions(model, date, *args):
    args = [arg for arg in args if arg is not None]
    journal_entry, created = JournalEntry.objects.get_or_create(
        content_type=ContentType.objects.get_for_model(model), model_id=model.id,
        defaults={
            'date': date
        })

    for arg in args:
        matches = journal_entry.transactions.filter(account=arg[1])
        diff = 0
        if not matches:
            transaction = Transaction()
        else:
            transaction = matches[0]
            diff = zero_for_none(transaction.cr_amount)
            diff -= zero_for_none(transaction.dr_amount)
        if arg[0] == 'dr':
            transaction.dr_amount = float(arg[2])
            transaction.cr_amount = None
            diff += float(arg[2])
        elif arg[0] == 'cr':
            transaction.cr_amount = float(arg[2])
            transaction.dr_amount = None
            diff -= float(arg[2])
        else:
            raise Exception('Transactions can only be either "dr" or "cr".')
        transaction.account = arg[1]
        transaction.account.current_balance += diff
        transaction.current_balance = transaction.account.current_balance
        transaction.account.save()
        journal_entry.transactions.add(transaction)
        alter(transaction.account, date, diff)


class Party(models.Model):
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254, blank=True, null=True)
    phone_no = models.CharField(max_length=100, blank=True, null=True)
    pan_no = models.CharField(max_length=50, blank=True, null=True)
    account = models.ForeignKey(Account, null=True)

    def save(self, *args, **kwargs):
        if not self.account_id:
            account = Account(name=self.name)
            account.save()
            self.account = account
        super(Party, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Parties'


class PartyPayment(models.Model):
    party = models.ForeignKey(Party, related_name='rows')
    date = models.DateField(null=True)
    amount = models.FloatField(default=0.0)
    voucher_no = models.PositiveIntegerField(blank=True, null=True)


class Purchase(models.Model):
    party = models.ForeignKey(Party, related_name='purchase')
    voucher_no = models.PositiveIntegerField(blank=True, null=True)
    credit = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)

    @property
    def total(self):
        grand_total = 0
        for obj in self.rows.all():
            total = obj.quantity * obj.rate
            grand_total += total
        return grand_total

    def get_absolute_url(self):
        return reverse_lazy('purchase-detail', kwargs={'id': self.pk})


class PurchaseRow(models.Model):
    sn = models.PositiveIntegerField()
    item = models.ForeignKey(Item)
    quantity = models.FloatField()
    rate = models.FloatField()
    discount = models.FloatField(default=0)
    unit = models.CharField(max_length=50, default=_('pieces'))
    purchase = models.ForeignKey(Purchase, related_name='rows')

    def get_voucher_no(self):
        return self.purchase.voucher_no