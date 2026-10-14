**2 WEEKS**  
**sort -k10,10n access.log | tail -1**  
**sort reorders the lines of access.log.**  
**-k10,10 restricts the sort key to field 10 only (through field 10), instead of the whole line.**  
**n (attached to the key spec) tells sort to compare that field numerically rather than as text.**  
**access.log is the input file sort reads and sorts.**  
**Common mistake: writing -k10 alone instead of -k10,10. Without the second number, sort uses field 10 through the end of the line as the key, not just field 10, which silently changes the ordering when later fields differ.**  
**10 YEARS**  
**-k10,10n: sort using only field 10 as the key, treated numerically  
  tail -1: print only the last line of sort's output**  
**Common mistake: forgetting the n flag (or forgetting to restrict the field with 10,10) — plain -k10 sorts from field 10 to the end of the line as one string key, and without n the values sort lexicographically, so 9 comes after 100.**  
The two ${LEVEL} values I used were “two weeks” and “ten years”  
The answer for ‘two weeks’ explained every part of the pipeline and its purpose (except for tail -1), while the answer for ‘ten years’ explained only –k10 and-k10n as well as tail -1.  
The answer for ‘two weeks’ did not mention why it was important to have the ‘n’ in 10n.   
One rule I would add would be to add a checklist of proper syntax for executing the command. It’s easy to make typographical errors and not notice, but even a missed space can ruin an entire command. At least I would include it in the rules for the two-week prompt.  
   
