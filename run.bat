@echo off
chcp 65001 >nul
echo 正在安装依赖包...
pip install -r requirements.txt
echo.
echo 正在启动程序...
python main.py
echo.
pause
