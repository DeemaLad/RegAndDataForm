from django.contrib import admin
from .models import Parent1, Parent2, Kid, Squad20, Squad19, Squad18, Squad17, Squad16, Squad15, Squad14, Squad13, Squad12, Squad11, Squad10, Squad9, Squad8, Squad7, Squad6, Squad5, Squad4, Squad3, Squad2, Squad1
from import_export.admin import ImportExportModelAdmin


class Parent1Admin(ImportExportModelAdmin):
	list_display = ["id", "full_name","status","phone_number", "email","user_agreement"]
	pass

class Parent2Admin(ImportExportModelAdmin):
	list_display = ["id", "full_name","status","phone_number", "email","user_agreement"]
	pass

class KidAdmin(ImportExportModelAdmin):
	list_display = ["id", "passportDetails","copyPassport","kidFullName", "birthDate","phone_number", "address","user_agreement","snils", "polis","copyVaccSertificate", "BSZH","copyPassport","AKDS", "poliomielit","refusal_vaccinations","medExit"]
	pass

admin.site.register(Parent1, Parent1Admin)
admin.site.register(Parent2, Parent2Admin)
admin.site.register(Kid,KidAdmin)
admin.site.register(Squad20)
admin.site.register(Squad19)
admin.site.register(Squad18)
admin.site.register(Squad17)
admin.site.register(Squad16)
admin.site.register(Squad15)
admin.site.register(Squad14)
admin.site.register(Squad13)
admin.site.register(Squad12)
admin.site.register(Squad11)
admin.site.register(Squad10)
admin.site.register(Squad9)
admin.site.register(Squad8)
admin.site.register(Squad7)
admin.site.register(Squad6)
admin.site.register(Squad5)
admin.site.register(Squad4)
admin.site.register(Squad3)
admin.site.register(Squad2)
admin.site.register(Squad1)



