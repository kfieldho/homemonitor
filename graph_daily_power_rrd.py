import os
import rrdtool

thermostat_www = "/var/www/thermostat"
thermostat_dir = "/home/kfieldho/thermostat"
daily_rrd=os.path.join(thermostat_dir,"thermostatDaily.rrd")
daily_graph=os.path.join(thermostat_www,"thermostatDaily.png")

rrdtool.graph(daily_graph,
        '--title',' Daily Temperature',
        '--vertical-label','degrees F',
        'DEF:indoorTemperature=%s:indoorTemperature:AVERAGE'%(daily_rrd),
            'AREA:indoorTemperature#ccffcc:IndoorTemperature',
        'DEF:outdoorTemperature=%s:outdoorTemperature:AVERAGE'%(daily_rrd),
            'LINE1:outdoorTemperature#aaaaaa:OutdoorTemperature',
        'DEF:setPoint=%s:setPoint:MAX'%(daily_rrd),
            'LINE1:setPoint#0000ff:SetPoint',
        'DEF:thermostatState=%s:thermostatState:MAX'%(daily_rrd),
        'DEF:thermostatMode=%s:thermostatMode:MAX'%(daily_rrd),
        'CDEF:heating=indoorTemperature,thermostatState,1,EQ,*',
            'AREA:heating#ffcccc:Furnace On',
        'CDEF:cooling=indoorTemperature,thermostatState,2,EQ,*',
            'AREA:cooling#ccccff:AC On',
        'GPRINT:indoorTemperature:LAST:Current Indoor Temp\: %2.1lf F',
        'GPRINT:outdoorTemperature:LAST:Current Outdoor Temp\: %2.1lf F',
        'GPRINT:setPoint:LAST:Current Set Point\: %2.1lf F',
        )
