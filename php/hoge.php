<?php

$username = htmlspecialchars($_POST['user']);
$text = htmlspecialchars($_POST['message']);
$channel = htmlspecialchars($_POST['channel']);

function send_to_slack($message) {
	$webhook_url = 'https://hooks.slack.com/services/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';
	$options = array(
		'http' => array(
    	'method' => 'POST',
    	'header' => 'Content-Type: application/json',
    	'content' => json_encode($message),
    )
  );
  $response = file_get_contents($webhook_url, false, stream_context_create($options));
  return $response === 'ok';
}

$message = array(
  'username' => $username,
  'text' => $text,
  'channel' => '#'.$channel
);

send_to_slack($message);

echo "送信完了しました。";
print <<< html
<html>
<head>
	<meta charset="utf-8">
	<title>sentSlack</title>
</head>
<body>
	<a href="hoge.html">もどる</a>
</body>
</html>
html;

?>