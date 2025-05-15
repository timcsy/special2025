GUIDE.SPEC.md · Guide and Template (read-only)
=============================================

本檔為「契約」，AI Agent 必須嚴格遵守所有規則，不得偏離。

常用指令（給開發者）  
- 請閱讀 GUIDE.SPEC.md  
- NEXT／繼續  
- DONE／完成  
- SYNC／同步  

1. 載入與初始化  
   第一次輸入「請閱讀 GUIDE.SPEC.md」時，檢查 git status，如果還沒初始化存放庫，則 AI 自動執行：  
   git init && git config user.name "ai-agent" && git config user.email "agent@example.com" && git add -A && git commit -m "agent: init"  

2. 三種契約指令  
   - NEXT：推進到下一步  
   - DONE：標記完成狀態  
   - SYNC：全案同步  

3. 使用契約指令前後要進行的 Git 動作  
   無論是呼叫 SYNC、NEXT 還是 DONE，都要在操作前後各執行一次 Git 提交，確保備份：  
   - 操作前：  
     git add -A && git commit -m "agent: backup before <命令>"  
   - 執行命令（SYNC / NEXT / DONE）  
   - 操作後：  
     git add -A && git commit -m "agent: apply <命令> – <摘要>"  

4. 各命令行為  
   - SYNC／同步  
     1. backup before sync  
     2. 掃描所有資料夾並確認 `.SPEC.md`  
     3. 為缺檔資料夾建立骨架檔  
     4. 更新 Submodules 清單並追蹤變化  
     5. 自動勾選所有已完成但未打勾的 Tasks，並在 Logs 底部加入 `Auto-sync YYYY-MM-DD`  
     6. 在 Thoughts 底部記錄「本次同步原因」  
     7. 顯示「新增 N 檔、更新 M 檔」，詢問是否提交  
     8. backup apply sync  

   - NEXT／繼續  
     1. backup before next  
     2. 將 Goal.State.Next → State.Current，清空 Next  
     3. 在 Logs 底部新增 `<日期> · NEXT → Current`  
     4. 從未完成的 Tasks 中自動挑選下一項設為新的 Next；若所有 Tasks 已完成，提示「建議撰寫或更新測試」或「部署上線」  
     5. backup apply next  

   - DONE／完成  
     1. backup before done  
     2. 如果上下文對應某 Task，為該項打勾並在 Logs 記錄；否則將 State.Current 設為 Done、清空 Next  
     3. 提示「要撰寫或更新測試嗎？」或「要部署或上線嗎？」  
     4. backup apply done  

5. 檔案放置與命名  
   - 每個模組的 `.〈模組名〉.SPEC.md` 放在該模組資料夾根目錄  
   - 模組名可自訂；同一資料夾可有多個模組檔  

6. `.SPEC.md` 結構詳解  
   Goal  
   - State  
     - Objective：此模組要實現的核心功能或價值  
     - Current：當前具體狀況，包括進度、阻礙、環境或測試狀態等  
     - Next：下一步具體可執行行動  
   - Tasks：拆解 Objective 的子任務，完成後 AI 自動打勾  

   Flow  
   - Thoughts：設計思路、介面草稿、技術選擇、重構或同步原因等備註  
   - Logs：事件時間軸，記錄每次命令、NEXT→Current、DONE、Auto-sync 等操作  

   Rule  
   - Domain：此模組所屬的業務或功能範疇，描述責任與其他範疇互動方式  
   - System  
     - ParentModules：上層模組路徑，最頂層填 `.`  
     - Submodules：AI 自動維護並追蹤其變化  
     - Dependencies：Markdown 連結列出相依模組或第三方套件  

7. 骨架段（新建檔時複製並替換 `[[…]]`）  

# [[TITLE]]  

## Goal  
### State  
Objective: [[OBJECTIVE]]  
Current:   [[CURRENT]]  
Next:      [[NEXT]]  

### Tasks  
[[TASKS]]  

## Flow  
### Thoughts  
[[THOUGHTS]]  

### Logs  
- [[DATE]] · INIT (GUIDE.SPEC.md)  

## Rule  
### Domain  
[[DOMAIN]]  

### System  
ParentModules: [[PARENT_PATHS]]  
Submodules:    （AI 自動維護並追蹤變化）  
Dependencies:  [[DEPENDENCIES]]  
