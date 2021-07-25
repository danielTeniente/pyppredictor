# Pico y placa predictor
This module can tell if a car plate can be on the road. There are four rules depending on the year. Each rule was extracted from:
* [Wikipedia](https://es.wikipedia.org/wiki/Pico_y_placa#Quito,_Ecuador)
* [El comercio](https://www.elcomercio.com/actualidad/quito/circulacion-vehicular-no-circula-quito.html)
* [Agencia metropolitana](http://www.amt.gob.ec/index.php/servicios/hoy-no-circula.html)

## Execute the module
Use:  

python main.py car_plate date time  

Parameters:  

car_plate: digits of the car's plate  

date: in format dd/mm/yy  

time: in format hh:mm:ss  

example:  

python main.py AAC-0123 24/07/21 18:52:30

## Testing
There are two testing files:
* test.py for testing functions
* test_main.py for testing main function