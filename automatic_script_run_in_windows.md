# This file guides through the steps, to create a scheduled task to run the script daily.

### This works for Windows 8, 8.1 and 10.

## Steps

1. Open 'Task Scheduler' in windows.
2. Click on 'Create Basic Task' tab, on the right.
3. Give a name to the task, such as 'Bing Wallpaper' and a optional description, then click next.
4. Select 'daily' from the option to run the task.
5. Select the time at which you want to run the task each day. Click next.
6. Select 'start a program' from the action menu. Click next.
7. In the path to Program/script, enter the path to your 'python.exe' file, like "C:\Python27\python.exe" and
   then add the path to 'main.py' file in the 'Add arguments' option, like "C:\bing_wallpaper_python_script\main.py". Click next.
   ### Put the path in " ", if there is any name seperated by space, like C:\bing wallpaper\main.py (space between bing and wallpaper)
   
8. Check the properties of the task. Click Finish.
