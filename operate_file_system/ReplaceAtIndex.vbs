Set objFolder = CreateObject("Scripting.FileSystemObject").GetFolder("C:\Users\will\Desktop\a")
For Each objObject in objFolder.Files
'For Each objFolder in objFolder.SubFolders
	originalObjName = objObject.Name
	modifiedObjName = Mid(originalObjName, 1, WScript.Arguments(0)-1) & WScript.Arguments(1) & Mid(originalObjName, WScript.Arguments(0)+1)
	objObject.name = "$" & modifiedObjName
	objObject.name = modifiedObjName
Next


'ReplaceAtIndex.vbs	replace char on index 1 as S