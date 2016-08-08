# -*- coding: utf-8 -*-
from django.db import models

class Asset(models.Model):
	asset_name = models.CharField(verbose_name = "название актива", max_length = 100, unique=True)

	class Meta:
		verbose_name = "актив"
		verbose_name_plural = "активы"

	def __unicode__(self):
		return self.asset_name

	def __str__(self):
		return self.asset_name


class Beneficiary(models.Model):
	ben_name = models.CharField(verbose_name = "имя", max_length = 50)
	ben_lastname = models.CharField(verbose_name = "фамилия", max_length = 100)
	ben_midname = models.CharField(verbose_name = "отчество", max_length = 30, blank = True)
	ben_holding = models.CharField(verbose_name = "холдинговая компания бенефициара", max_length = 70, blank = True)

	class Meta:
		unique_together = ('ben_name', 'ben_lastname', 'ben_midname',)
		ordering = ['ben_lastname', 'ben_name']
		verbose_name = "бенефициар"
		verbose_name_plural = "бенефициары"
	
	def clean(self):
		self.ben_name = self.ben_name.capitalize()
		self.ben_lastname = self.ben_lastname.capitalize()

	def __unicode__(self):
		return self.ben_lastname

	def __str__(self):
		return self.ben_lastname



class Offshore(models.Model):
	off_name = models.CharField(verbose_name = "название офшора", max_length = 50, unique=True)
	off_jurisdiction = models.CharField(verbose_name = "юрисдикция офшора", max_length = 50, blank = True)
	file = models.FileField(upload_to = "offshores/", blank = True, null = True)
	image = models.ImageField(upload_to = "offshores/", blank = True, null = True)
	off_parent = models.CharField(verbose_name = "материнский офшор", max_length = 50, blank = True)

	class Meta:
		verbose_name = "офшор"
		verbose_name_plural = "офшоры"

	def clean(self):
		self.off_name = self.off_name.title()

	# def clean(self):
	# 	self.off_name = self.off_name.uppercase()

	def __unicode__(self):
		return self.off_name

	def __str__(self):
		return self.off_name

	def image_thumb(self):
		return '<img src="/media/%s" width="100" height="100" />' % (self.image)
	image_thumb.allow_tags = True
	
class AssetsBeneficiaries(models.Model):
	beneficiary = models.ForeignKey(Beneficiary,verbose_name = "бенефициар", on_delete = models.SET(""))
	asset = models.ForeignKey(Asset, verbose_name = "актив", on_delete = models.SET(""))
	share = models.DecimalField(verbose_name = "доля бенефициара в активе, %", max_digits = 6, decimal_places = 4, blank = True, default = 0.0)
	rel_date = models.DateField(verbose_name = "дата актуальности", null = True, blank = True)
	source = models.CharField(verbose_name = "источник", max_length = 150, blank = True)

	class Meta:
		verbose_name = "Бенефициар-Актив"
		verbose_name_plural = "Бенефициры-Активы"

	def __unicode__(self):
		return "связь"

	def __str__(self):
		return "связь"


class BeneficiariesOffshores(models.Model):
	beneficiary = models.ForeignKey(Beneficiary, verbose_name = "бенефициар", on_delete = models.SET(""))
	offshore = models.ForeignKey(Offshore, verbose_name = "офшор", on_delete = models.SET(""))
	share = models.DecimalField(verbose_name = "доля бенефициара в офшоре, %", max_digits = 7, decimal_places = 4, blank = True, default = 0.0)
	rel_date = models.DateField(verbose_name = "дата актуальности", blank = True, null = True)
	source = models.CharField(verbose_name = "источник", max_length = 150, blank = True)

	class Meta:
		verbose_name = "Офшор-Бенефициар"
		verbose_name_plural = "Офшоры-Бенефициары"



class OffshoresAssets(models.Model):
	offshore = models.ForeignKey(Offshore, verbose_name = "офшор", on_delete = models.SET(""))
	asset = models.ForeignKey(Asset, verbose_name = "актив", on_delete = models.SET(""))
	share = models.DecimalField(verbose_name = "доля офшора в активе, %", max_digits = 6, decimal_places = 4, blank = True, default = 0.0)
	rel_date = models.DateField(verbose_name = "дата актуальности", blank = True, null = True)
	source = models.CharField(verbose_name = "источник", max_length = 150, blank = True)

	class Meta:
		verbose_name = "Офшор-Актив"
		verbose_name_plural = "Офшоры-Активы"


