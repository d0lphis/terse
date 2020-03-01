'notice: name.txt needs to be encoded as ANSI


' Function Encode(filePath)
' 	Set stm = CreateObject("Adodb.Stream")
' 	stm.Type = 2
' 	stm.mode = 3
'  	stm.charset = "utf-8"
'  	stm.Open
'  	stm.LoadFromFile filePath
'  	Encode = stm.readtext
'  	stm.close
' End Function

' Msgbox Encode(WScript.Arguments(0))


Set fileSO = CreateObject("Scripting.FileSystemObject")
Set obj = fileSO.OpenTextFile(WScript.Arguments(0))
Do While obj.AtEndOfStream <> True
	Dim originalLine
	originalLine = obj.ReadLine
	'MsgBox originalLine
	objNameSuffix = fileSO.GetExtensionName(WScript.Arguments(1))
	MsgBox objNameSuffix

	'fileSO.CopyFile WScript.Arguments(1), WScript.Arguments(2) + originalLine + "." + objNameSuffix, False
LOOP

'C:\Users\Will\Desktop\autoscript\DupFileThenAppendName.vbs "C:\Users\Will\Desktop\name.txt" "C:\Users\Will\Desktop\content.docx" "C:\Users\Will\Desktop\b\"
'	"C:\Users\Will\Desktop\name.txt"
'		Ella
'		Austin
'		Aaron
'	"C:\Users\Will\Desktop\content.docx"

'	"C:\Users\Will\Desktop\b\"
'		Ella.docx
'		Austin.docx
'		Aaron.docx