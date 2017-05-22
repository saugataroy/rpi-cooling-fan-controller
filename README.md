# Raspberry Pi cooling fan controller

A Raspberry Pi doesn't exactly need a cooling fan. But is cool to see a Pi programmatically control a fan. Moreover, a cool breeze now and then doesn't harm.

What may really harm a Pi, however, is a fan directly connected to the GPIO. A simple transistor based circuit is used to power the fan externally.

### Installing

Save the file cooling_fan.py at a convenient location e.g. /home/pi/cooling_fan.py

Update variable values in the file

> BCM_output_pin=18   #GPIO pin for PWM output
> ontemp=60           #in deg C      
> offtemp=55          #in deg C
> max_fan_speed=80	  # maximum speed in percent 0-100

Execute and test

> sudo python /home/pi/cooling_fan.py

Add to cron

## Authors

* **Saugata Roy** - *Initial work* - [saugataroy](https://github.com/saugataroy)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
