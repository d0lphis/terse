Set fileSO = CreateObject("Scripting.FileSystemObject")
Set obj = fileSO.OpenTextFile(WScript.Arguments(0),1)
Do While obj.AtEndOfStream <> True
	Dim originalLine
	originalLine = obj.ReadLine
	'MsgBox originalLine



	Dim regex
	Set regex = New RegExp



	regex.Pattern = WScript.Arguments(1)
	regex.Global = True

	Dim lineRemoveMatch
	lineRemoveMatch = regex.Replace(originalLine, "")
	'MsgBox "|" + lineRemoveMatch + "|"



	regex.Pattern = lineRemoveMatch

	Dim lineOfMatch
	lineOfMatch = regex.Replace(originalLine, "")
	'MsgBox "|" + lineOfMatch + "|"



	regex.Pattern = WScript.Arguments(3)
	Set folderSO = CreateObject("Scripting.FileSystemObject")
	Set objFolder = folderSO.GetFolder(WScript.Arguments(2))
	For Each objTarget in objFolder.Files
		Dim originalTargetName
		originalTargetName = objTarget.Name
		'MsgBox originalTargetName
		originalTargetNameSuffix = folderSO.GetExtensionName(objTarget.Path)
		'MsgBox originalTargetNameSuffix
		originalTargetNam = Replace(originalTargetName, "." + originalTargetNameSuffix, "")
		'MsgBox "|" + originalTargetNam + "|"

		Set matches = regex.Execute(originalTargetNam)
		For Each m in matches
			'MsgBox "|" + originalTargetNam + "|"
			'MsgBox "|" + lineOfMatch + "|"
			If Instr(originalTargetNam, lineOfMatch) <> 0 Then
				Dim modifiedTargetName
				modifiedTargetName = originalTargetNam + WScript.Arguments(4) + lineRemoveMatch + "." + originalTargetNameSuffix
				'MsgBox modifiedTargetName

				objTarget.name = "$" & modifiedTargetName
				objTarget.name = modifiedTargetName
			End If
		Next
	Next
LOOP

'C:\Users\Will\Desktop\autoscript\AdjustFileNameByList.vbs "C:\Users\Will\Desktop\fileNameList.txt" "G[A-Z0-9] Unit\d\d Week\d\d - Big Book - " "C:\Users\Will\Desktop\a" " - Big Book - $" ""
'	"C:\Users\Will\Desktop\fileNameList.txt"
'		G1 Unit01 Week01 - Big Book - This School Year Will Be The Best
'		G1 Unit01 Week02 - Big Book - Alicia's Happy Day
'		G1 Unit01 Week03 - Big Book - Cool Dog School Dog
'	"G[A-Z0-9] Unit\d\d Week\d\d "
'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Big Book - .pdf
'		G1 Unit01 Week02 - Big Book - .pdf
'		G1 Unit01 Week03 - Big Book - .pdf
'	" Big Book$"
'	""

'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Big Book - This School Year Will Be The Best.pdf
'		G1 Unit01 Week02 - Big Book - Alicia's Happy Day.pdf
'		G1 Unit01 Week03 - Big Book - Cool Dog School Dog.pdf






'C:\Users\Will\Desktop\autoscript\AdjustFileNameByList.vbs "C:\Users\Will\Desktop\fileNameList.txt" "G[A-Z0-9] Unit\d\d Week\d\d - Leveled Reader - \d" "C:\Users\Will\Desktop\a"  " - \d$" ""
'	"C:\Users\Will\Desktop\fileNameList.txt"
'		G1 Unit01 Week01 - Leveled Reader - 1 We Like to Share
'		G1 Unit01 Week02 - Leveled Reader - 1 A Trip to the City
'		G1 Unit01 Week01 - Leveled Reader - 2 A Fun Day
'		G1 Unit01 Week02 - Leveled Reader - 2 What Can We See
'		G1 Unit01 Week01 - Leveled Reader - 3 We Like to Share
'		G1 Unit01 Week02 - Leveled Reader - 3 A Trip to the City
'		G1 Unit01 Week01 - Leveled Reader - 4 Class Party
'		G1 Unit01 Week02 - Leveled Reader - 4 Harvest time
'	"G[A-Z0-9] Unit\d\d Week\d\d \d - Leveled Reader - \d"
'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Leveled Reader - 1.pdf
'		G1 Unit01 Week01 - Leveled Reader - 2.pdf
'		G1 Unit01 Week01 - Leveled Reader - 3.pdf
'		G1 Unit01 Week01 - Leveled Reader - 4.pdf
'		G1 Unit01 Week02 - Leveled Reader - 1.pdf
'		G1 Unit01 Week02 - Leveled Reader - 2.pdf
'		G1 Unit01 Week02 - Leveled Reader - 3.pdf
'		G1 Unit01 Week02 - Leveled Reader - 4.pdf
'	" - \d$"
'	""

'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Leveled Reader - 1 We Like To Share.pdf
'		G1 Unit01 Week01 - Leveled Reader - 2 A Fun Day.pdf
'		G1 Unit01 Week01 - Leveled Reader - 3 We Like To Share.pdf
'		G1 Unit01 Week01 - Leveled Reader - 4 Class Party.pdf
'		G1 Unit01 Week02 - Leveled Reader - 1 A Trip To The City.pdf
'		G1 Unit01 Week02 - Leveled Reader - 2 What Can We See.pdf
'		G1 Unit01 Week02 - Leveled Reader - 3 A Trip To The City.pdf
'		G1 Unit01 Week02 - Leveled Reader - 4 Harvest Time.pdf