@echo off
setlocal EnableDelayedExpansion
rem 12/21/2026 - replaced wmic with PowerShell command and changed to use batch file label subroutines
rem This batch file was modified by Tom Hoar.
rem 01/13/2016 - Added error routine and other minor changes by Robert Rubino
rem This batch file was modified by Steven Shiau.
rem The original one is from PDLA http://pendrivelinux.com
rem This batch file was created by ©2007 PDLA http://pendrivelinux.com

call :main %*

exit /b %ERRORLEVEL%


:main

  title %~nx0
  pushd "%~dp0"

  call :test-systemdrive
  if %ERRORLEVEL% neq 0 ( exit /b %ERRORLEVEL% )

  call :welcome

  call :test-filesystem
  if %ERRORLEVEL% neq 0 ( exit /b %ERRORLEVEL% )

  call :make-bootable
  if %ERRORLEVEL% equ 0 (
    call :success-message
  ) else (
    call :fail-message
  )

  echo *** Press any key to exit this window ***
  pause > nul
  color

  popd

exit /b %ERRORLEVEL%


:test-systemdrive
  if /i [%~d0] == [%SystemDrive%] (
    color 4f
    echo Do not run %~nx0 from your local system hard drive.
    echo It should only be run from your USB drive.
    exit /b 1
    rem echo %~d0 | "%windir%\system32\findstr.exe" /B /I "%SystemDrive%" && color 4f && echo You can _NOT_ RUN %~nx0 from your local system hard drive! It should only be run from your USB drive or USB drive. && goto end
  ) else (
    echo Pass. Target drive is not the SystemDrive ^(%SystemDrive%^)
  )
exit /b %ERRORLEVEL%


:welcome
  echo -----------------------------------------------------------------
  echo This batch file prepares drive %~d0 for boot using syslinux64
  echo --------------------- WARNING -----------------------------------
  echo Run this file from your portable USB drive ONLY.
  echo.
  echo Running this file from your hard drive may overwrite your current
  echo Master Boot Record (MBR) and render your Windows Operating System
  echo un-bootable. YOU HAVE BEEN WARNED.
  echo.
  echo This batch file is offered in hopes that it is useful and
  echo comes with absolutely no warranty.
  echo.
  echo *** USE AT YOUR OWN RISK ***
  echo -------------------------------------------------------------------
  REM cls
exit /b %ERRORLEVEL%


:test-filesystem

  REM Microsoft depricated wmic. Replace with Powershell
  REM wmic logicaldisk where caption="%~d0" get filesystem|find "FAT32">nul

  set "_letter=%~d0

  echo.
  echo Testing the filesystem on drive %_letter%. Please wait. . .

  REM Call PowerShell to get the file system type. Remove the colon (:) in variable
  for /f "delims=" %%f in ('PowerShell.exe -command "Get-Volume -DriveLetter "%_letter::=%" | Select-Object -ExpandProperty FileSystem"') do (
    set "FileSystem=%%f"
  )

  if [%FileSystem%] == [FAT32] (
    echo The target ^(USB^) drive is FAT32.
    set /a EXITCODE=0
  ) else (
    echo Please format your USB drive as FAT32
    set /a EXITCODE=1
  )
  echo.

exit /b %EXITCODE%


:make-bootable
  echo Press any key to make drive %~d0 bootable
  echo or close this window to abort...
  pause > nul
  cls
  echo syslinux64.exe -d syslinux -mafi %~d0
exit /b %ERRORLEVEL%


:success-message
  color 2D
  echo.
  echo ~~~~~~~~ Congratulations ~~~~~~~
  echo.
  echo The hidden file ldlinux.sys has been installed.
  echo Your %~d0 drive should now be bootable.
  echo //NOTE// If your USB drive fails to boot (maybe buggy BIOS),
  echo          try to use "syslinux64 -d syslinux -sfmar %~d0".
exit /b %ERRORLEVEL%


:fail-message
  color 4f
  echo.
  echo ----------------------------
  echo *** FATAL ERROR                                   ***
  echo *** %~d0 drive is not bootable for Clonezilla       ***
  echo *** %~nx0 should be run as Administrator ***
  echo *** or other major failure has occurred           ***
  echo ----------------------------
exit /b %ERRORLEVEL%
