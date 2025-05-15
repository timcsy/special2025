from django.db import models

class Student(models.Model):
    """考生基本資料模型"""
    admit_number = models.CharField(max_length=10, primary_key=True, verbose_name='准考證號')
    id_last_4_digits = models.CharField(max_length=4, verbose_name='身份證末4碼')
    name = models.CharField(max_length=20, verbose_name='姓名')

    def __str__(self):
        return f"{self.admit_number} - {self.name}"

    class Meta:
        verbose_name = '考生資料'
        verbose_name_plural = '考生資料'


class FoodManagement(models.Model):
    """餐飲管理科成績模型"""
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='food_score', verbose_name='考生')
    food_identification = models.FloatField(verbose_name='食材辨識')
    utensil_identification = models.FloatField(verbose_name='餐飲器具辨識')
    total_score = models.FloatField(verbose_name='術科總成績')

    def __str__(self):
        return f"{self.student.name} - 餐飲管理科 - {self.total_score}"

    class Meta:
        verbose_name = '餐飲管理科成績'
        verbose_name_plural = '餐飲管理科成績'


class FashionDesign(models.Model):
    """流行服飾科成績模型"""
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='fashion_score', verbose_name='考生')
    basic_sewing = models.FloatField(verbose_name='基礎設計手縫')
    creative_drawing = models.FloatField(verbose_name='創意繪圖')
    total_score = models.FloatField(verbose_name='術科總成績')

    def __str__(self):
        return f"{self.student.name} - 流行服飾科 - {self.total_score}"

    class Meta:
        verbose_name = '流行服飾科成績'
        verbose_name_plural = '流行服飾科成績'


class StylingDesign(models.Model):
    """整體造型特色班成績模型"""
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='styling_score', verbose_name='考生')
    basic_sewing = models.FloatField(verbose_name='基礎設計手縫')
    color_drawing = models.FloatField(verbose_name='整體造型色彩繪圖')
    total_score = models.FloatField(verbose_name='術科總成績')

    def __str__(self):
        return f"{self.student.name} - 整體造型特色班 - {self.total_score}"

    class Meta:
        verbose_name = '整體造型特色班成績'
        verbose_name_plural = '整體造型特色班成績'
