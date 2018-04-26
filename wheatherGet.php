<?php
$ForeCast = simplexml_load_file("http://www.yr.no/place/Denmark/Zealand/Roskilde/forecast_hour_by_hour.xml");
$NextForeCast = $ForeCast->forecast->tabular->time;

$weatherDescriptionArray = array(

	"1"=>"wi-day-sunny",
	"2"=>"wi-day-cloudy-high",
	"3"=>"wi-day-cloudy",
	"4"=>"wi-cloudy",
	"40"=>"wi-sprinkle",
	"5"=>"wi-showers",
	"41"=>"wi-rain",
	"24"=>"wi-storm-showers",
	"6"=>"wi-thunderstorm",
	"25"=>"wi-rain",
	"42"=>"wi-sleet",
	"7"=>"wi-sleet",
	"43"=>"wi-sleet",
	"26"=>"wi-storm-showers",
	"20"=>"wi-storm-showers",
	"27"=>"wi-storm-showers",
	"44"=>"wi-snow",
	"8"=>"wi-snow-wind",
	"45"=>"wi-snow-wind",
	"28"=>"wi-storm-showers",
	"21"=>"wi-storm-showers",
	"29"=>"wi-storm-showers",
	"46"=>"wi-sprinkle",
	"9"=>"wi-rain",
	"10"=>"wi-showers",
	"30"=>"wi-storm-showers",
	"22"=>"wi-storm-showers",
	"11"=>"wi-thunderstorm",
	"47"=>"wi-rain-mix",
	"12"=>"wi-rain-mix",
	"48"=>"wi-rain-mixd",
	"31"=>"wi-storm-showers",
	"23"=>"wi-storm-showers",
	"32"=>"wi-storm-showers",
	"49"=>"wi-snow",
	"13"=>"wi-snow",
	"50"=>"wi-snow-wind",
	"33"=>"wi-storm-showers",
	"14"=>"wi-storm-showers",
	"34"=>"wi-storm-showers",
	"15"=>"wi-fog"

);
$WeatherSymbolNumber = $NextForeCast[0]->symbol->attributes()["number"];
$weatherDescription = $weatherDescriptionArray[trim($WeatherSymbolNumber)];
$WeatherSymbolVar = $NextForeCast[0]->symbol->attributes()["var"];
$WeatherTemperature = $NextForeCast[0]->temperature->attributes()["value"];
$weatherIcon = $weatherDescriptionArray[trim($WeatherSymbolNumber)];

echo "<span class='temp'><i class='wi ".$weatherIcon." wi-fw weatherIcon'></i>$WeatherTemperature<span class='degrees'>&deg;C</span></span>";

?>