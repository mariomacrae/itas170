| | |  
|-|-|  
|   |   |   
|   |   |   
| input | output |   
| uv run —with tiktoken tokens.py sample.txt | file        chars   tokens  chars/tokensample.txt  140    46         3.04                                      |   
| uv run —with tiktoken tokens.py —pieces sample.txt | sample.txt: 140 chars, 46 tokens |   
| uv run --with tiktoken tokens.py ../week01/LOG.md ../week01/hunt.md../week01/access.log  | file                            chars   tokens  chars/token/week01/LOG.md   3,344      819         4.08d            ../week01/hunt.md  901         317         2.84../week01/access.log 420,141  188,054   2.23 |   
| uv run --with tiktoken tokens.py ../week02/ssh3.md | file                              chars   tokens  chars/token../week02/ssh3.md                    1,428      448         3.19 |   
| A web server log is the most expensive type of text because of all the numbers and characters. There is no english for it to compress. |   |   
| The LLM reads ‘strawberries’ 3 ways. Uncapitalized, it reads it as three pieces, and capitalized, 3 different pieces.  With a space after it, it is read as only one word. This is because LLMS read words as tokens and not letters. |   |   
| The ratio for normal English prose is usually 3.19 characters per token. |   |   
|   |   |   
|   |   |   
   
