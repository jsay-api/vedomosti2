# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

# Admin customization
admin.site.site_header = "Ведомости | База офшоров"
admin.site.site_title = "| Vedomosti"
admin.site.index_title = "Администрирование сайта"


class ABInline(admin.StackedInline):
	model = AssetsBeneficiaries
	extra = 0


class OAInline(admin.StackedInline):
	model = OffshoresAssets
	extra = 0


class BOInline(admin.StackedInline):
	model = BeneficiariesOffshores
	extra = 0


class AssetModelAdmin(admin.ModelAdmin):
	list_display = ["asset_name"]
	search_fields = ["asset_name"]
	# inlines = [ABInline, OAInline]
	class Meta:
		model = Asset


class BeneficiaryModelAdmin(admin.ModelAdmin):
	list_display = ["ben_name", "ben_lastname", "ben_midname", "ben_holding"]
	list_display_links = ["ben_lastname"]
	search_fields = ["ben_name", "ben_lastname", "ben_holding"]
	inlines = [ABInline]
	# list_editable = ["ben_name"]
	class Meta:
		model = Beneficiary


class OffshoreModelAdmin(admin.ModelAdmin):
	list_display = ["off_name", "off_jurisdiction", "off_parent"]
	list_display_links = ["off_name"]
	search_fields = ["off_name", "off_jurisdiction", "off_parent"]
	inlines = [BOInline, OAInline]
	class Meta:
		model = Offshore



# class ABModelAdmin(admin.ModelAdmin):
# 	list_display = ["asset", "beneficiary"]
# 	search_fields = ["asset", "beneficiary"]
# 	class Meta:
# 		model = AssetsBeneficiaries


# class BOModelAdmin(admin.ModelAdmin):
# 	list_display = ["beneficiary", "offshore"]
# 	list_filter = ["beneficiary", "offshore"]
# 	search_fields = ["beneficiary", "offshore"]
# 	class Meta:
# 		model = BeneficiariesOffshores


# class OAModelAdmin(admin.ModelAdmin):
# 	list_display = ["offshore", "asset"]
# 	search_fields = ["offshore", "asset"]
# 	class Meta:
# 		model = OffshoresAssets


admin.site.register(Asset, AssetModelAdmin)
admin.site.register(Beneficiary, BeneficiaryModelAdmin)
admin.site.register(Offshore, OffshoreModelAdmin)
# admin.site.register(AssetsBeneficiaries, ABModelAdmin)
# admin.site.register(BeneficiariesOffshores, BOModelAdmin)
# admin.site.register(OffshoresAssets, OAModelAdmin)