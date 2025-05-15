# 台南家齊高中特色招生查詢成績系統

## Goal
### State
Objective: 建立台南家齊高中特色招生查詢成績網站，提供考生以准考證號碼與身分證後四碼查詢各術科考試成績
Current:   系統已完成開發，可供學生查詢成績
Next:      部署系統到生產環境

### Tasks
- [x] 建立 Django 專案架構
- [x] 設計資料庫模型 (匯入 2025score.xlsx 資料)
- [x] 實現成績查詢功能 (依准考證號碼與身分證後四碼)
- [x] 設計美觀直覺的使用者介面
- [x] 設定 Docker 容器化部署方案
- [x] 部署系統到容器環境
- [ ] 部署系統到生產線上環境

## Flow
### Thoughts
1. 將使用 Django 框架搭配 SQLite 資料庫
2. 從 2025score.xlsx 匯入資料，術科包括：餐飲管理科、流行服飾科、整體造型特色班
3. 每個術科有不同的考科結構
4. 只儲存身分證字號後四碼，確保資料安全
5. 查詢介面需直觀易用，不需太多說明即可操作
6. 顯示內容包括：准考證號、姓名、術科名稱、考科成績、術科總成績
7. 本次同步原因：完成了系統的主要功能開發，需要更新任務狀態並標記已完成項目

### Logs
- 2025-05-14 · INIT (special.SPEC.md)
- 2025-05-15 · Auto-sync 2025-05-15
- 2025-05-15 · 新增 Docker 部署配置
- 2025-05-15 · 成功部署到 Docker 容器環境

## Rule
### Domain
台南家齊高中特色招生入學系統

### System
ParentModules: .
Submodules:    score/.score.SPEC.md, special/.special.SPEC.md
Dependencies:  [Django](https://www.djangoproject.com/), [Pandas](https://pandas.pydata.org/) (Excel處理)