#When you create repo in Github so its brach nme is main.
#When you create repo in local so its branch nme is master.

git init  
git add command.py or git add. # to taale fie rom untrcked to staged
git rm --cached command.py # to take back from stage to untracked
git commit -m "added command file" #to take stage to tracked

# How to restore deleted file:

git rm command.py
git status # You can see deleted file here{deleted: comand.py}
git restore command.py