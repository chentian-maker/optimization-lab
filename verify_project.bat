
@echo off
setlocal

cd /d "%~dp0"

echo ========================================
echo   Optimization-Lab Verification
echo ========================================

echo.
echo [1/3] Checking Python environment...

if not exist ".venv\Scripts\python.exe" (
    echo [FAILED] Virtual environment not found.
    exit /b 1
)

set "PYTHON=.venv\Scripts\python.exe"

"%PYTHON%" --version
if errorlevel 1 goto failed

echo.
echo [2/3] Running unit tests...

"%PYTHON%" -m unittest discover -s tests -v
if errorlevel 1 goto failed

echo.
echo [3/3] Running Optimization-Lab...

"%PYTHON%" -m optimization_lab
if errorlevel 1 goto failed

echo.
echo ========================================
echo   ALL VERIFICATIONS PASSED
echo ========================================

exit /b 0

:failed
echo.
echo ========================================
echo   VERIFICATION FAILED
echo ========================================

exit /b 1
