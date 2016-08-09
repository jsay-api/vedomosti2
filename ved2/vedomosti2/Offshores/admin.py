# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

# Admin customization
admin.site.site_header = "ВЕДОМОСТИ | ОФШОРЫ"
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
	list_per_page = 10
	class Meta:
		model = Asset

	def get_model_perms(self, request):
		"""
		Return empty perms dict thus hiding the model from admin index.
		"""
		return {}


class BeneficiaryModelAdmin(admin.ModelAdmin):
	
	list_display_links = ["ben_lastname"]
	search_fields = ["ben_name", "ben_lastname", "ben_holding"]
	# inlines = [ABInline]
	list_display = ["ben_name", "ben_lastname", "ben_midname", "ben_holding"]
	list_per_page = 10
	# list_editable = ["ben_name"]
	class Meta:
		model = Beneficiary

	def get_model_perms(self, request):
		return {}


class OffshoreModelAdmin(admin.ModelAdmin):
	list_display = ["off_name", "off_jurisdiction", "off_parent", "file", "image"]
	list_display_links = ["off_name"]
	search_fields = ["off_name", "off_jurisdiction", "off_parent"]
	fields = ["off_name", "off_jurisdiction", "off_parent", "file", "image", "image_thumb"]
	readonly_fields = ['image_thumb']
	list_per_page = 10
	# inlines = [BOInline, OAInline]
	class Meta:
		model = Offshore

	# def get_model_perms(self, request):
	# 	return {}


class ABModelAdmin(admin.ModelAdmin):
	list_display = ["ben_name", "beneficiary", "ben_midname", "ben_holding", "asset", "share", "rel_date", "source"]
	search_fields = ["asset__asset_name", "beneficiary__ben_lastname", "beneficiary__ben_name", "beneficiary__ben_midname", "beneficiary__ben_holding", "share",  "source"]
	list_filter = ["asset", "beneficiary", "source"]
	list_editable = ["share", "source"]
	list_display_links = ["beneficiary", "asset"]
	list_per_page = 10
	class Meta:
		model = AssetsBeneficiaries

	def ben_name(self, object):
		return object.beneficiary.ben_name
	ben_name.short_description = "имя бенефициара"

	def ben_midname(self, object):
		return object.beneficiary.ben_midname
	ben_midname.short_description = "отчество бенефициара"

	def ben_holding(self, object):
		return object.beneficiary.ben_holding
	ben_holding.short_description = "холдинговая компания"

	# def list_of_bens(self, obj):
	# 	return ("%s" % ','.join([ben.ben_lastname for be in obj.beneficiary.all()]))
	# list_of_bens.short_description = 'Beneficiaries'
	

class BOModelAdmin(admin.ModelAdmin):
	list_display = ["offshore", "off_jur", "off_prnt", "ben_name", "beneficiary", "ben_midname", "ben_holding", "share", "rel_date",  "source"]
	list_filter = ["beneficiary", "offshore", "source"]
	list_display_links = ["offshore", "beneficiary"]
	search_fields = ["beneficiary__ben_lastname", "beneficiary__ben_name", "beneficiary__ben_holding", "offshore__off_name", "offshore__off_jurisdiction", "offshore__off_parent", "source", "share", ]
	list_per_page = 10
	class Meta:
		model = BeneficiariesOffshores

	def ben_name(self, object):
		return object.beneficiary.ben_name
	ben_name.short_description = "имя бенефициара"

	def ben_lastname(self, object):
		return object.beneficiary.ben_lastname
	ben_lastname.short_description = "фамилия бенефициара"

	def ben_midname(self, object):
		return object.beneficiary.ben_midname
	ben_midname.short_description = "отчество бенефициара"

	def ben_holding(self, object):
		return object.beneficiary.ben_holding
	ben_holding.short_description = "холдинговая компания"

	def off_jur(self, object):
		return object.offshore.off_jurisdiction
	off_jur.short_description = "Юрисдикция офшора"

	def off_prnt(self, object):
		return object.offshore.off_parent
	off_prnt.short_description = "Материнский офшор"


class OAModelAdmin(admin.ModelAdmin):
	list_display = ["offshore", "off_jur", "off_prnt", "asset", "share", "rel_date",  "source"]
	list_filter = ["offshore", "asset", "source"]
	list_display_links = ["offshore", "asset"]
	search_fields = ["offshore__off_name", "offshore__off_jurisdiction", "offshore__off_parent", "asset__asset_name", "share",  "source"]
	list_per_page = 10
	class Meta:
		model = OffshoresAssets

	def off_jur(self, object):
		return object.offshore.off_jurisdiction
	off_jur.short_description = "Юрисдикция офшора"

	def off_prnt(self, object):
		return object.offshore.off_parent
	off_prnt.short_description = "Материнский офшор"

	# def ast_name(self, object):
	# 	return object.asset.asset_name
	# ast_name.short_description = "актив"


admin.site.register(Asset, AssetModelAdmin)
admin.site.register(Beneficiary, BeneficiaryModelAdmin)
admin.site.register(Offshore, OffshoreModelAdmin)
admin.site.register(AssetsBeneficiaries, ABModelAdmin)
admin.site.register(BeneficiariesOffshores, BOModelAdmin)
admin.site.register(OffshoresAssets, OAModelAdmin)