# Write-up :Tr4nsf3r
* *1. after downloading and exreacting files from "Tr4nsf3r.7z",you will find a .pcap file and a key.log file is a text-based log containing encryption key data captured when pcap was originally recorded .With this key log file,we can decrypt HTTPS activity in the pcap file*
* *2. to add the key.log in wireshark go to **Edit > Preferences > Protocols > TLS** ,then add the file in Master-Secret log .Now you should be able to see the decrypted TLS traffic*
* *3. when scrolling down the packets we notice this http packet with that request : 'GET /search?query=here!!!%40here!!!-virtualmachine%20Y1sUWLp6NcHeeQxwb52mEaLSsX8qsCEFavFNUuGCcNkV2WiFv.txt' is look like a hint ,the intersting part what the encoded file name*
* *4. take the file name to CyberChef and use Magic on it detect that is a **base58-encoded** text ,after decoding it gives the flag : **Flag{N0_Th1Ng_15_S4F3_3ven_Tr4FF1C5}***
