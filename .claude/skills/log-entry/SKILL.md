---  
disable-model-invocation: true  
name: log-entry  
---  
**log-entry**  
**Inputs**  
DATE (the date the action was logged)  
   
 TOOL (the assistant used)  
   
 ASKED (What I asked the assistant)  
   
 VERIFIED (How I checked, or "did not check")  
**Steps**  
1. Summarize answer in one or two plain sentences. Never copy it.  
2. If VERIFIED is "did not check", write exactly that and suggest one "next time" line.  
**Output**  
Exactly this shape, and nothing else:  
**DATE · tool: TOOL**  
**Asked:** ASKED and nothing else  
   
 **Got (in my words):** ANSWER (and nothing else)  
   
 **Verified by:** VERIFIED  
   
 **Next time:** suggest another way to verify the answer  
