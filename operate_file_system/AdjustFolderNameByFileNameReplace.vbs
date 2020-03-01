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



	regex.Pattern = WScript.Arguments(3) + fileNamRemoveMatch + "$"
	Set folderSO = CreateObject("Scripting.FileSystemObject")
	Set objFolderFolder = folderSO.GetFolder(WScript.Arguments(2))
	For Each objFolder in objFolderFolder.SubFolders
		Dim originalFolderName
		originalFolderName = objFolder.Name
		'MsgBox "|" + originalFolderName + "|"

		Set matches = regex.Execute(originalFolderName)
		For Each m in matches
			'MsgBox "|" + originalFolderName + "|"
			'MsgBox "|" + fileNamRemoveMatch + "|"
			'MsgBox Instr(originalFolderName, fileNamRemoveMatch)
			'If Instr(originalFolderName, fileNamRemoveMatch) <> 0 then
			If Len(originalFolderName) - Len(fileNamRemoveMatch) = 5 then
				Dim modifiedFolderName

				modifiedFolderName = fileNam + " (MP3)"
				'MsgBox modifiedFolderName

				objFolder.name = "$" & modifiedFolderName
				'MsgBox "1"
				objFolder.name = modifiedFolderName
				'MsgBox "2"
			End If
		Next
	Next
Next

'C:\Users\Will\Desktop\autoscript\AdjustFolderNameByFileNameReplace.vbs "C:\Users\Will\Desktop\a" "G[A-Z0-9] Unit\d\d Week\d\d - Leveled Readers - " "C:\Users\Will\Desktop\b" "^G[A-Z0-9] - "
'	"C:\Users\Will\Desktop\a"
'		G1 Unit01 Week01 - Leveled Readers - Can You.pdf
'		G1 Unit01 Week01 - Leveled Readers - Cat Can Jump.pdf
'		G1 Unit01 Week01 - Leveled Readers - Look at me Chameleon.pdf
'	"G[A-Z0-9] Unit\d\d Week\d\d - Leveled Readers - "
'	"C:\Users\Will\Desktop\b"
'		G1 - Can You
'		G1 - Cat Can Jump
'		G1 - Look at me Chameleon
'	"^G[A-Z0-9] - "

'	"C:\Users\Will\Desktop\b"
'		G1 Unit01 Week01 - Leveled Readers - Can You
'		G1 Unit01 Week01 - Leveled Readers - Cat Can Jump
'		G1 Unit01 Week01 - Leveled Readers - Look at me Chameleon