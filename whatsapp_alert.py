#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WhatsApp提醒模塊 - 使用Smithery MCP發送WhatsApp通知
"""

import os
import requests
from datetime import datetime
import json

# WhatsApp MCP URL
WHATSAPP_MCP_URL = "https://smithery.ai/server/@jlucaso1/whatsapp-mcp-ts"

def send_whatsapp_alert(phone_number, message):
    """
    使用Smithery WhatsApp MCP發送WhatsApp消息
    
    參數:
    phone_number (str): 目標手機號碼，需要包含國家代碼，如 "85298765432"
    message (str): 要發送的消息文本
    
    返回:
    bool: 是否成功發送
    """
    try:
        # 檢查環境變數中是否有MCP配置
        api_key = os.getenv("WHATSAPP_MCP_KEY", "")
        session_name = os.getenv("WHATSAPP_SESSION_NAME", "0xAICryptoCat")
        
        # 如果沒有API KEY，則不能發送
        if not api_key:
            print("缺少WhatsApp MCP API Key，無法發送WhatsApp消息")
            return False
        
        # 構建MCP請求體
        payload = {
            "phone": phone_number,  # 包含國家代碼的手機號碼
            "message": message,      # 消息文本
            "session_name": session_name  # 會話名稱，用於識別發送者
        }
        
        # 設置請求頭
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "0xAICryptoCat/1.0"
        }
        
        # 發送請求到WhatsApp MCP
        response = requests.post(
            f"{WHATSAPP_MCP_URL}/send-message",
            json=payload,
            headers=headers,
            timeout=15
        )
        
        # 檢查响應
        if response.status_code == 200:
            result = response.json()
            print(f"WhatsApp消息已成功發送到 {phone_number}")
            return True
        else:
            print(f"WhatsApp消息發送失敗: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"WhatsApp消息發送錯誤: {str(e)}")
        return False

def format_crypto_alert(symbol, timeframe, strategy_name, score, entry_point, target_price, stop_loss, confidence):
    """
    格式化加密貨幣提醒消息，適合WhatsApp顯示
    
    參數:
    symbol (str): 加密貨幣符號，如 'BTC/USDT'
    timeframe (str): 時間框架
    strategy_name (str): 策略名稱
    score (float): 策略評分
    entry_point (str): 進場點描述
    target_price (str): 目標價格
    stop_loss (str): 止損位置
    confidence (float): 信心水平
    
    返回:
    str: 格式化的WhatsApp消息
    """
    # 添加表情符號和格式化文本，使消息在WhatsApp中更易讀
    message = f"""🚨 *交易提醒: {symbol}*
    
📊 *{strategy_name} [{score}分]*
⏱️ 時間框架: {timeframe}
    
📍 *進場點:* {entry_point}
🎯 *目標價:* {target_price}
🛑 *止損位:* {stop_loss}
    
🔍 信心水平: {confidence*100:.1f}%
    
⏰ 提醒時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
訪問 https://0xaicryptocat.zeabur.app 獲取更多詳情
    
_0xAI CryptoCat - AI驅動的加密貨幣分析平台_
"""
    return message

def test_whatsapp_alert(phone_number="85298765432"):
    """
    發送測試WhatsApp消息
    
    參數:
    phone_number (str): 目標手機號碼，需要包含國家代碼，如 "85298765432"
    
    返回:
    bool: 是否成功發送
    """
    try:
        test_message = format_crypto_alert(
            symbol="BTC/USDT", 
            timeframe="1h", 
            strategy_name="測試策略", 
            score=9.5, 
            entry_point="當前價格附近", 
            target_price="上漲5-8%", 
            stop_loss="下跌2%處", 
            confidence=0.85
        )
        
        return send_whatsapp_alert(phone_number, test_message)
    
    except Exception as e:
        print(f"測試WhatsApp提醒錯誤: {str(e)}")
        return False

# 檢查WhatsApp MCP連接狀態
def check_whatsapp_connection():
    """
    檢查WhatsApp MCP連接狀態
    
    返回:
    dict: 連接狀態信息
    """
    try:
        # 獲取API密鑰
        api_key = os.getenv("WHATSAPP_MCP_KEY", "")
        session_name = os.getenv("WHATSAPP_SESSION_NAME", "0xAICryptoCat")
        
        # 如果沒有API KEY，則無法檢查
        if not api_key:
            return {"status": "error", "message": "缺少WhatsApp MCP API Key"}
        
        # 設置請求頭
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "0xAICryptoCat/1.0"
        }
        
        # 發送請求到WhatsApp MCP狀態端點
        response = requests.get(
            f"{WHATSAPP_MCP_URL}/session/status?session_name={session_name}",
            headers=headers,
            timeout=15
        )
        
        # 檢查響應
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": "error", "code": response.status_code, "message": response.text}
            
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # 測試代碼
    status = check_whatsapp_connection()
    print(f"WhatsApp連接狀態: {status}")
    
    # 如果想測試發送消息，取消下面的註釋並填入有效的手機號碼
    # test_whatsapp_alert("8529XXXXXXXX")  # 替換為有效的手機號碼 