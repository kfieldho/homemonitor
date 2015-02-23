#power_dir=/home/kfieldho/thermostat
power_dir=/Users/kfieldho/Projects/Personal/DataAnalysis/homemonitor

rrdtool create $power_dir/powerDaily.rrd \
    -s 300 \
    DS:currentPower:GAUGE:599:0:50000 \
        RRA:AVERAGE:0.5:1:288 
