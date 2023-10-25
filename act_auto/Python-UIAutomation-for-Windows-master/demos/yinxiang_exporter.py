#!python3
# -*- coding: utf-8 -*-
# works on windows XP, 7, 8, 8.1 and 10
import os
import sys
import time
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto

auto.uiautomation.DEBUG_EXIST_DISAPPEAR = True  # set it to False and try again, default is False
auto.uiautomation.DEBUG_SEARCH_TIME = True  # set it to False and try again, default is False
auto.uiautomation.TIME_OUT_SECOND = 10  # global time out



def exportAllYinXiangNotebooks():
    windowYinXiang = auto.WindowControl(searchDepth=1, RegexName = '.* - 印象笔记', AutomationId = 'QFrameWindow')
    windowYinXiang.SetActive()

    treeCtrlNotebooks = auto.TreeControl(searchFromControl = windowYinXiang, Name = 'NotebooksTreeCtrl')
    auto.Logger.WriteLine(treeCtrlNotebooks.AutomationId)

    for treeItem, treeDepth in auto.WalkControl(treeCtrlNotebooks, includeTop = True):
        notebookName = treeItem.Name
        # auto.Logger.WriteLine(notebookName)
        if isinstance(treeItem, auto.TreeItemControl):  # or treeItem.ControlType == auto.ControlType.TreeItemControl
            if notebookName not in ["Conflicting Changes", "WECHAT", "来自「印象识堂」", "来自「印象图记」", "来自小程序「印象笔记」"]:
                auto.Logger.WriteLine(' ' * (treeDepth - 1) * 4 + treeItem.Name, auto.ConsoleColor.Green)

                # right click a notebook
                treeItem.RightClick(waitTime=0)

                # find context menu window
                contxtMenu = auto.WindowControl(searchDepth= 1, Name = 'Evernote', AutomationId = 'QCustomRoundMenu')
                # click menu "Export Notes..."
                for menuItem in contxtMenu.GetChildren():
                    if menuItem.Name == 'Export Notes...':
                        menuItem.Click(40)
                        break

                # find export types Wizard (don't find Window, it's not visible so cannot be found) 
                dialogExportTypes = auto.WindowControl(searchDepth= 2, AutomationId = 'QFrameWindow.ExportWizardDlg')
                # click type "Export as multiple Web Pages (.html)"
                listCtrlExportTypes = auto.ListControl(searchFromControl = dialogExportTypes, ClassName = 'QListView')
                for listItem, listDepth in auto.WalkControl(listCtrlExportTypes, includeTop = True):
                    auto.Logger.WriteLine(' ' * (listDepth - 1) * 4 + listItem.Name, auto.ConsoleColor.Yellow)
                    if listItem.Name == 'Export as multiple Web Pages (.html)':
                        listItem.Click(40)
                        break
                # click button "Export"
                dialogExportTypes.ButtonControl(Name='Export').Click(40)
                
                # find item Desktop in prompted browser
                treeItemDesktop = auto.TreeItemControl(searchFromControl = dialogExportTypes, Name = 'Desktop')
                # click folder "yinxiang" in prompted browser
                for folderItem, folderDepth in auto.WalkControl(treeItemDesktop, includeTop = True):
                    # auto.Logger.WriteLine(' ' * (folderDepth - 1) * 4 + folderItem.Name, auto.ConsoleColor.Blue)
                    if folderItem.Name == 'yinxiang':
                        folderItem.GetScrollItemPattern().ScrollIntoView()      # else it will prompt error "Cannot move cursor"
                        folderItem.Click(40)

                        # click button "Make New Folder"
                        dialogExportTypes.ButtonControl(Name='Make New Folder').Click(40)
                        edit = dialogExportTypes.EditControl(searchDepth=4, ClassName='Edit')# search 2 times
                        edit.SendKeys(notebookName)
                        edit.SendKeys('{Enter}')

                        # click button "OK"
                        dialogExportTypes.ButtonControl(Name='OK').Click(40)

                        # click button "Close"
                        dialogMsgBox = auto.WindowControl(searchDepth= 2, AutomationId =  'QFrameWindow.QMsgBox')
                        dialogMsgBox.ButtonControl(Name='Close').Click(40)

                        break

                # focus on next notebook, else it will prompt error "Cannot move cursor
                # treeItem.GetSelectionItemPattern().Select(waitTime=0.05)      # cannot select notebook due to control properties missing, use click instead
                treeItem.Click(40)
                edit.SendKeys('{Down}')

                # break
        


if __name__ == '__main__':
    exportAllYinXiangNotebooks()

    # auto.Logger.Write('\nPress any key to exit', auto.ConsoleColor.Cyan)
    # import msvcrt
    # while not msvcrt.kbhit():
    #     time.sleep(0.05)
