<?php

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
  'username' => 'Bot',
  'text' => 'fooooo!!!',
);

send_to_slack($message);

?>