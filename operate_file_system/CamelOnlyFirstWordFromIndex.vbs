Set objFolder = CreateObject("Scripting.FileSystemObject").GetFolder("C:\Users\will\Desktop\solo)(M¨¦av)(ACelticJourney~")
For Each objFile in objFolder.Files
	originalFileName = objFile.Name
	processPart = Mid(originalFileName, WScript.Arguments(0))
	nameArr = Split(processPart, WScript.Arguments(1))
	Dim modifiedProcessPart
	modifiedProcessPart = ""
	For i=0 To Ubound(nameArr)
		If i = 0 Then
			nameArr(i) = UCase(Left(nameArr(i), 1)) & Mid(nameArr(i), 2)
		Else
			nameArr(i) = LCase(Left(nameArr(i), 1)) & Mid(nameArr(i), 2)
			modifiedProcessPart = modifiedProcessPart & " "
		End If
		modifiedProcessPart = modifiedProcessPart & nameArr(i)
	Next
	modifiedFileName = Mid(originalFileName, 1, WScript.Arguments(0)-1) & modifiedProcessPart
	objFile.name = "$" & modifiedFileName
	objFile.name = modifiedFileName
Next


'CamelOnlyFirstWordFromIndex.vbs 14 " " 	From index 14, split as words by blank string, capital first char and lower other chars for first word, lover chars for other words