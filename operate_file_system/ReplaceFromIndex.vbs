Set objFolder = CreateObject("Scripting.FileSystemObject").GetFolder("C:\Users\will\Desktop\Marc.Antoine.-.[The.Very.Best.of.Marc.Antoine].×¨¼­.(AAC)")
For Each objFile in objFolder.Files
	originalFileName = objFile.Name
	modifiedFileName = Mid(originalFileName, 1, WScript.Arguments(0)) & Replace(Mid(originalFileName, WScript.Arguments(0)+1), WScript.Arguments(1), WScript.Arguments(2))
	objFile.name = "$" & modifiedFileName
	objFile.name = modifiedFileName
Next


'ReplaceFromIndex.vbs 1 _ " " 	start from index 1, replace all - as blank char