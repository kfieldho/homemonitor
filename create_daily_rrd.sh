thermostat_dir=/home/kfieldho/thermostat

rrdtool create $thermostat_dir/thermostatDaily.rrd \
    -s 300 \
    DS:indoorTemperature:GAUGE:599:-100:200 \
    DS:outdoorTemperature:GAUGE:599:-100:200 \
        RRA:AVERAGE:0.5:1:288 \
    DS:setPoint:GAUGE:599:0:100 \
    DS:thermostatMode:GAUGE:599:0:10 \
        RRA:MAX:0.9:1:288 \
    DS:thermostatState:GAUGE:599:0:10 \
        RRA:MAX:0.9:1:288 
