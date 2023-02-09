# 0x00 Shell, basics
* 0-current_working_directory: Prints the absolute path name of the current working directory.
* 1-listit: Display the contents list of your current directory.
* 2-bring_me_home: Change the working directory to the user’s home directory.
* 3-listfiles: Display current directory contents in a long format.
* 4-listmorefiles: Display current directory contents, including hidden files (starting with .) in the long format.
* 5-listfilesdigitonly: Display current directory contents in long format with user and group IDs displayed numerically and hidden files (starting with .).
* 6-firstdirectory: Create a directory named my_first_directory in the /tmp/ directory.
* 7-movethatfile: Move the file betty from /tmp/ to /tmp/my_first_directory.
* 8-firstdelete: Delete the file /tmp/my_first_directory/betty.
* 9-firstdirdeletion: Delete the directory /tmp/my_first_directory.
* 10-back: Change the working directory to the previous one.
* 11-lists: lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
* 12-file_type: prints the type of /tmp/iamafile.
* 13-symbolic_link: Create a symbolic link to /bin/ls, named __ls__.
* 14-copy_html: Copy all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
* 100-lets_move: Moves all files beginning with an uppercase letter to the directory /tmp/u.
* 101-clean_emacs: Delete all files in the current working directory that end with the character ~.
* 102-tree: Create the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
* 103-commas: List all the files and directories of the current directory, separated by commas (,).
> Directory names end with a slash (/).
> Files and directories starting with a dot (.) are listed.
> The listing is alpha ordered, except for the directories . and .. which are listed at the very beginning.
> Only digits and letters are used to sort; Digits come first.
* school.mgc: A magic file that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.