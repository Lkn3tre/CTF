# Write-up :TrueSecrets
* *1. use volatility to scan all file in the memory dump (afer identifying the profile ofc)  and filter for zip files: `python vol.py filescan -f TrueSecrets.raw  --profile=Win7SP1x86_23418 | grep -i ".zip"`*
* *2. notice an interesting file "backup_developement.zip"*
* *3. use the dumpfiles plungin to dump the zip file (with physical adress 0x000000000bbf6158):`python vol.py dumpfiles -Q 0x000000000bbf6158 --dump-dir=. --name zipfile -f TrueSecrets.raw  --profile=Win7SP1x86_23418`*
* *4. after extracting ,you will get a (.tc) file named "development.tc" ,is a container file typically encrypted by a software named TrueCrypt*
* *5. I used VeraCrypt to mount the file but it has a password, I found The password by using the “truecryptpassphrase” plugin: `python vol.py truecryptpassphrase -f TrueSecrets.raw  --profile=Win7SP1x86_23418`*
* *6. Inside the disk, you will find a folder named “malware_agent” which contains four files first one is C# encryption script and the three others are Encrypted by the given script*
* *7. i user a python script to decrypt all tree file the last one has the flag*

