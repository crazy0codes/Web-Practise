<?php

/*// CONNCETION TO MY SQL DATABASE//

$host = "127.0.0.1";
$name = "root";
$pswd = "";
$db = "etc";
$conn = mysqli_connect($host,$name,$pswd,$db);
if(!$conn){
    echo "Connection Error" .mysqli_connect_error();
    exit;
}
$sql = "INSERT INTO STUDENTS VALUES ('MADHAN','madhan#4332','mdaaa')";
$result = mysqli_query($conn,$sql);
if(!$result){
    echo "NOT SAVED" .mysqli_error($conn);
    exit;
}
echo "Regestration Successsful";
mysqli_close($conn)*/

/*//_______________LOOPs______________//

//for//
for($i=0;10>$i;$i++) {
    echo $i;
}
//while//
$M = 23;
$B = 1;
while($M > $B){
    echo $B;
    $B++;
}
//do __ while//
do{
    echo $B;
    $B++;
}
while($M > $B);

$Array = array("Madhan","Mahaan");
foreach($Array as $Arrays){
    echo 'i'.$Arrays;
}
*/
// => IMPORTANCE //
/* 
$data = array
(
    "Amit" => array(
        "phy" => 60,
        "che" => 50,
        "maths" => 68
    ),
    "Arjun" => array(
        "phy" => 60,
        "che" => 50,
        "maths" => 68
    ),
    "Doraemon" => array(
        "phy" => 60,
        "che" => 50,
        "maths" => 68
    ),
    "Nobita" => array(
        "phy" => 44,
        "che" => 43,
        "maths" => 21
    )
);

foreach($data as $datas => $Names){
    foreach($Names as $subject => $Marks ){
        echo 
    }
}
*/
/*$domain="hackerrank.com";
if(checkdnsrr($domain)) {
  echo "Passed";
} else {
  echo "Failed";
}
echo gethostname();*/

/*$portnum = getservbyname("http", "tcp");
echo $portnum;*/

/*$intservname = getservbyport(80, "tcp");
echo $intservname;*/

/*$addr = inet_pton("127.0.1.1");
echo $addr;*/

// PASSWORD HASHING //

//echo password_hash("Goldenduck:VAK VAK",PASSWORD_DEFAULT);

//$hash = '$2y$10$NdhsHF7Mz/yj7fRtho6V/.yeB9A1qhqOWE2bfGYPyNSoCARDvnA.6';

/*if (password_verify('Madhan#4332', $hash)) {
    echo 'Password is valid!';
} else {
    echo 'Invalid password.';
}*/
?>
