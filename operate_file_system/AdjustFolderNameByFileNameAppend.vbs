Set fileSO = CreateObject("Scripting.FileSystemObject")
Set objFileFolder = fileSO.GetFolder(WScript.Arguments(0))
For Each objFile in objFileFolder.Files
	Dim fileName
	fileName = objFile.Name
	'MsgBox fileName
	fileNameSuffix = fileSO.GetExtensionName(objFile.Path)
	fileNam = Replace(fileName, "." + fileNameSuffix, "")



	Dim regex
	Set regex = New RegExp



	regex.Pattern = WScript.Arguments(1)
	regex.Global = True

	Dim targetNameRemoveMatch
	fileNamRemoveMatch = regex.Replace(fileNam, "")



	regex.Pattern = fileNamRemoveMatch

	Dim targetNameOfMatch
	fileNamOfMatch = regex.Replace(fileNam, "")
	'MsgBox "|" + fileNamOfMatch + "|"



	regex.Pattern = WScript.Arguments(1)
	fileNamRemoveMatch = regex.Replace(fileNamRemoveMatch, "")
	'MsgBox "|" + fileNamRemoveMatch + "|"



	regex.Pattern = WScript.Arguments(3)
	Set folderSO = CreateObject("Scripting.FileSystemObject")
	Set objFolderFolder = folderSO.GetFolder(WScript.Arguments(2))
	For Each objFolder in objFolderFolder.SubFolders
		Dim originalFolderName
		originalFolderName = objFolder.Name
		'MsgBox originalFolderName

		Set matches = regex.Execute(originalFolderName)
		For Each m in matches

			If Instr(originalFolderName, fileNamOfMatch) <> 0 Then
				Dim index: index = Instr(originalFolderName, "(")
				Dim modifiedFolderName

				modifiedFolderName = Left(originalFolderName, index - 1) + WScript.Arguments(4) + fileNamRemoveMatch + " " + Left(Mid(originalFolderName, index), Len(originalFolderName) - index + 1)
				'MsgBox modifiedFolderName

				objFolder.name = "$" & modifiedFolderName
				objFolder.name = modifiedFolderName
			End If
		Next
	Next
Next

'C:\Users\Will\Desktop\autoscript\AdjustFolderNameByFileNameAppend.vbs "C:\Users\Will\Desktop\a" "G[A-Z0-9] Unit\d\d Week\d\d - Big Book - \d " "C:\Users\Will\Desktop\b" " Big Book \(" ""
'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Big Book - This School Year Will Be The Best.pdf
'		G1 Unit01 Week02 - Big Book - Alicia's Happy Day.pdf
'		G1 Unit01 Week03 - Big Book - Cool Dog School Dog.pdf
'	"G[A-Z0-9] Unit\d\d Week\d\d - Big Book - \d "
'	"C:\Users\Will\Desktop\b"
'		G1 Unit01 Week01 - Big Book (MP3)
'		G1 Unit01 Week02 - Big Book (MP3)
'		G1 Unit01 Week03 - Big Book (MP3)
'	" Big Book \("
'	""
'

'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Big Book - This School Year Will Be The Best (MP3)
'		G1 Unit01 Week02 - Big Book - Alicia's Happy Day (MP3)
'		G1 Unit01 Week03 - Big Book - Cool Dog School Dog (MP3)






'C:\Users\Will\Desktop\autoscript\AdjustFolderNameByFileNameAppend.vbs "C:\Users\Will\Desktop\a" "G[A-Z0-9] Unit\d\d Week\d\d - Leveled Reader - \d " "C:\Users\Will\Desktop\b" " - \d \(" ""
'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Leveled Reader - 1 We Like To Share.pdf
'		G1 Unit01 Week01 - Leveled Reader - 2 A Fun Day.pdf
'		G1 Unit01 Week01 - Leveled Reader - 3 We Like To Share.pdf
'		G1 Unit01 Week01 - Leveled Reader - 4 Class Party.pdf
'		G1 Unit01 Week02 - Leveled Reader - 1 A Trip To The City.pdf
'		G1 Unit01 Week02 - Leveled Reader - 2 What Can We See.pdf
'		G1 Unit01 Week02 - Leveled Reader - 3 A Trip To The City.pdf
'		G1 Unit01 Week02 - Leveled Reader - 4 Harvest Time.pdf
'	"G[A-Z0-9] Unit\d\d Week\d\d - Leveled Reader - \d "
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