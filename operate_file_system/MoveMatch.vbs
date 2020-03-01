Set objFolder = CreateObject("Scripting.FileSystemObject").GetFolder("C:\Users\Will\Desktop\u")
'For Each objTarget in objFolder.Files
For Each objTarget in objFolder.SubFolders
	Dim originalTargetName
	originalTargetName = objTarget.Name
	'MsgBox originalTargetName

	Dim regex
	Set regex = New RegExp
	'regex.Pattern = " \[W\d_\d\d\]"
	regex.Pattern = " \[W\d]"
	regex.Global = True

	Dim TargetNameRemoveMatch
	TargetNameRemoveMatch = regex.Replace(originalTargetName, "")
	'MsgBox TargetNameRemoveMatch

	Dim matches, match
	Set matches = regex.Execute(originalTargetName)
	For Each m in matches
		'MsgBox "|MATCH| " & m.Value & " |AT| " & CStr(m.FirstIndex +1)
		match = m.value

		Dim index: index = 10
		Dim modifiedTargetName

		modifiedTargetName = Left(TargetNameRemoveMatch, index - 1) + match + " " + Left(Mid(TargetNameRemoveMatch, index + 1), Len(TargetNameRemoveMatch) - index)
		'MsgBox Left(TargetNameRemoveMatch, index)
		'MsgBox modifiedTargetName
		objTarget.name = "$" & modifiedTargetName
		objTarget.name = modifiedTargetName

		'Exit For
	Next
Next


'MoveMatch	in file/folder name, move the part which matching regex to specified index