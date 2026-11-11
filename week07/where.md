uname -r: 7.0.0-31-generic

lsblk -f: 
NAME        FSTYPE   FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0       squashfs 4.0                                                    0   100% /snap/bare/5
loop1       squashfs 4.0                                                    0   100% /snap/core22/2955
loop2       squashfs 4.0                                                    0   100% /snap/core24/1643
loop3       squashfs 4.0                                                    0   100% /snap/core24/2124
loop4       squashfs 4.0                                                    0   100% /snap/core26/462
loop5       squashfs 4.0                                                    0   100% /snap/onlyoffice-desktopeditors/1706
loop6       squashfs 4.0                                                    0   100% /snap/desktop-security-center/188
loop7       squashfs 4.0                                                    0   100% /snap/firmware-updater/226
loop8       squashfs 4.0                                                    0   100% /snap/snap-store/1447
loop9       squashfs 4.0                                                    0   100% /snap/gnome-46-2404/153
loop10      squashfs 4.0                                                    0   100% /snap/gnome-mines/326
loop11      squashfs 4.0                                                    0   100% /snap/gtk-common-themes/1535
loop12      squashfs 4.0                                                    0   100% /snap/mesa-2404/1839
loop13      squashfs 4.0                                                    0   100% /snap/mesa-2404/1165
loop14      squashfs 4.0                                                    0   100% /snap/onlyoffice-desktopeditors/1220
loop15      squashfs 4.0                                                    0   100% /snap/prompting-client/222
loop16      squashfs 4.0                                                    0   100% /snap/prompting-client/228
loop17      squashfs 4.0                                                    0   100% /snap/thunderbird/1282
loop18      squashfs 4.0                                                    0   100% /snap/firefox/8995
loop19      squashfs 4.0                                                    0   100% /snap/snapd/27738
loop20      squashfs 4.0                                                    0   100% /snap/core26/646
loop21      squashfs 4.0                                                    0   100% /snap/snapd-desktop-integration/361
loop22      squashfs 4.0                                                    0   100% /snap/snapd-desktop-integration/391
loop23      squashfs 4.0                                                    0   100% /snap/pinta/98
loop24      squashfs 4.0                                                    0   100% /snap/firefox/9036
loop25      squashfs 4.0                                                    0   100% /snap/thunderbird/1259
loop26      squashfs 4.0                                                    0   100% /snap/snap-store/1427
loop27      squashfs 4.0                                                    0   100% /snap/gnome-46-2404/168
loop28      squashfs 4.0                                                    0   100% /snap/dg-adw-gtk3-theme/15
loop29      squashfs 4.0                                                    0   100% /snap/desktop-security-center/206
loop30      squashfs 4.0                                                    0   100% /snap/astral-uv/1773
loop31      squashfs 4.0                                                    0   100% /snap/cups/1262
loop32      squashfs 4.0                                                    0   100% /snap/snapd/28254
loop33      squashfs 4.0                                                    0   100% /snap/pinta/101
loop34      squashfs 4.0                                                    0   100% /snap/astral-uv/1781
loop35      squashfs 4.0                                                    0   100% /snap/firmware-updater/262
loop36      squashfs 4.0                                                    0   100% /snap/cups/1266
loop37      squashfs 4.0                                                    0   100% /snap/mesa-2604/123
loop38      squashfs 4.0                                                    0   100% /snap/gnome-core26/33
nvme0n1                                                                              
├─nvme0n1p1 vfat     FAT32       7011-5C4D                                 1G     1% /boot/efi
└─nvme0n1p2 ext4     1.0         dfa21990-5c4d-4095-8542-dda74abec6c0  398.5G    10% /

df -hT ~ /tmp /dev/shm:
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/nvme0n1p2 ext4   468G   46G  399G  11% /
tmpfs          tmpfs  7.5G  314M  7.2G   5% /tmp
tmpfs          tmpfs  7.5G   23M  7.5G   1% /dev/shm

df -hT /run/media/$USER/*:
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      vfat   15G   32K   15G   1% /run/media/mario.macrae/BEA1-BC0B

/tmp is from RAM here, we know because of the line 7.5G  314M  7.2G   5% /tmp

