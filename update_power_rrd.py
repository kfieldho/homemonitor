import os
import xml.etree.ElementTree as ET
import rrdtool

power_dir = "/home/kfieldho/thermostat"
#power_dir="/Users/kfieldho/Projects/Personal/DataAnalysis/homemonitor"
daily_rrd=os.path.join(power_dir,"powerDaily.rrd")

current_power_xml = os.path.join(power_dir,"power_current.xml")

tree = ET.parse(current_power_xml)
root = tree.getroot()

power_now = root.findall('./Power/Total/PowerNow')
if len(power_now):
    #print "N:%d"%(int(power_now[0].text))
    rrdtool.update(daily_rrd,"N:%d"%(int(power_now[0].text)))
