I predict that the write test will be the slowest, and be 50 times slower than my home folder.

test                ext4           ram           usb
create           4.63(3)       4.03(3)     355.46(1)
read             0.03(3)       0.02(3)       0.03(1)
git              0.19(3)       0.16(3)     581.79(1)
big200MB         0.16(3)       0.08(3)      30.29(1)
delete           0.06(3)       0.04(3)      99.49(1)

test              ram / ext4        usb / ext4
create                  0.9x             76.8x
read                    0.7x              1.0x
git                     0.8x           3062.1x
big200MB                0.5x            189.3x
delete                  0.7x           1658.2x
The slowest test on my stick was git. I think that since the files were not kept in memory, the test took much longer. 
My prediction for the test was incorrect. The write test was the second slowest, with the slowest being the git test. The test was also 75x slower, not 50x like i predicted.
The pooled table has two extra columns of information that my table alone did not (usb2, ntfs-9p.)
