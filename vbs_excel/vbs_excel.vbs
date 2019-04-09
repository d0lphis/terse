Function CreateExcelFile(sFilePath)
	Dim xlsApp,xlsWorkBook,xlsSheet

	'declare Excel Obj
	Set xlsApp=WScript.CreateObject("Excel.Application")

	'true: show Excel obj，false: not show Excel obj
	xlsApp.Visible=True

	'create Excel instance
	Set xlsWorkBook=xlsapp.Workbooks.Add

	'get the second worksheet in workbook
	'Set xlsSheet=xlsWorkBook.Worksheets("Sheet1")
	Set xlsSheet=xlsApp.Sheets.Item("Sheet1")
	'Set xlsSheet=xlsApp.Sheets.Item(1)
	'xlsApp.Sheets.Item(1).Select
	'xlsApp.Sheets.Item(1).activate

	'add text "Hello World" in cell
	xlsSheet.Cells(1,1).Value="Hello World!"
	'activesheet.cells(i,1).formula="='D:\[税金.xls]sheet1'!$A$" & i

	'save workbook
	xlsApp.ActiveWorkbook.SaveAs(sFilePath)
	'xlsWorkBook.SaveAs(sFilePath)
	'xlsWorkBook.Save

	'quit workbook
	xlsWorkBook.Close
	xlsApp.Quit

	'release memory
	Set xlsSheet=Nothing
	Set xlsWorkBook=Nothing
	Set xlsApp=Nothing
End Function

Function OpenExcelFile(sFilePath)
	Dim xlsApp,xlsWorkBook,xlsSheet

	Set xlsApp=WScript.CreateObject("Excel.Application")
	xlsApp.Visible=True

	'open Excel file
	Set xlsWorkBook=xlsApp.Workbooks.Open(sFilePath)

	'select worksheet sheet1
	Set xlsSheet=xlsApp.Sheets.Item("Sheet1")

	'save workbook
	xlsWorkBook.Save

	'xlsApp.Quit
	Set xlsApp=Nothing
	Set xlsWorkBook=Nothing
	Set xlsApp=Nothing
End Function

Function DeleteSheet(n)
	Dim xlsApp,xlsWorkBook,xlsSheet

	Set xlsApp=WScript.CreateObject("Excel.Application")
	xlsApp.Visible=True

	Set xlsWorkBook=xlsapp.Workbooks.Add()
	Set xlsSheet=xlsWorkBook.Sheets.Add()
	xlsWorkBook.Worksheets("Sheet"&n).Delete

	xlsApp.Quit
	Set xlsSheet=Nothing
	Set xlsWorkBook=Nothing
	Set xlsApp=Nothing
End Function

Function AddSheets(sFilePath)
	Dim xlsApp,xlsWorkBook,xlsSheet

	Set xlsApp=WScript.CreateObject("Excel.Application")
	xlsApp.Visible=True

	Set xlsWorkBook=xlsapp.Workbooks.Add()
	Set xlsSheet=xlsApp.Sheets.Item("Sheet1")
	xlsSheet.Cells(1,1).Value="Hello World!"

	Set xlsSheet=xlsWorkBook.Sheets.Add()
	xlsSheet.name="Practice"
	xlsSheet.activate
	xlsSheet.range("A1:B5").Value="Hello World"

	xlsApp.ActiveWorkbook.SaveAs(sFilePath)
	xlsApp.Quit
	Set xlsSheet=Nothing
	Set xlsWorkBook=Nothing
	Set xlsApp=Nothing
End Function

Function CreateWriteSaveAsExcelFile(sSheetName,i,j,sFilePath)
	Dim xlsApp,xlsWorkBook,xlsSheet

	Set xlsApp=WScript.CreateObject("Excel.Application")
	xlsApp.Visible=True

	Set xlsWorkBook=xlsapp.Workbooks.Add()
	Set xlsSheet=xlsApp.Sheets.Item(sSheetName)
	xlsSheet.Cells(i,j).Value="Hello World!"

	xlsApp.ActiveWorkbook.SaveAs(sFilePath)
	xlsApp.Quit
	Set xlsSheet=Nothing
	Set xlsWorkBook=Nothing
	Set xlsApp=Nothing
End Function

'Funciton TouchExcelNoOpen()
	'Application.ScreenUpdating = False

	'activesheet.range("a1").currentregion.copy

	'activesheet.range("a1").PasteSpecial xlPasteValues

	'Application.CutCopyMode = False

	'Application.ScreenUpdating=true
'End Function



