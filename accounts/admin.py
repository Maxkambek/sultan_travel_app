from django.contrib import admin
from .models import Account, AccountDetails, VerifyPhone


@admin.register(VerifyPhone)
class ModelNameAdmin(admin.ModelAdmin):
    pass


class AccountDetailsAdmin(admin.StackedInline):
    model = AccountDetails
    extra = 0


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountDetailsAdmin]
