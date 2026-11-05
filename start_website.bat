@echo off
title Shahad Alharabi Advertising - Web Server
color 06

echo =======================================================
echo   SHAHAD ALHARABI ADVERTISING - LOCAL WEB SERVER
echo   شركة شهد الحربي للدعاية والإعلان
echo   "Where Light Becomes Luxury"
echo =======================================================
echo.

cd /d "%~dp0"

echo [1/2] Opening website in your default browser...
start http://localhost:3000

echo [2/2] Starting server at http://localhost:3000 ...
echo Press Ctrl+C in this window anytime to stop the server.
echo.

npx -y serve -l 3000 -L .

pause
