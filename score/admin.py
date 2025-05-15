from django.contrib import admin
from .models import Student, FoodManagement, FashionDesign, StylingDesign

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('admit_number', 'name', 'id_last_4_digits')
    search_fields = ('admit_number', 'name', 'id_last_4_digits')

@admin.register(FoodManagement)
class FoodManagementAdmin(admin.ModelAdmin):
    list_display = ('student', 'food_identification', 'utensil_identification', 'total_score')
    search_fields = ('student__admit_number', 'student__name')

@admin.register(FashionDesign)
class FashionDesignAdmin(admin.ModelAdmin):
    list_display = ('student', 'basic_sewing', 'creative_drawing', 'total_score')
    search_fields = ('student__admit_number', 'student__name')

@admin.register(StylingDesign)
class StylingDesignAdmin(admin.ModelAdmin):
    list_display = ('student', 'basic_sewing', 'color_drawing', 'total_score')
    search_fields = ('student__admit_number', 'student__name')
