# write-up :Stolen
* *1.scan processes with Volatility : vol Stolen.vmem windows.psscan*
* *2.Identify cmd.exe and msedge processes ,first let's view cmdline with : `vol Stolen.vmem windows.cmdline`*
* *3.Find the last executed command : echo "UmVnYXJkcyBmcm9tIHhlbGVzc2F3YXkgdXNlIHRoZSBiYXNlIGFzIHBhc3N3b3Jk" ,when decoding base64 text it gives that message : "Regards from xelessaway use the base as password"*
* *4.now locate the browser history ,i used the following command to search for the history database : `vol Stolen.vmem windows.scanfiles | grep -i history`*
* *5.dump database (the browser history) file :`vol -f  Stolen.vmem -o 'logfiles' windows.dumpfiles --virtaddr 0xa68243fa2250`*
* *6.view the database with `sqlitebrowser` ,found a pastebin link 'https://pastebin.com/zLt4XP5W' .It can be accessed using the password found in the command line,we found a dictionary of password*
* *7.going back to the browser history ,we found a mega link 'https://mega.nz/file/XJAiyIyZ#uElBQQbtUTQ6YNSlD-5EL8g88EkKafmZW8VREk1YrIw' .After downloading and unzipping the file ,we found a file with .kdbx extension which is a database file format used by Keepass ,a popular open-source password manager.*
* *8.we can crack the password for the keepass database with john using the worldlist found previously : `keepass2john keys.kdbx > hash ;john --worldlist=pastebin_dictionary hash`*
* *9.after a few secondes,we obtain the password is **icanfindthishiddenpasswordforcrack***
* *10.finally after opening the Keepaas database we found the flag : **Flag{Bru73_F0RC3_TH3_KDBX_P45$W0RD}***
