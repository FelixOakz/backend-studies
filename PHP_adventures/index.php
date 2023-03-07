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


class Pessoa {

    public $nome;
    public $idade;

    public function __construct($nome, $idade) {
    $this->nome = $nome;
    $this->idade = $idade;
    }

    public function printNomeEIdade(){
        echo $this->nome;
        echo '<br>';
        echo $this->idade;
    }
}

// intanciar a classe , precisa ser chamada assim como uma funcão

$pessoa = new Pessoa('Guilherme', '26');

$arr = ['guilherme', 'joao', 'felipe'];

echo $arr[1];