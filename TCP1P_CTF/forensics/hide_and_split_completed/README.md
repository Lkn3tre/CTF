# Write-up :Diagnotic
* *1. List files on the disk with:* 
```sh
fls challenge.ntfs
```
* *2. Notice that the file "flag0" starts with "89504e47," which is a PNG header.*
* *3. Collect all files with names starting with **flag0** to **flag99** into one file, **flag.png** using the following command:* 
```sh
for i in {64..163};do icat challenge.ntfs $i-128-4;done > flag.png
```
* *4. It's a QR code. Decode it to get the flag: **TCP1P{hidden_flag_in_the_extended_attributes_fea73c5920aa8f1c}***


