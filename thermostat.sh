#!/bin/bash 
thermostat_dir="/home/kfieldho/thermostat"
thermostat_current="${thermostat_dir}/thermostat_current.json"
wunderground_current="${thermostat_dir}/wunderground_current.json"
power_current="${thermostat_dir}/power_current.xml"
thermostat_log="${thermostat_dir}/$(date "+%Yw%W")-thermostat_log.json"
#thermostat_error="${thermostat_dir}/thermostat_error.txt"
thermostat_error=/dev/null
power_error=/dev/null
wunderground_key=$(cat ${thermostat_dir}/wunderground_api.txt)

echo -n "{ \"timestamp\": " >> ${thermostat_log}
echo -n "\"$(date -Iseconds) \"" >>  ${thermostat_log}
echo "," >> ${thermostat_log}
echo -n "\"tstat\": " >> ${thermostat_log}
curl http://192.168.168.166/tstat 1> ${thermostat_current} 2>> ${thermostat_error} || echo "{ \"curl_error\": \"Could not connect to thermostat.\" }" > ${thermostat_current}
cat ${thermostat_current} >> ${thermostat_log}
echo "," >> ${thermostat_log}
echo -n "\"wunderground\": " >> ${thermostat_log}
curl http://api.wunderground.com/api/${wunderground_key}/conditions/q/NY/Ballston_Lake.json 1> ${wunderground_current} 2> ${thermostat_error} || echo "{ \"curl_error\": \"Could not connect to wunderground.\" }" >> ${wunderground_current}
cat ${wunderground_current} >> ${thermostat_log}
echo "}," >> ${thermostat_log}
python ${thermostat_dir}/update_rrd.py 
python ${thermostat_dir}/graph_daily_rrd.py
curl http://192.168.168.155/api/LiveData.xml 1> ${power_current} 2>> ${power_error} || echo "<powererror>curl_error: Could not connect to thermostat.</powererror>" > ${power_current}
