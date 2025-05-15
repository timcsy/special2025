# 台南家齊高中特色招生查詢成績系統

## Goal
### State
Objective: 建立台南家齊高中特色招生查詢成績網站，提供考生以准考證號碼與身分證後四碼查詢各術科考試成績
Current:   初始規劃階段
Next:      建立 Django 專案並設計資料模型

### Tasks
- [ ] 建立 Django 專案架構
- [ ] 設計資料庫模型 (匯入 excel 資料)
- [ ] 實現成績查詢功能 (依准考證號碼與身分證後四碼)
- [ ] 設計美觀直覺的使用者介面
- [ ] 部署系統

## Flow
### Thoughts
1. 將使用 Django 框架搭配 SQLite 資料庫
2. 從 excel 匯入資料，術科包括：餐飲管理科、流行服飾科、整體造型特色班
3. 每個術科有不同的考科結構
4. 只儲存身分證字號後四碼，確保資料安全
5. 查詢介面需直觀易用，不需太多說明即可操作
6. 顯示內容包括：准考證號、姓名、術科名稱、考科成績、術科總成績

### Logs
- 2025-05-14 · INIT (special.SPEC.md)

## Rule
### Domain
台南家齊高中特色招生入學系統

### System
ParentModules: .
Submodules:    (AI 自動維護並追蹤變化)
Dependencies:  [Django](https://www.djangoproject.com/), [Pandas](https://pandas.pydata.org/) (Excel處理)