# start-an-app
Just a tool to start some apps.


Usage: `python start.py --type <system (Default)/startfile/force/> --path "C:/Some/Example/Path" (Required)` 


system: use `os.system()` to start an app
startfile: use `os.startfile()` to start an app (in theory this can start any **file** even urls)
force: this checks the first two byte of the file is `MZ` or not (actually this is just `system` method with a stricter inspection)
