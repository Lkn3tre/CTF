# Write-up :Red Failure
* *1.export http object from pcap file with : `tshark -r capture.pcap --export-objects "http,out_path"`*
* *2.deobfuscat the powershell script relize that the script download something from 147.182.172.189 "9tVIO" and "user32.dll"*
* *3.user32.dll is .NET program we can open it with DnSpy*



