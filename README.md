# 0xAI CryptoCat 加密貨幣分析儀表板

## 簡介

0xAI CryptoCat 是一個多模型 AI 驅動的加密貨幣技術與市場情緒分析工具，使用 Streamlit 構建的互動式儀表板，提供即時加密貨幣分析。

### 版本資訊

**當前版本**: v3.5.0 (Binance API 增強版)

**更新內容**:
- 優化 Binance API 連接和重試機制
- 增強價格合理性驗證系統
- 添加多交易所備選數據源 (Kucoin、OKX、Bybit、Gate.io、Huobi)
- 改進用戶界面和數據展示

## 功能特點

- **多來源數據獲取**: 使用 Binance API 作為主要數據源，同時備有多個備用數據源，確保數據可靠性
- **AI 驅動分析**: 整合 DeepSeek V3 和 GPT-4o-mini 進行市場和技術分析
- **智能市場結構分析**: 使用 SMC (Smart Money Concept) 和 SNR (Supply and Demand) 分析方法
- **完整的技術指標**: 包括移動平均線、RSI、支撐阻力位等
- **交互式圖表**: 即時更新的價格圖表和技術指標
- **交易建議**: 基於 AI 分析提供交易建議

## 數據來源優先順序

1. Binance API (主要數據源)
2. Crypto APIs (備用數據源)
3. Smithery MCP API
4. CoinCap API
5. CoinGecko API (價格驗證)

## 安裝與運行

### 需求

- Python 3.8+
- Pip

### 安裝步驟

1. 複製儲存庫
```
git clone https://github.com/terry1723/0xaicryptocat07-04-25.git
cd 0xaicryptocat07-04-25
```

2. 安裝依賴
```
pip install -r requirements.txt
```

3. 配置環境變數 (.env 文件)
```
CRYPTOAPIS_KEY=your_api_key
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret
```

4. 運行應用
```
streamlit run app.py
```

## Zeabur 部署

本應用專為 Zeabur 平台部署優化，部署時需要設置以下環境變數：
- `CRYPTOAPIS_KEY`
- `BINANCE_API_KEY`
- `BINANCE_API_SECRET`

## 使用的 AI 模型

- DeepSeek V3 (技術分析和整合分析)
- GPT-4o-mini (市場情緒分析)

## 作者

Terry Lee 