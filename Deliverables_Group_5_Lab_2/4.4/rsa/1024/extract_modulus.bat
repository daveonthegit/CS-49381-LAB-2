@echo off
setlocal enabledelayedexpansion

REM Paths to openssl.exe and ssh-keygen.exe
set OPENSSL_PATH=C:\Program Files\OpenSSL-Win64\bin\openssl.exe
set SSH_KEYGEN_PATH=C:\Program Files\Git\usr\bin\ssh-keygen.exe

REM Create output directories if they don't exist
set OUTPUT_DIR=output
set ERROR_DIR=errors
mkdir "%OUTPUT_DIR%" 2>nul
mkdir "%ERROR_DIR%" 2>nul

REM Find the next available number for output files
set count=1
:find_number
if exist "%OUTPUT_DIR%\modulus_output_!count!.txt" (
    set /a count+=1
    goto find_number
)

REM Set output file names
set output_file=%OUTPUT_DIR%\modulus_output_!count!.txt
set error_log=%ERROR_DIR%\errors_!count!.log

echo Modulus Extraction Results > "%output_file%"
echo Errors will be saved to "%error_log%" > "%error_log%"

REM Temporary PEM file
set temp_pem=temp_key.pem

REM Loop through all .pub files in the current directory
for %%f in (*.pub) do (
    echo Processing %%f...
    echo ============================== >> "%output_file%"
    echo File: %%f >> "%output_file%"

    REM Check if the file contains "BEGIN" (PEM format check)
    type "%%f" | find "BEGIN" >nul
    if !errorlevel! equ 0 (
        "%OPENSSL_PATH%" rsa -pubin -in "%%f" -noout -modulus >> "%output_file%" 2>> "%error_log%"
    ) else (
        REM Convert OpenSSH to PEM and extract modulus
        "%SSH_KEYGEN_PATH%" -f "%%f" -e -m pem > "%temp_pem%" 2>> "%error_log%"
        if exist "%temp_pem%" (
            "%OPENSSL_PATH%" rsa -pubin -in "%temp_pem%" -noout -modulus >> "%output_file%" 2>> "%error_log%"
            del "%temp_pem%"
        ) else (
            echo Could not convert or extract modulus from %%f >> "%output_file%"
            echo [ERROR] %%f - Conversion failed >> "%error_log%"
        )
    )

    echo. >> "%output_file%"
)

echo.
echo Modulus extraction completed.
echo Results saved to: "%output_file%"
echo Errors saved to: "%error_log%"
pause
