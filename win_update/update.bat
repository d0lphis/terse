'https://kb.cscc.edu/article/how-to-install-a-msu-update-on-windows-7-from-the-command-line-63.html

Set Folder="C:\updates"
for %%f in (%Folder%\*.msu) do (
  wusa.exe %%f /quiet /norestart
)