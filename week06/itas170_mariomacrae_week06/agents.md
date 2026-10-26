**agents.md — three agents, one table**  
Copy this file to week06/agents.md. Fill the Claude Code Desktop and  
   
 OpenCode columns in Part 2 and the Hermes column in Part 4, from what you  
   
 saw today. One short phrase per cell.  
  
|  |  |  |  |  
| - | - | - | - |  
|   |  **Claude Code Desktop** |  **OpenCode** |  **Hermes Agent** |  
| the model, and where it runs |  Opus 5.5 |  Big Pickle |  Itas170 |  
| time for its first answer today |  12 |  38 |  15 |  
| did it ask before running a command or editing a file? |  Yes |  Yes |  Yes |  
| what it remembers in the next session, and where that is kept |  AGENTS.md, CLAUDE.md. Kept in home folder |  AGENTS.md, SKILL.md, kept in home folder and dedicated hidden folders |  Keeps MEMORY.md in dedicated folder |  
| something it told you that you checked (and what you found) |  SKILL.md |  SKILL.md copied over from claude |  My file system for access.log, and its memory file |  
| what it cost you today |  My ITAS Claude seat |  My computer’s RAM and electricity |  The computer’s RAM and memory |  
  
   
Where to find each answer:  
- **the model**: Claude Code Desktop shows it beside the send button;  
   
 OpenCode shows it under the prompt box; Hermes uses the model you gave  
 `ollama launch hermes --model`.  
- **time**: OpenCode prints it after each answer (e.g. `· 52.2s`); Hermes  
   
 prints `Duration:` at the end; for Claude Code Desktop, estimate.  
- **remembers**: Claude Code reads `CLAUDE.md` and `AGENTS.md`; OpenCode  
   
 reads `AGENTS.md`; Hermes keeps `~/.hermes/memories/MEMORY.md`.  
- **cost**: your ITAS Claude seat (paid by ITAS), or nothing but  
   
 electricity for a model on your own computer.  
**Two sentences.** Which of the three would you let run on its own while  
   
 you sleep? What exactly would you let it do, and why that and nothing  
   
 more?  
I would trust Hermes to run while I sleep because it is completely localized and no data leaves your machine. I would only ever trust it to read files. Anything else is too risky. It could harm my files or delete something important.  