Function CopmareWrite(sFilePath)
	'Option Explicit
	'On Error Resume Next

	'declare vars
	Dim a(),b()
	Dim iRowCount,i,rowCount
	Dim oLoop,xLoop,jLoop



	Dim xlsApp1,xlsWorkBook1,xlsSheet1
	Set xlsApp1=CreateObject("Excel.Application")
	xlsApp1.Visible=True

	Set xlsWorkBook1=xlsApp1.Workbooks.Open(sFilePath)
	Set xlsSheet1=xlsApp1.Sheets.Item("3rdLineAnalysis")
	'WScript.Echo xlsSheet1.range("C2").Value



	Dim xlsApp2,xlsWorkBook2,xlsSheet2
	Set xlsApp2=WScript.CreateObject("Excel.Application")
	xlsApp2.Visible=True

	Set xlsWorkBook2=xlsapp2.Workbooks.Add()
	Set xlsSheet2=xlsApp2.Sheets.Item("Sheet1")
	xlsSheet2.activate



	'format destination sheet
	xlsApp2.ActiveWindow.DisplayGridlines = false
	'Set objRange=xlsSheet2.UsedRange
	'objRange.EntireColumn.Autofit
	xlsSheet2.Columns("A").ColumnWidth=2.43
	xlsSheet2.Columns("B").ColumnWidth=6.71
	xlsSheet2.Columns("C").ColumnWidth=2.43
	xlsSheet2.Columns("D:G").ColumnWidth=1.57
	xlsSheet2.Columns("I").ColumnWidth=24.71
	xlsSheet2.Columns("J").ColumnWidth=46.86
	xlsSheet2.Columns("K").ColumnWidth=80
	xlsSheet2.Columns("L").ColumnWidth=70
	'xlsSheet2.range("C2").Value="Hello World!"
	


	'copy and format
	xlsSheet1.Range("B2:N6").Copy
	xlsSheet2.Range("B2:N6").PasteSpecial 8



	'get valid row and column number
	'WScript.Echo xlsSheet1.UsedRange.Rows.Count
	'WScript.Echo xlsSheet1.UsedRange.Columns.Count



	For oLoop=8 To xlsSheet1.UsedRange.Rows.Count
		'WScript.Echo "oLoop "&oLoop
		sFeatureFullName=xlsSheet1.range("I"&oLoop).Value
		nInx=Instr(sFeatureFullName,":")
		If nInx<>0 Then
			sFeatureName=Mid(sFeatureFullName, 1, nInx-1)




			bTypeAdded="false"
			For xLoop=7 To xlsSheet2.UsedRange.Rows.Count
				If xlsSheet2.Range("B"&xLoop).Value=sFeatureName Then
					bTypeAdded="true"
				End If
			Next

			xlsSheet2.activate
			existingRowCount=xlsSheet2.UsedRange.Rows.Count+1
			If bTypeAdded="false" Then
				xlsSheet1.Range("B7:N7").Copy
				xlsSheet2.Range("B"&existingRowCount+1).PasteSpecial 8
				'xlsSheet2.range("B"&existingRowCount+1).Font.Size=20
				xlsSheet2.range("B"&existingRowCount+1).Value=sFeatureName
			End If
			



			'WScript.Echo sFeatureName
			'bTypeCaseMaxStartLine=7
			For jLoop=7 To xlsSheet2.UsedRange.Rows.Count+1
				If Instr(xlsSheet2.Range("B"&jLoop).Value,sFeatureName)<>0 Then
					bTypeCaseMaxStartLine=jLoop
				End If
			Next
			'WScript.Echo "START "&bTypeCaseMaxStartLine
			bTypeCaseMaxEndLine=bTypeCaseMaxStartLine
			For jLoop=bTypeCaseMaxStartLine To xlsSheet2.UsedRange.Rows.Count+1
				'WScript.Echo jLoop
				'WScript.Echo xlsSheet2.UsedRange.Rows.Count
				'WScript.Echo xlsSheet2.Range("I"&jLoop).Value
				'WScript.Echo sFeatureName
				If Instr(xlsSheet2.Range("I"&jLoop).Value,sFeatureName)<>0 Then
					bTypeCaseMaxEndLine=jLoop
				End If
			Next
			'WScript.Echo "END "&bTypeCaseMaxEndLine
			xlsSheet1.Range("A"&oLoop&":N"&oLoop).Copy
			If xlsSheet2.Range("B"&bTypeCaseMaxEndLine+1).value<>"" Then
				xlsSheet2.Rows(bTypeCaseMaxEndLine+1).Insert
				'WScript.Echo "Bingo"
			End If
			xlsSheet2.Range("A"&bTypeCaseMaxEndLine+1).pasteSpecial 8
			
		End If
	Next
End Function



'Application.Version					show excel version
'Application.UserName					show current user name
'Application.StatusBar = "loading..."			show text loading... in status var
'Application.StatusBar = False				disable info in status bar
'Application.Wait Now() + TimeValue("00:00:01")		pause 1 sec



'CreateExcelFile("C:\Users\Administrator\Desktop\test.xlsx")
'OpenExcelFile("C:\Users\Administrator\Desktop\test.xlsx")
'AddSheets("C:\Users\Administrator\Desktop\test.xlsx")
'DeleteSheet(1)
'CreateWriteSaveAsExcelFile "Sheet1", 2, 2, "C:\Users\Administrator\Desktop\test.xlsx"
'CopmareWrite("C:\Users\Administrator\Desktop\test.xlsx")
CopmareWrite("C:\Users\Administrator\Desktop\CASE_LIBRARY_10.1.xlsx")
'TouchExcelNoOpen()
