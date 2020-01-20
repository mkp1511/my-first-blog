"""

Subsequent steps:
(1) git status
(2) git add --all     OR     git add -A
(3) git status
(4) git commit -m "comment"
(5) git push





First time steps:

(1)
(girls) MK:djangogirls purohit$ git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout    Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.

(2)
(girls) MK:djangogirls purohit$ git --version
git version 2.20.1 (Apple Git-117)


(3)
(girls) MK:djangogirls purohit$ git init
Initialized empty Git repository in /Users/purohit/projects/djangogirls/.git/


(4)
(girls) MK:djangogirls purohit$ git config --global user.name "mahendra"


(5)
(girls) MK:djangogirls purohit$ git config --global user.email "mkpurohit.imd2007@gmail.com"


(6)
(girls) MK:djangogirls purohit$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
	blog/
	djangogirls.code-workspace
	girls/
	manage.py
	mysite/
	requirements.txt
	working_steps.py

nothing added to commit but untracked files present (use "git add" to track)


(7)
(girls) MK:djangogirls purohit$ git add -A


(8)
(girls) MK:djangogirls purohit$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   .gitignore
	new file:   blog/__init__.py
	new file:   blog/admin.py
	new file:   blog/apps.py
	new file:   blog/migrations/0001_initial.py
	new file:   blog/migrations/__init__.py
	new file:   blog/models.py
	new file:   blog/templates/blog/post_list.html
	new file:   blog/tests.py
	new file:   blog/urls.py
	new file:   blog/views.py
	new file:   manage.py
	new file:   mysite/__init__.py
	new file:   mysite/settings.py
	new file:   mysite/urls.py
	new file:   mysite/wsgi.py
	new file:   requirements.txt
	new file:   working_steps.py


(9)
(girls) MK:djangogirls purohit$ git commit -m 'first commit'
[master (root-commit) 4a3fbdd] first commit
 18 files changed, 471 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 blog/__init__.py
 create mode 100644 blog/admin.py
 create mode 100644 blog/apps.py
 create mode 100644 blog/migrations/0001_initial.py
 create mode 100644 blog/migrations/__init__.py
 create mode 100644 blog/models.py
 create mode 100644 blog/templates/blog/post_list.html
 create mode 100644 blog/tests.py
 create mode 100644 blog/urls.py
 create mode 100644 blog/views.py
 create mode 100755 manage.py
 create mode 100644 mysite/__init__.py
 create mode 100644 mysite/settings.py
 create mode 100644 mysite/urls.py
 create mode 100644 mysite/wsgi.py
 create mode 100644 requirements.txt
 create mode 100644 working_steps.py


(10)
(girls) MK:djangogirls purohit$ git remote add origin https://github.com/mkp1511/my-first-blog.git
fatal: remote origin already exists.


(11)
(girls) MK:djangogirls purohit$ git push -u origin master
Enumerating objects: 23, done.
Counting objects: 100% (23/23), done.
Delta compression using up to 4 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (23/23), 6.54 KiB | 1.64 MiB/s, done.
Total 23 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/mkp1511/my-first-blog.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
(girls) MK:djangogirls purohit$ 

"""
