query : select 1234 fromprob_giant where 1
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
// string length must be no longer than 1?
// that's strict...

  if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
// new line, carriage return, tab are not allowed....

  $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
  // shit?= prepended to prob_giant table I think
  // but also if result is 1234, from any tables? then this is passsed?
  // // that being said, this just needs a whitespace so that table name can be separated in the query
  // so the answer is supposed to be always 1234 I guess.

  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 

  if($result[1234]) solve("giant"); 
  highlight_file(__FILE__);

?>