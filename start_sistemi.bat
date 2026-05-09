@echo off
echo Duke nisur Sistemin e Monitorimit...
docker-compose down
docker-compose up -d
echo Dashboard-i eshte gati te: http://127.0.0.1:8080
pause