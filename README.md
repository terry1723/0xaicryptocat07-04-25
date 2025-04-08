# GentsClub XAI - 標準普爾500指數(SPX)分析工具

## 簡介

GentsClub XAI 是一個多模型 AI 驅動的標準普爾500指數(SPX)技術與市場情緒分析工具，使用 Streamlit 構建的互動式儀表板，提供即時市場分析。

### 版本資訊

**當前版本**: v1.0.0 (SPX專用版)

**特色功能**:
- 專注於標準普爾500指數(SPX)的AI驅動分析
- 支持多種時間框架分析（1小時、4小時、1天等）
- 整合結構市場理論(SMC)分析
- 支持供需水平(SNR)分析
- 透過WhatsApp自動發送高評分交易機會提醒

## 功能特點

- **多來源數據獲取**: 使用 Yahoo Finance API 作為主要數據源，同時備有Alpha Vantage作為備用數據源
- **AI 驅動分析**: 整合 DeepSeek V3 和 GPT-4o-mini 進行市場和技術分析
- **智能市場結構分析**: 使用 SMC (Smart Money Concept) 和 SNR (Supply and Demand) 分析方法
- **完整的技術指標**: 包括移動平均線、RSI、支撐阻力位等
- **交互式圖表**: 即時更新的價格圖表和技術指標
- **交易建議**: 基於 AI 分析提供交易建議
- **WhatsApp通知**: 自動檢測高分交易策略並發送提醒

## 數據來源優先順序

1. Yahoo Finance API (主要數據源)
2. Alpha Vantage API (備用數據源)
3. 內部SPX數據模型 (備用方案)

## 安裝與運行

### 需求

- Python 3.8+
- Pip

### 安裝步驟

1. 複製儲存庫
```
git clone https://github.com/terry1723/gentsclubXAI.git
cd gentsclubXAI
```

2. 安裝依賴
```
pip install -r requirements.txt
```

3. 配置環境變數 (.env 文件)
```
WHATSAPP_MCP_KEY=your_whatsapp_key
WHATSAPP_SESSION_NAME=your_session_name
```

4. 運行應用
```
streamlit run app.py
```

## Zeabur 部署

本應用專為 Zeabur 平台部署優化，部署時需要設置以下環境變數：
- `WHATSAPP_MCP_KEY` (可選，如不設置將使用模擬器模式)
- `WHATSAPP_SESSION_NAME` (可選，默認為"GentsClubXAI")

## 使用的 AI 模型

- DeepSeek V3 (技術分析和整合分析)
- GPT-4o-mini (市場情緒分析)

## 作者

Terry Lee 