Set fileSO = CreateObject("Scripting.FileSystemObject")
Set objFileFolder = fileSO.GetFolder(WScript.Arguments(0))
For Each objFile in objFileFolder.Files
	Dim fileName
	fileName = objFile.Name
	'MsgBox fileName
	fileNameSuffix = fileSO.GetExtensionName(objFile.Path)
	'MsgBox fileNameSuffix
	fileNam = Replace(fileName, "." + fileNameSuffix, "")
	'MsgBox fileNam

	If fileNameSuffix = "pdf" Then
		'MsgBox fileName
		
		serial = Left(fileName, 2)

		dim unit
		dim week
		If serial mod 5 <> 0 Then
			week = Int(serial mod 5)
			unit = Int(serial / 5) + 1
		Else
			week = 5
			unit = Int(serial / 5)
		End If

		dim placeHolderU: placeHolderU = ""
		If unit < 10 Then
			placeHolderU = "0"
		End If
		dim placeHolderW: placeHolderW = ""
		If week < 10 Then
			placeHolderW = "0"
		End If

		modifiedName = WScript.Arguments(2) + " Unit" + placeHolderU + Cstr(unit) + " Week" + placeHolderU + Cstr(week) + " - Leveled Reader - " + WScript.Arguments(3) + " " + Right(fileNam, Len(fileNam) - 3)
		'MsgBox "|" + modifiedName + "|"
		fileSO.CreateFolder(WScript.Arguments(1) + "\" + modifiedName + " (MP3)")
		fileSO.CopyFile WScript.Arguments(0) + "\"  + fileName, WScript.Arguments(1) + "\" + modifiedName + "." + fileNameSuffix
		fileSO.CopyFile WScript.Arguments(0) + "\"  + fileNam + "*.mp3", WScript.Arguments(1) + "\" + modifiedName + " (MP3)" + "\"
	End If
Next



'C:\Users\Will\Desktop\autoscript\MoveAudioToFolder.vbs "C:\Users\Will\Desktop\a" "C:\Users\Will\Desktop\b" "G2" "2"
'	"C:\Users\Will\Desktop\a"
'		09 Little Bat 00.mp3
'		09 Little Bat 02-03.mp3
'		09 Little Bat 04-05.mp3
'		09 Little Bat 06-07.mp3
'		09 Little Bat 08-09.mp3
'		09 Little Bat 10-11.mp3
'		09 Little Bat 12-13.mp3
'		09 Little Bat 14-15.mp3
'		09 Little Bat.pdf
'	"C:\Users\Will\Desktop\b"
'		G1 Unit01 Week01 - Leveled Reader - 1 (MP3)
'		G1 Unit01 Week01 - Leveled Reader - 2 (MP3)
'		G1 Unit01 Week01 - Leveled Reader - 3 (MP3)
'		G1 Unit01 Week01 - Leveled Reader - 4 (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 1 (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 2 (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 3 (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 4 (MP3)
'	" - \d \("
'	""

'	"C:\Users\Will\Desktop\b"
'		G1 Unit01 Week01 - Leveled Reader - 1 We Like To Share (MP3)
'		G1 Unit01 Week01 - Leveled Reader - 2 A Fun Day (MP3)
'		G1 Unit01 Week01 - Leveled Reader - 3 We Like To Share (MP3)
'		G1 Unit01 Week01 - Leveled Reader - 4 Class Party (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 1 A Trip To The City (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 2 What Can We See (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 3 A Trip To The City (MP3)
'		G1 Unit01 Week02 - Leveled Reader - 4 Harvest Time (MP3)