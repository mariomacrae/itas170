**gitlog.md — week 2**  
   
 **Part 1 — the first commit**  
   
 git status  
   
   
 On branch master  
   
 Changes not staged for commit:  
(use "git add ..." to update what will be committed)  
   
(use "git restore ..." to discard changes in working directory)  
   
modified:   hunt.md  
git log  
   
  fefb1b7 (HEAD -> master) hunt: deleteed text  
2365d79 First log entry  
   
 gitignore  
   
.env  
   
  secrets/  
   
  .venv/  
   
 node_modules/  
   
   
  *.tmp  
   
git status  
   
    
   
     
   
    
 git add -A  
     
   
    
 git commit -m "Week 1 of ITAS170"  
   
   
    
 git log --oneline  
   
 **Part 2 — the diff, and the recovery**  
   
 Paste the git diff you read aloud, then git log --oneline showing two  
   
    
   
 commits:  
   
 diff  
   
    
   
  diff --git a/LOG.md b/LOG.md  
   
    
   
  index 2e51aa1..bd1bf7a 100644  
   
    
   
  --- a/LOG.md  
   
    
   
  +++ b/LOG.md  
   
 fefb1b7 (HEAD -> master) hunt: deleteed text  
   
    
   
  2365d79 First log entry  
   
    
   
 **Why did ** ** **git restore** ** ** bring ** ** **hunt.md** ** ** back?** One sentence, in your words:  
   
    
   
 Git restore copied the changes from the cache, or staging area. Had we not configured git in the first step, we wouldn't be able to execute these commands.  
   
    
   
 **Part 4 — the remote**  
   
 The URL of your repository on GitHub: [https://github.com/mariomacrae/itas170   
   
 **Part 5 — the log has a history**  
   
 Paste the first five lines of git log -p --oneline -- week01/LOG.md:  
   
 +| | | |  
   
    
   
     
   
    
   
   +|-|-|-|  
   
    
   
     
   
    
   
   +| Question asked | What I got | How I verified it |  
   
    
   
     
   
    
   
   +| “cat , head , tail , wc , grep , cut , sort , uniq  Please explain the purpose of these commands” | Claude explained each of these commands to me, summarizing their purposes. | See below |  
   
    
   
     
   
    
   
   +| “I would like to use it to find patterns in a .md file” | Gave me several ‘grep’ commands to get me started, including ‘grep -i "pattern’. Requested the document so it could run the code itself (which I didn’t do). | I tested out the commands in the terminal |  
   
    
   
     
   
    
   
   +| It’s an access log file. One thing I want to do is to see what five clients made the most requests | Produced the standard combination of code and broke it down for me. | Typed out the command by hand and ran it. |  
   
    
   
     
   
    
   
   +| And then I want to see how many requests each made | Told me that was already included in the previous command and showed me an example/ | Verified it against the produced code  |  
   
    
   
     
   
    
   
   +| Next I would like to find out what hour is the busiest | Produced the standard code combination and explained the different steps |  Ran the code |  
   
    
   
     
   
    
   
  ](https://github.com/mariomacrae/itas170 "https://github.com/mariomacrae/itas170")  
