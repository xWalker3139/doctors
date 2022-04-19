from django.contrib import admin
from .models import Patients, Prescription, X_Ray_Reports, Scan_Report

admin.site.register(Patients)
admin.site.register(Prescription)
admin.site.register(X_Ray_Reports)
admin.site.register(Scan_Report)

# Register your models here.
