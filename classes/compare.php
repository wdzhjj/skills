<?php
require_once("Picmatch.php");
$src1 = '1.jpg';
$src2 = '11.jpg';
$P = new Picmatch();

$color1 = $P->getColor($src1);
$color2 = $P->getColor($src2);
var_dump($color1);
var_dump($color2);

$compare = $P->match($color1,$color2);
var_dump($compare);
