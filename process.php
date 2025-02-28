<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results</title>
</head>
<body>
<h1>Results</h1>
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $numberA = escapeshellarg($_POST['numberA']);
    $numberB = escapeshellarg($_POST['numberB']);
    $numberC = escapeshellarg($_POST['numberC']);
    $numberD = escapeshellarg($_POST['numberD']);
    $numberE = escapeshellarg($_POST['numberE']);



    $command = "python3 data_management.py $numberA $numberB $numberC $numberD $numberE";
    $output = shell_exec($command);

    if ($output === null) {
        echo "<p>Error: Unable to execute the Python script.</p>";
    } else {
        echo "<pre>$output</pre>";
    }
} else {
    echo "<p>Error: Invalid request method.</p>";
}
?>
</body>
</html>
