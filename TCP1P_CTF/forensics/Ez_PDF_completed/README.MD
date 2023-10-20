# Write-up :Ez_PDF
* *1. Use ExifTool ,notice a base64 chunk. When decoded, you will get this message: `In this question, the flag has been divided into 3 parts. You have found the first part of the flag!! **TCP1P{D01n9_F023n51C5**`*

* *2. Extract all the images from the PDF. One of them contains the second part: **_ON_pdf_f1L35_15_345y***

* *3. When performing a "strings" operation, notice a JavaScript code obfuscates. After understanding what it does, it takes three elements "a, b, c" from the list "_0x3c1521", concatenates them in a certain order, and puts them in "console.log()". That give the third part of the flag: **_15N7_17_l3jaf9ci293m1d}***

Flag: TCP1P{D01n9_F023n51C5_0N_pdf_f1L35_15_345y_15N7_17_l3jaf9ci293m1d}

