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
| qwen3:4b | 4 | 2GB | 2GB | yes | yes | yes | yes | yes |   
| qwen3:8b | 8 | 6GB | 2GB | yes | yes | yes | yes | yes |   
| a 14B | 14 | 8GB | 2GB | no | yes | es | yes | yes |   
| Qwen3.8-27B | 27 | 10GB | 4GB | no | yes | yes | yes | yes |   
| a 32B | 32 | 12GB | 8GB | no | yes | yes | yes | yes |   
| a 70B | 70 | 36GB | 16GB | no | no | no | yes | yes |   
| Qwen3.8-Max (2.4T MoE) | 2400 | 128GB | 32GB | no |  no | no | no | no |   
   
**Checked:** ollama ps showed qwen3:4b using 5.2 GB while answering.  
   
 My prediction for that row was 2GB. Difference: 3.2 GB.  
**One sentence:** does a model that *fits* in system RAM run well on a CPU?  
   
 Yes, it will run stably on a CPU but will be much slower in turn.  
qwen3:8b    500a1f067a9f    5.2 GB    3 hours ago      
Model  
    architecture        qwen3       
    parameters          4.02B       
    context length      40960       
    embedding length    2560        
    quantization        Q4_K_M      
   
  Capabilities  
    completion      
    tools           
    thinking        
   
  Parameters  
    stop                "<|im_start|>"      
    stop                "<|im_end|>"        
    min_p               0                   
    presence_penalty    1.5                 
    top_k               20                  
    num_ctx             40960               
    temperature         0.6                 
    repeat_penalty      1                   
    top_p               0.95                
    num_predict         32768               
   
  License  
    Apache License                 
    Version 2.0, January 2004      
    ...                            
   
mario.macrae@BITS-YR1-114:~/code/ITAS170/week04$ ollama list  
NAME                               ID              SIZE      MODIFIED      
hf.co/Qwen/Qwen3-4B-GGUF:Q4_K_M    3c4f22130d40    2.5 GB    4 hours ago      
qwen3:8b                           500a1f067a9f    5.2 GB    4 hours ago      
qwen3:4b                           359d7dd4bcda    2.5 GB    4 hours ago      
