# DriveUsageAnalyser
Walks through a Folder and it's contents and displays the size of each folder so you can determine where "the dog is buried"

## Usage

Start analyser.py. When you are asked for a folder, enter the folder you want to use as a base directory. For example, you can enter `C:\` 

The script will start to scan the Folder ans it's subfolders, while that it will display the Filesize already scanned. 
 Once ready, you will se a GUI consisting of lines like this:
 
 `|[2] - 1.9 GB           2.871%          C:\\$RECYCLE.BIN\           |`
 You'll see:
- The first is the number you can type in to go to this folder
- The size of the folder
- How many % of all file-size in the subfolder this folder contains
- The name of the folder
