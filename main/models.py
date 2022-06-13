from django.conf import settings
from django.db import models

class Parent1(models.Model):
	full_name = models.CharField("ФИО", max_length = 100, null=True)
	status = models.CharField("Статус", max_length = 10, null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15, null=True)
	email = models.EmailField(max_length = 50, null=True)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)

	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = "Родитель №1"
		verbose_name_plural = "Список родителей(опекунов) №1" 


class Parent2(models.Model):
	full_name = models.CharField("ФИО", max_length = 100)
	status = models.CharField("Статус", max_length = 10)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	email = models.EmailField(max_length = 50)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)

	def __str__(self):
		return self.full_name

	class Meta:
		verbose_name = "Родитель №2"
		verbose_name_plural = "Список родителей(опекунов) №2" 


class Kid(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Ребенок"
		verbose_name_plural = "Список детей" 

#Начало отрядов
class Squad20(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №20"
		verbose_name_plural = "Отряд №20" 


class Squad19(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №19"
		verbose_name_plural = "Отряд №19"

class Squad18(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №18"
		verbose_name_plural = "Отряд №18"

class Squad17(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №17"
		verbose_name_plural = "Отряд №17"

class Squad16(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №16"
		verbose_name_plural = "Отряд №16"

class Squad15(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №15"
		verbose_name_plural = "Отряд №15"


class Squad14(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №14"
		verbose_name_plural = "Отряд №14"

class Squad13(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №13"
		verbose_name_plural = "Отряд №13"

class Squad12(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №12"
		verbose_name_plural = "Отряд №12"

class Squad11(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №11"
		verbose_name_plural = "Отряд №11"

class Squad10(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №10"
		verbose_name_plural = "Отряд №10"

class Squad9(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №9"
		verbose_name_plural = "Отряд №9"

class Squad8(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №8"
		verbose_name_plural = "Отряд №8"

class Squad7(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №7"
		verbose_name_plural = "Отряд №7"

class Squad6(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №6"
		verbose_name_plural = "Отряд №6"

class Squad5(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №5"
		verbose_name_plural = "Отряд №5"

class Squad4(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №4"
		verbose_name_plural = "Отряд №4"

class Squad3(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №3"
		verbose_name_plural = "Отряд №3"

class Squad2(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №2"
		verbose_name_plural = "Отряд №2"

class Squad1(models.Model):
	passportDetails = models.CharField("Паспортные данные/Свидетельство о рождении", max_length = 100)
	copyPassport = models.ImageField("Копия паспорта", upload_to = "passports/", null=True)
	kidFullName = models.CharField("ФИО", max_length = 100)
	birthDate = models.DateField("Дата Рождения", null=True)
	phone_number = models.CharField("Номер телефона", max_length = 15)
	address = models.CharField("Адрес по месту прописки", max_length = 100)
	user_agreement = models.BooleanField("Пользовательское соглашение", default=True)
	snils = models.CharField("СНИЛС", max_length = 20, null=True)
	polis = models.CharField("Полис", max_length = 20, null=True)
	copyVaccSertificate = models.ImageField("Копия сертификата о прививках", upload_to = "VaccSertificate/", null=True)
	BSZH = models.DateField("Дата прививки БЦЖ", null=True)
	AKDS = models.DateField("Дата прививки АКДС", null=True)
	poliomielit = models.DateField("Дата прививки от полиомиелита", null=True)
	refusal_vaccinations = models.BooleanField("Отказ от прививок", default=False)
	medExit = models.BooleanField("Имеется медотвод", default=False)
	trainTicketThere = models.BooleanField("Билет туда", default=False)
	trainTicketBack = models.BooleanField("Билет обратно", default=False)


	def __str__(self):
		return self.kidFullName

	class Meta:
		verbose_name = "Отряд №1"
		verbose_name_plural = "Отряд №1"
