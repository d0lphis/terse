set cmd to ""
tell application "Finder"
    set theWindow to window 1
    set thePath to (POSIX path of (target of theWindow as alias))
    set cmd to "cd " & "\"" & thePath & "\""
end tell

tell application "Terminal"
    activate
    tell application "System Events" to keystroke "t" using command down

    delay 0.5
    do script cmd in window 1
end tell

保存成finder2shell.scpt，另存为Application 类型，这样就会得到finder2shell.app。
按住command键，把它拖动到 Finder 的工具栏上即可。
