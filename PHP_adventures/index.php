<?php

for($i = 0; $i <= 10; $i++){
    echo $i;
    echo '<hr>';
}

$i = 0;
while($i < 10)
    echo $i;
    $i++;


printNum(30);
function printNum($n){
    echo $n;
}