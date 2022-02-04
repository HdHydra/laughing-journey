@echo off
:loop
echo.
set /A x=300
echo Waiting For %x% seconds... 
  TIMEOUT /T %x% /NOBREAK
  echo.
  bomb_1.wav
  echo time up
goto loop
