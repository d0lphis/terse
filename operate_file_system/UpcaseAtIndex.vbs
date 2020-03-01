Set objFolder = CreateObject("Scripting.FileSystemObject").GetFolder("C:\Users\will\Desktop\solo)(M¨¦av)(ACelticJourney~")
For Each objFile in objFolder.Files
	originalFileName = objFile.Name
	ucaseChar = UCase(Mid(originalFileName, WScript.Arguments(0), 1))
	modifiedFileName = Mid(originalFileName, 1, WScript.Arguments(0)-1) & ucaseChar & Mid(originalFileName, WScript.Arguments(0)+1)
	objFile.name = "$" & modifiedFileName
	objFile.name = modifiedFileName
Next


'UpcaseAtIndex.vbs 14 	capital char on index 14