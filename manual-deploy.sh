#!/bin/bash
# 用於手動觸發Zeabur部署的腳本
# 使用方法: ./manual-deploy.sh [YOUR_ZEABUR_API_KEY] [YOUR_PROJECT_ID]

ZEABUR_API_KEY=$1
PROJECT_ID=$2

if [ -z "$ZEABUR_API_KEY" ] || [ -z "$PROJECT_ID" ]; then
  echo "請提供Zeabur API密鑰和項目ID"
  echo "使用方法: ./manual-deploy.sh [YOUR_ZEABUR_API_KEY] [YOUR_PROJECT_ID]"
  exit 1
fi

echo "觸發Zeabur部署..."
curl -X POST "https://api.zeabur.com/projects/$PROJECT_ID/deploy" \
  -H "Authorization: Bearer $ZEABUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"force": true}'

echo "部署請求已發送！" 