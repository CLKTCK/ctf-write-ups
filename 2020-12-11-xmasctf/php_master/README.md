# PHP Master
[@katipuzer0](https://twitter.com/katipuzer0)

This web challenge requires us to specify the correct parameters to get the flag. 

### Given
We are given the following PHP code:

```php
<?php

include('flag.php');

$p1 = $_GET['param1'];
$p2 = $_GET['param2'];

if(!isset($p1) || !isset($p2)) {
    highlight_file(__FILE__);
    die();
}

if(strpos($p1, 'e') === false && strpos($p2, 'e') === false  && strlen($p1) === strlen($p2) && $p1 !== $p2 && $p1[0] != '0' && $p1 == $p2) {
    die($flag);
}

?>

```

### Approach
To find the flag, we need to review some of the interesting [properties](https://medium.com/@Asm0d3us/part-1-php-tricks-in-web-ctf-challenges-e1981475b3e4) of PHP's comparison operators. We also note the the second parameter of the `strpos()` function is case-sensitive.

### Exploit
```
http://challs.xmas.htsp.ro:3000/?param1=100&param2=1E2
```
The values of param1 and param2 satisfy the condition: 100=1x10^2=1E2

### Flag
`X-MAS{s0_php_m4ny_skillz-69acb43810ed4c42}`
