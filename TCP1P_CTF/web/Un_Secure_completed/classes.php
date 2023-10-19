<?php
namespace GadgetThree {

class Vuln
{
    public $waf1;
    protected $waf2;
    private $waf3;
    public $cmd;

    public function __construct($waf1, $waf2, $waf3, $cmd)
    {
        $this->waf1 = $waf1;
        $this->waf2 = $waf2;
        $this->waf3 = $waf3;
        $this->cmd = $cmd;
    }

    public function __toString()
    {
        if (!($this->waf1 === 1)) {
            die("not x");
        }
        if (!($this->waf2 === "\xDE\xAD\xBE\xEF")) {
            die("not y");
        }
        if (!($this->waf3 === false)) {
            die("not z");
        }
        eval($this->cmd);
    }
}
}
namespace GadgetOne {

class Adders
{
    private $x;

    function __construct($x)
    {
        $this->x = $x;
    }

    function get_x()
    {
        return $this->x;
    }
}
}
namespace GadgetTwo {

class Echoers
{
    public $klass;

//    function __destruct()
//    {
 //       echo $this->klass->get_x();
  //  }
}
}

?>
