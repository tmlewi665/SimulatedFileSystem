# SimulatedFileSystem
The program simulates a basic file system with directories and files.  Users can perform operations like creating directories, creating files, listing files, changing directories, and more.

This code has 5 main commmands:
'ls': List files in the current directory.
'mkdir <name>': Creates a new directory.
'touch <name>.<type>': Create a new file with the specified name and time, or change modify data on file.
'cd /<name>': Change to specified directory, leave name blank to go back a directory.
'exit': Exits the program.

Example Usage:
ls
mkdir users
touch hello.txt
cd /users
cd /
exit
