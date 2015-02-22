import os
import json
import rrdtool

thermostat_dir = "/home/kfieldho/thermostat"
daily_rrd=os.path.join(thermostat_dir,"thermostatDaily.rrd")

current_thermostat_json = os.path.join(thermostat_dir,"thermostat_current.json")
current_wunderground_json = os.path.join(thermostat_dir,"wunderground_current.json")

with open(current_thermostat_json,'rb') as current_thermostat_file:
    current_thermostat_data = json.load(current_thermostat_file)


with open(current_wunderground_json,'rb') as current_wunderground_file:
    current_wunderground_data = json.load(current_wunderground_file)

if False:
    print current_thermostat_data
    print current_wunderground_data

    print current_thermostat_data['temp']
    print current_wunderground_data['current_observation']['temp_f']
    print current_thermostat_data['tmode']
    if 't_heat' in current_thermostat_data:
        print current_thermostat_data['t_heat']
    else:
        print current_thermostat_data['t_cool']


if 't_heat' in current_thermostat_data:
    setpoint = current_thermostat_data['t_heat']
else:
    setpoint =  current_thermostat_data['t_cool']

print('N:%f:%f:%f:%d:%d'%(current_thermostat_data['temp'],
    current_wunderground_data['current_observation']['temp_f'],
    setpoint,
    current_thermostat_data['tmode'],
    current_thermostat_data['tstate']
    ))
rrdtool.update(daily_rrd,'N:%f:%f:%f:%d:%d'%(current_thermostat_data['temp'],
    current_wunderground_data['current_observation']['temp_f'],
    setpoint,
    current_thermostat_data['tmode'],
    current_thermostat_data['tstate']
    ))
