| | |  
|-|-|  
|   |   |   
| input | output |   
| uv run —with tiktoken tokens.py sample.txt | file        sample.txt                               chars   140 tokens  46   chars/token   3.04                                      |   
| uv run —with tiktoken tokens.py —pieces sample.txt | sample.txt: 140 chars, 46 tokensThe |   
| uv run --with tiktoken tokens.py ../week01/LOG.md ../week01/hunt.md | file                                 chars   tokens  chars/token../week01/LOG.md                     3,344      819         4.08../week01/hunt.md                      901      317         2.84../week01/access.log               420,141  188,054         2.23 |   
| uv run --with tiktoken tokens.py ../week02/ssh3.md | file                                 chars   tokens  chars/token../week02/ssh3.md                    1,428      448         3.19 |   
|   |   |   
|   |   |   
| A web server log is the most expensive type of text because of all the numbers and characters. There is no english for it to compress. |   |   
| The LLM reads ‘strawberries’ 3 ways. Uncapitalized, it reads it as three pieces, and capitalized, 3 different pieces.  St | raw |   
| The ratio for normal inglish prose is usually 3.19 characters per token. |   |   
|   |   |   
   
