curl -s http://localhost:8081 | grep h1
  <h1>Mario Macrae Web Portfolio</h1>
curl -s http://localhost:8081 | grep -i "Buying physical media"
<li>Buying physical media (books, DVDs, vinyl/CDs)</li>
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mysite:1       1369555ef505       93.7MB         26.4MB        
mysite:2       723f4183161a       93.7MB         26.4MB        
mysite:model   f95f6fb70d6f       73.7MB           21MB      
The localhost hosted my page fine, the only problem was the layout.
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
mysite:1       1369555ef505       93.7MB         26.4MB    U   
mysite:2       723f4183161a       93.7MB         26.4MB        
mysite:model   94a63d357d00       73.7MB           21MB        
Both docker images mysite outputs were the same, with the dockerfile.model one having a 'u' under extra, meaning that the image was in use.
