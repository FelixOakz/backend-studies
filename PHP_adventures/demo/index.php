<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <style>
    body {
        scroll-behavior: auto;
        display: grid;
        place-items: center;
        height: 100vh;
        margin: 0;
        font-family: sans-serif;
    }
    </style>
</head>

<body>
    <?php
        $name = "Dark Matter";
        $read = true;
    ?>
    <h1>
        You have read "<?php echo $name; ?>."
    </h1>
</body>

</html>