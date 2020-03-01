Set objFolder = CreateObject("Scripting.FileSystemObject").GetFolder(WScript.Arguments(0))
For Each objFile in objFolder.Files
'For Each objFile in objFolder.SubFolders
	originalFileName = objFile.Name
	processPart = Mid(originalFileName, WScript.Arguments(1))
	nameArr = Split(processPart, WScript.Arguments(2))
	Dim modifiedProcessPart
	modifiedProcessPart = ""
	For i=0 To Ubound(nameArr)
		If i = 0 Then
			nameArr(i) = UCase(Left(nameArr(i), 1)) & Mid(nameArr(i), 2)
		Else
			nameArr(i) = UCase(Left(nameArr(i), 1)) & Mid(nameArr(i), 2)
			modifiedProcessPart = modifiedProcessPart & " "
		End If
		modifiedProcessPart = modifiedProcessPart & nameArr(i)
	Next
	modifiedFileName = Mid(originalFileName, 1, WScript.Arguments(1)-1) & modifiedProcessPart
	objFile.name = "$" & modifiedFileName
	objFile.name = modifiedFileName
Next


'CamelOnlyFirstWordFromIndex.vbs "C:\Users\Will\Desktop\b" 14 " " 	From index 14, split as words by blank string, capital first char and lower other chars for every word