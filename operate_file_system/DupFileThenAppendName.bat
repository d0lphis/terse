@echo off
for /f "delims=" %%i in (C:\Users\Will\Desktop\name.txt) do (
	set "a=%%i"
	echo %%i
	rem xcopy "X:\Project_Movie\HERO\FromClient\source\Hero_2to3_0705\ca003\%a%" "X:\Project_Movie\HERO\Shots\%a%\Source\%a%"
)