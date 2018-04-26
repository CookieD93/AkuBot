<?php 

date_default_timezone_set("Europe/Copenhagen");
$date = date("d. M y");
?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>AkuBotScreen</title>
	<link rel="stylesheet" href="assets/style.css">
	<link rel="stylesheet" href="assets/weather-icons-master/css/weather-icons.min.css">
	<link href="https://fonts.googleapis.com/css?family=Homenaje|Noto+Sans|Oswald|Poiret+One" rel="stylesheet">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <script>
    	function checkTime(i) {
	        if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
	        return i;
	    }
	    function startTime() {
	        var today = new Date();
	        var h = today.getHours();
	        var m = today.getMinutes();
	        var s = today.getSeconds();
	        h = checkTime(h);
	        m = checkTime(m);
	        s = checkTime(s);
	        document.getElementById('time').innerHTML =
	        h + ":" + m;
	        var t = setTimeout(startTime, 500);
	    }
	    
	</script>

</head>
<body onload="startTime();">
	<div id="dateTime">
		<span id="time"></span>
		<p id='date'><?php echo $date ?></p>
	</div>
	<div id="weather">da</div>
	<script>
	    $(function(){
	        $("#weather").load("wheatherGet.php");
	        setInterval(function(){
	            $("#weather").load("wheatherGet.php");
	    	},300000)
		});
	</script>
</body>
</html>