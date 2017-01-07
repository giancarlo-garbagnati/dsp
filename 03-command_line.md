# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > `ls -lG`                                              - colorful list in column format  
> > `cd`                                                  - change directory  
> > `..`                                                  - one directory up (towards root)  
> > `/`                                                   - root directory (not '.')  
> > `pwd`                                                 - print working directory (in case I'm lost)  
> > `mkdir`                                               - make a directory  
> > `touch`                                               - makes a new file in the current directory  
> > `cp fileorfilestocopy.txt whereandwhattocopyto.txt`   - copy a file  
> > `*`                                                   - everything (in a dir), like when copying, can also use as a wildcard  
> > `mv`                                                  - move a file to another destination, can move multiple files, and/or rename files in the moving process  
> > `rm`                                                  - delete (remove) a file  
> > `rm -r`                                               - delete a directory (and it's contents) ('r' for recursive)  
> > `echo "String"`                                       - outputs a string to the terminal ("String" in this example)  
> > `>`                                                   - redirecting an output of something to a different file  
> > `cat foo.txt`                                         - outputs the content of a file to the terminal, can also use > to redirect the contents of that file elsewhere  
> > `>>` .                                                - redirects an output of something to a different file, but keeps the original contents  
> > `<`                                                   - takes the standard input from the file on the right and inputs it into the program on the left  
> > `|`                                                   - pipe, takes the std output o the command on the left and pipes it as std input to the command on the right  
> > `wc`                                                  - some kind of a word count program (outputs the number of words/lines/characters)  
> > `sort`                                                - sorts something alphabetically  
> > `uniq` .                                              - filters out adjacent, duplicate lines in a file  
> > tab                                                   - will try to guess and fill in the rest of the command  
> > `grep pattern fileToSearchIn.txt`                     - search within a file for all entries that contain a pattern, "global regular expression print"  
> > `grep -i pattern file.txt`                            - grep, but case insensitive  
> > `grep -R`                                             - grep recursive, to use to search within a directory  
> > `grep -Rl`                                            - grep R, but lists files that contain the pattern  
> > `sed 's/snow/rain/' forests.txt`                      - sed = stream editor, accepts std input and modifies it based on an expression, similar to find and replace, 's' stands for substution 'snow' is the search string to find 'rain' is the replacement string to add in place, this will only replace the first instance per line  
> > `sed 's/snow/rain/g' forests.txt`                      - same as the one above, but the 'g' makes it global and replaces all instances of the search string to the replacement string  
> > ``                                           -  
> > ``                                           -  


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`       - List all files in a directory
> > `ls -a`    - List all files in a directory (including files prefaced with ".")
> > `ls -l`    - List all files, in column format
> > `ls -lh`   - Does the same as "ls -l" but printed in sizes in human readable format
> > `ls -lah`  - Does the same as both "ls -lh" and "ls -a" combined
> > `ls -t`    - Sorts all the items by modification time
> > `ls -Glp`  - Does the same as "ls -l" but appends a file-type indicator (one of "/" "=" "@" or "|"), and also adds color to the output

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

