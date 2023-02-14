# 0x02 Shell Redirections
* 0-hello_world: Print “Hello, World”, followed by a new line to the standard output.
* 1-confused_smiley: Display a confused smiley "(Ôo)'.
* 2-hellofile: Display the content of the /etc/passwd file.
* 3-twofiles: Display the content of /etc/passwd and /etc/hosts.
* 4-lastlines: Display the last 10 lines of /etc/passwd.
* 5-firstlines: Display the first 10 lines of /etc/passwd.
* 6-third_line: Display the third line of the file iacta.
* 7-file: Create a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
* 8-cwd_state: Write into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, it will be created.
* 9-duplicate_last_line: Duplicate the last line of the file iacta.
* 10-no_more_js: Delete all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
* 11-directories: Count the number of directories and sub-directories in the current directory.
> The current and parent directories are not taken into account.
> Hidden directories are counted.
* 12-newest_files: Display the 10 newest files in the current directory.
> One file per line.
> Sorted from the newest to the oldest.
* 13-unique: Take a list of words as input and prints only words that appear exactly once.
> Input format: One line, one word.
> Output format: One line, one word.
> Words are sorted.
* 14-findthatword: Display lines containing the pattern “root” from the file /etc/passwd.
* 15-countthatword: Display the number of lines that contain the pattern “bin” in the file /etc/passwd.
* 16-whatsnext: Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
* 17-hidethisword: Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
* 18-letteronly: Display all lines of the file /etc/ssh/sshd_config starting with a letter. Capital letters are included as well.
* 19-AZ: Replace all characters A and c from input to Z and e respectively.
* 20-hiago: Remove all letters c and C from input.
* 21-reverse: Reverse its input.
* 22-users_and_homes: Display all users and their home directories, sorted by users.
* 100-empty_casks: Find all empty files and directories in the current directory and all sub-directories.
> Only the names of the files and directories are displayed (not the entire path).
> Hidden files are listed.
> One file name per line.
> The listing ends with a new line.
* 101-gifs: List all the files with a .gif extension in the current directory and all its sub-directories.
> Hidden files are listed.
> Only regular files (not directories) are listed.
> The names of the files are displayed without their extensions.
> The files are sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay).
> One file name per line.
> The listing ends with a new line.
* 102-acrostic: Decode acrostics that use the first letter of each line. The ‘decoded’ message ends with a new line.