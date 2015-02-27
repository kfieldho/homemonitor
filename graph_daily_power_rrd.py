import os
import rrdtool

thermostat_www = "/var/www/thermostat"
power_dir = "/home/kfieldho/thermostat"
daily_rrd=os.path.join(power_dir,"powerDaily.rrd")
daily_graph=os.path.join(thermostat_www,"powerDaily.png")

rrdtool.graph(daily_graph,
        '--title',' Daily Power Usage',
        '--vertical-label','Watts',
        'DEF:currentPower=%s:currentPower:AVERAGE'%(daily_rrd),
            'LINE2:currentPower#ccccff:currentPower',
        'GPRINT:currentPower:LAST:Current Usage\: %6.0lf watts',
        )
