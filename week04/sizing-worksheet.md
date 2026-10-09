**sizing.md — how much memory does a model need?**  
The rule of thumb, good to about 20%:  
memory (GB)  ≈  parameters (billions)  ×  bytes per parameter  +  working room  
| | | |  
|-|-|-|  
| **precision** | **bytes per parameter** | **who uses it** |   
| FP16 / BF16 | 2.0 | the model as released |   
| Q8 | 1.0 | high-quality quantized |   
| **Q4 (Q4_K_M)** | **~0.6** | Ollama's default download |   
   
**Working room** (the KV cache — the model's memory of the conversation so  
   
 far — plus overhead): call it **1–2 GB** at the default context window, and  
   
 more the longer the window you set. It grows with context, not with the  
   
 model's size alone.  
**Fill in the table**  
Predict first, then check one row against ollama show MODEL and  
   
 ollama ps while it is running. The last column is the desktop you are  
   
 sitting at: 64 GB, no graphics card.  
| | | | | | | | | |  
|-|-|-|-|-|-|-|-|-|  
| **model** | **parameters** | **Q4 weights (GB)** | **+ working room** | **fits 8 GB?** | **16 GB?** | **24 GB?** | **32 GB?** | **64 GB?** |   
| qwen3:4b | 4 |   |   |   |   |   |   |   |   
| qwen3:8b | 8 |   |   |   |   |   |   |   |   
| a 14B | 14 |   |   |   |   |   |   |   |   
| Qwen3.8-27B | 27 |   |   |   |   |   |   |   |   
| a 32B | 32 |   |   |   |   |   |   |   |   
| a 70B | 70 |   |   |   |   |   |   |   |   
| Qwen3.8-Max (2.4T MoE) | 2400 |   |   |   |   |   |   |   |   
   
**Checked:** ollama ps showed qwen3:__ using ______ GB while answering.  
   
 My prediction for that row was ______. Difference: ______.  
**One sentence:** does a model that *fits* in system RAM run well on a CPU?  
   
 (Your eval rate from Part 1 is the evidence.)  
   
