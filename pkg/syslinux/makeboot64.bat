@echo off
setlocal EnableDelayedExpansion
title %~nx0
rem 01/13/2016 - Added error routine and other minor changes by Robert Rubino
rem This batch file was modified by Steven Shiau.
rem The original one is from PDLA http://pendrivelinux.com
rem This batch file was created by ©2007 PDLA http://pendrivelinux.com
cd /d "%~dp0"
cls
echo -----------------------------------------------------------------
echo This batch file will prepare drive %~d0 for boot using syslinux64
echo --------------------- WARNING -----------------------------------
echo Run this file from your portable USB device ONLY.
echo.
echo Running this file from your hard drive may overwrite your current
echo Master Boot Record (MBR) and render your Windows Operating System
echo un-bootable. YOU HAVE BEEN WARNED.
echo.
echo This batch file is offered in hopes that it will be useful and
echo comes with absolutely no warranty. && echo. && echo *** USE AT YOUR OWN RISK ***
echo -------------------------------------------------------------------
pause
cls
if %~d0 == %systemdrive% (color 4f && echo Do not run %~nx0 from your local system hard drive. && echo It should only be run from your USB flash drive or USB hard drive. && goto end)
rem echo %~d0 | "%windir%\system32\findstr.exe" /B /I "%systemdrive%" && color 4f && echo You can _NOT_ RUN %~nx0 from your local system hard drive! It should only be run from your USB flash drive or USB hard drive. && goto end
echo.
echo Press any key to make drive %~d0 bootable
echo or close this window to abort...
pause > nul
cls
syslinux64.exe -d syslinux -mafi %~d0
if !errorlevel! neq 0 (
color 4f
echo.
echo ----------------------------
echo *** FATAL ERROR ***
echo *** %~d0 drive is not bootable for Clonezilla ***
echo *** %~nx0 should be run as Administrator ***
echo *** or other major failure has occurred ***
echo ----------------------------
goto end
)
echo.
echo ~~~~~~~~ Congratulations ~~~~~~~
echo The hidden file ldlinux.sys has been installed
echo Your %~d0 drive should now be bootable.
echo //NOTE// If your USB flash drive fails to boot (maybe buggy BIOS), try to use "syslinux64 -d syslinux -sfmar %~d0".
echo.
:end
echo.
cd /d %systemdrive%
echo *** Press any key to exit this window ***
pause > nul