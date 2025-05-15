import pandas as pd
from django.core.management.base import BaseCommand
from score.models import Student, FoodManagement, FashionDesign, StylingDesign

class Command(BaseCommand):
    help = '從Excel檔案匯入成績資料'

    def handle(self, *args, **kwargs):
        excel_file = '2025score.xlsx'
        
        # 匯入餐飲管理科資料
        self.import_food_management(excel_file)
        
        # 匯入流行服飾科資料
        self.import_fashion_design(excel_file)
        
        # 匯入整體造型特色班資料
        self.import_styling_design(excel_file)
        
        self.stdout.write(self.style.SUCCESS('成功匯入所有資料！'))
    
    def format_id_last_4_digits(self, value):
        """確保身分證末4碼總是4位數字的字符串"""
        # 轉為字符串並移除可能的小數點
        str_val = str(value).replace('.0', '')
        # 補足前導零，確保是4位數字
        return str_val.zfill(4)
    
    def import_food_management(self, excel_file):
        df = pd.read_excel(excel_file, sheet_name='餐飲管理科')
        for _, row in df.iterrows():
            # 先建立或取得學生資料
            student, created = Student.objects.update_or_create(
                admit_number=row['准考證號'],
                defaults={
                    'id_last_4_digits': self.format_id_last_4_digits(row['身份證末4碼']),
                    'name': row['姓名']
                }
            )
            
            # 建立或更新餐飲管理科成績
            FoodManagement.objects.update_or_create(
                student=student,
                defaults={
                    'food_identification': row['食材辨識'],
                    'utensil_identification': row['餐飲器具辨識'],
                    'total_score': row['術科總成績']
                }
            )
        
        self.stdout.write(self.style.SUCCESS(f'成功匯入餐飲管理科資料'))
    
    def import_fashion_design(self, excel_file):
        df = pd.read_excel(excel_file, sheet_name='流行服飾科')
        for _, row in df.iterrows():
            # 先建立或取得學生資料
            student, created = Student.objects.update_or_create(
                admit_number=row['准考證號'],
                defaults={
                    'id_last_4_digits': self.format_id_last_4_digits(row['身份證末4碼']),
                    'name': row['姓名']
                }
            )
            
            # 建立或更新流行服飾科成績
            FashionDesign.objects.update_or_create(
                student=student,
                defaults={
                    'basic_sewing': row['基礎設計手縫'],
                    'creative_drawing': row['創意繪圖'],
                    'total_score': row['術科總成績']
                }
            )
        
        self.stdout.write(self.style.SUCCESS(f'成功匯入流行服飾科資料'))
    
    def import_styling_design(self, excel_file):
        df = pd.read_excel(excel_file, sheet_name='整體造型特色班')
        for _, row in df.iterrows():
            # 先建立或取得學生資料
            student, created = Student.objects.update_or_create(
                admit_number=row['准考證號'],
                defaults={
                    'id_last_4_digits': self.format_id_last_4_digits(row['身份證末4碼']),
                    'name': row['姓名']
                }
            )
            
            # 建立或更新整體造型特色班成績
            StylingDesign.objects.update_or_create(
                student=student,
                defaults={
                    'basic_sewing': row['基礎設計手縫'],
                    'color_drawing': row['整體造型色彩繪圖'],
                    'total_score': row['術科總成績']
                }
            )
        
        self.stdout.write(self.style.SUCCESS(f'成功匯入整體造型特色班資料'))