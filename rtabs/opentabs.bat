@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION



REM prototype:
REM "C:\Program Files\Mozilla Firefox\firefox.exe" -new-window -url "http://www.baidu.com" -url "http://www.163.com"

REM #usage:
REM opentabs.bat firefox C:\Users\Will\Desktop\a.txt ______routine_affair_a
REM opentabs.bat firefox C:\Users\Will\Desktop\a.txt ______routine_affair_a 6



SET browserType=%1
REM ECHO %browserType%
SET urlListFile=%2
SET startKey=%3
SET endKey=______
SET urlCount=%4

SET /A STRLENGTH=0
CALL:StrLen %startKey%
REM ECHO startKey %startKey% length %STRLENGTH%
SET /A startKeyEndIdx=STRLENGTH
REM ECHO startKey %startKey% end position %startKeyEndIdx%

CALL:StrLen %endKey%
REM ECHO endKey %endKey% length %STRLENGTH%
SET /A endKeyEndIdx=STRLENGTH
REM ECHO endKey %endKey% end position %endKeyEndIdx%



SET inRecordingMode=False
SET /A i=1
SET urls=
for /f %%l in (%urlListFile%) do (
    SET headOrUrl=%%l
        REM ECHO !headOrUrl:~0,%startKeyEndIdx%!
        REM ECHO %startKey%
        REM ECHO !headOrUrl:~0,%endKeyEndIdx%!
        REM ECHO %endKey%
    IF !inRecordingMode!==False (
        IF "!headOrUrl:~0,%startKeyEndIdx%!" EQU "%startKey%" (
            REM ECHO !headOrUrl!
            SET inRecordingMode=True
        )
    ) else IF "!headOrUrl:~0,%endKeyEndIdx%!" EQU "%endKey%" (
        SET inRecordingMode=False
        GOTO BreakRecordUrl
    ) else (
        REM ECHO !headOrUrl!
        REM ECHO !i! GTR !urlCount!
        IF NOT "!urlCount!"=="" (
            IF !i! GTR !urlCount! (
                GOTO BreakRecordUrl
            )
        )
        SET urls=!urls! -url "!headOrUrl!"
        SET /A i+=1
    )
)
:BreakRecordUrl
REM ECHO %urls%
REM EXIT /b



SET array[0].name=firefox
SET array[0].value=C:\Program Files\Mozilla Firefox\firefox.exe
SET array[1].name=firefoxd
SET array[1].value=C:\Program Files\Mozilla Firefox Developer\firefox.exe
SET array[2].name=chrome
SET array[2].value=C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
SET array[3].name=chromium
SET array[3].value=C:\Program Files (x86)\Google\Chromium\Application\chromium.exe
SET array[4].name=opera
SET array[4].value=C:\Users\Will\AppData\Local\Programs\Opera\launcher.exe
SET array[5].name=edge
SET array[5].value=C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
SET array[6].name=vivaldi
SET array[6].value=C:\Program Files (x86)\Vivaldi\Vivaldi.exe

SET ARRAYELEMENTVALUE=
CALL:GetEle %browserType%
ECHO %ARRAYELEMENTVALUE%

ECHO START "" "%ARRAYELEMENTVALUE%" -new-window %urls%
START "" "%ARRAYELEMENTVALUE%" -new-window %urls%






:StrLen strVar
REM compute string length of strVar
REM store length to STRLENGTH, fetch by defining global var before
    SET "strToHandle=%1!%%^^()^!"
    (ECHO "%strToHandle%" & echo.) | findstr /O . | more +1 | (SET /P result= & CALL EXIT /B %%result%%)
    SET /A STRLENGTH=%ERRORLEVEL%-5
    EXIT /b



:GetEle key
REM get element of Array by Index
REM store element to TARGETELE, fetch by defining global var before
REM TODO: array need to be passed in as arg
    SET idx=0
    SET key_located=False
    :LoopStart
        FOR /F "usebackq delims==. tokens=1-3" %%I IN (`SET array[%idx%]`) DO (
            REM ECHO !idx! %%J %%K %1 !key_located!
            REM IF !idx! EQU %1 (
            REM     SET ARRAYELEMENT.%%J=%%K.exe
            REM ) else IF !idx! GTR %1 (
            REM     GOTO BreakGetEle
            REM )
            IF !key_located!==True (
                SET ARRAYELEMENTVALUE=%%K.exe
                SET key_located=False
                GOTO BreakGetEle
            )
            IF "%%J" EQU "name" (
                IF "%%K" EQU "%1" (
                    SET key_located=True
                )
            )
        )
        SET /A idx+=1
    GOTO LoopStart
    :BreakGetEle
    EXIT /b