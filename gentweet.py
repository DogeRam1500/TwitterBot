f=open('/home/pi/consolewdfiles/twitter.txt', 'r')
tweet=open('/home/pi/tweet.txt', 'w')
lines=f.readlines()
variables=[]
for i in lines:
    variables.append(i)
sunrise=variables[0]
sunset=variables[1]
temp_str=variables[2]
dew=variables[3]
heatindex_str=variables[4]
chill_str=variables[5]
windsp=variables[6]
gust_kts=variables[7]
winddir=variables[8]
cardinal=variables[9]
baro=variables[10]
barotrend=variables[11]
hourlyrain=variables[12]
dailyrain=variables[13]
solarrad=variables[14]
uv=variables[15]
soilmoist=variables[16]
soiltemp=variables[17]
time=variables[18]
soiltemp2=variables[19]
soiltemp3=variables[20]
soiltemp4=variables[21]
pooltemp=variables[22]
humidity=variables[23]
gust=str(round(1.15077945*int(gust_kts[:-3])))
temp_float=float(temp_str[:-7])
heat_float=float(heatindex_str[:-7])
chill_float=float(chill_str[:-7])
tweet.write('Wx at ''{}''\n''Tmp: ''{}''°F''\n''Hum: ''{}''%''\n''DwPt: ''{}''°F'.format(time[:-1],temp_str[:-7],humidity[:-1],dew[:-7]))
if chill_float < temp_float:
    tweet.write('\n''Windchill: ''{}''°F'.format(chill_str[:-7]))
if heat_float > temp_float:
    tweet.write('\n''Ht ind: ''{}''°F'.format(heatindex_str[:-7]))
tweet.write('\n''Wnd spd: ''{}'' mph (''{}' '°, ''{}'')''\n''Hrly gust: ''{}'' mph''\n''Baro: ''{}'' in Hg (''{}'' in Hg/hr)'.format(windsp[:-1],winddir[:-7],cardinal[:-1],gust[:-2],baro[:-5],barotrend[:-1]))
if float(hourlyrain[:-1])>0:
    tweet.write('\n''Hrly rain: ''{}'' in'.format(hourlyrain[:-2]))
if float(dailyrain[:-1])>0:
    tweet.write('\n''Dly rain: ''{}'' in'.format(dailyrain[:-1]))
if float(solarrad[:-1])>0:
    tweet.write('\n''Slr rad: ''{}'' W/m^2'.format(solarrad[:-1]))
if float(uv[:-1])>0:
    tweet.write('\n''UV ind: ''{}'.format(uv[:-1]))
tweet.write('\n''Soil moist: ''{}'' centibar''\n''Soil temp: ''{}''°F''\n''Pool temp: ''{}''°F'.format(soilmoist[:-1],soiltemp3[:-1],pooltemp[:-1]))
f.close()
tweet.close()
