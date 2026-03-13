@echo off
title Kenwell Enterprise Launcher
echo [KO] CHECKING VIRTUAL DRIVE K:...

:: Try to mount if it doesn't exist
if not exist K:\ (
    echo [KO] MOUNTING SOVEREIGN DRIVE...
    subst K: "C:\Users\Kenwell"
)

if exist K:\ (
    echo [KO] DRIVE K: ACTIVE. STRIKING ENGINE...
    K:
    python -m streamlit run kenwell.py
) else (
    echo [KO] ERROR: UNABLE TO ASSIGN DRIVE K:
    echo [KO] FALLING BACK TO DIRECT PATH...
    cd /d "C:\Users\Kenwell"
    python -m streamlit run kenwell.py
)
pause