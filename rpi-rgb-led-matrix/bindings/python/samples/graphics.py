#!/usr/bin/env python

from samplebase import SampleBase
from rgbmatrix import graphics
import time
from requests import get
import json
import bme280_v2 as bme
import BlynkLib
from subprocess import call

# Icon Colors
orange = graphics.Color(255,165,0)
medGray = graphics.Color(50,50,50)
gray = graphics.Color(130,130,130)
darkGray = graphics.Color(25,25,25)
white = graphics.Color(255,255,255)
yellow = graphics.Color(255,255,0)
purple = graphics.Color(110,115,240)
cyan = graphics.Color(0,255,255)

# Logical Operators for Blynk
reading = 'temp'
source = False

# Tuples for Icon Display Logic
cloud = ('Thunderstorms','Clouds','Atmosphere','Rain','Drizzle')
rain = ('Rain','Drizzle')

# Unique Blynk App Authentification Key
BLYNK_AUTH = '67632eab3412433bbcc2bb51d3799914'

time.sleep(10)

blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Blynk Virtual Button Handlers
@blynk.VIRTUAL_WRITE(0)
def v0_write_handler(value):    
    global source
    if value:
        source = not source
    
@blynk.VIRTUAL_WRITE(1)
def v1_write_handler(value):    
    global reading    
    value = int(value[0])
    if value == 0:
        reading = 'temp'
    elif value == 1:
        reading = 'humid'
    elif value == 2:
        reading = 'pressure'

@blynk.VIRTUAL_WRITE(2)
def v2_write_handler(value): 
    call("systemctl poweroff -i",shell=True)

class RunMatrix(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunMatrix, self).__init__(*args, **kwargs)     
      
    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()        
        font1 = graphics.Font()
        font1.LoadFont("../../../fonts/5x8.bdf")
        font2 = graphics.Font()
        font2.LoadFont("../../../fonts/4x6.bdf")
        canvas = self.matrix
        canvas.brightness = 60
        
        # Y Position of Text
        pos_y = 30        
        # Use to Move Sun/Snow Icon Up/Down
        sun_y = 2;
        snow_y = 2;

        # Waco ID: id=4739526        
        url = 'https://api.openweathermap.org/data/2.5/weather?id=4739526&units=imperial&APPID=hidden'
                     
        while True:            
            blynk.run()            
            offscreen_canvas.Clear()            
                
            # Get Weather Data from OpenWeatherMap
            response = get(url)
            # Converts Json Data to Python Dictionary
            weather = json.loads(response.text)
            
            # Get Readings From Sensor
            temp,pressure,humidity = bme.readBME280All()
            temp = int(temp*9/5+32)
            pressure = int(pressure)
            humidity = int(humidity)
            correction = 0           
                
            if reading == 'temp': # if temp is selected by blynk button
                if source == False: # if we wamt outside (internet) readings
                    temp = int((weather["main"]["temp"])) # Temp data from internet               
                my_text = str(temp) + u"\u00b0" + "F" # make usable by drawText()
                unit_len = 9
                digit_len = len(str(temp))
            elif reading == 'humid':
                if source == False:
                    humidity = int((weather["main"]["humidity"]))
                my_text = str(humidity) + "%"
                unit_len = 4
                digit_len = len(str(humidity))
                textColor = cyan
            elif reading == 'pressure':
                if source == False:
                    pressure = int((weather["main"]["pressure"]))
                    correction = 1
                my_text = str(round(pressure*.0009869,1)) + "atm"
                unit_len = 14
                digit_len = len(str(pressure))-correction              
                textColor = orange
            
            # For Centering Temp on Matrix           
            reading_len = digit_len*5 + unit_len           
            pos_x = (32-reading_len)/2
            
            # Temp Color
            if reading == 'temp':
                if 83<=temp<100:
                  val=255-((temp-83)*255)/17
                  textColor = graphics.Color(255,val,0)
                elif 66<=temp<83:
                  val=((temp-66)*255)/17
                  textColor = graphics.Color(val,255,0)
                elif 49<=temp<66:
                  val=255-((temp-49)*255)/17              
                  textColor = graphics.Color(0,255,val)
                elif 32<temp<49:
                  val=((temp-32)*255)/17
                  textColor = graphics.Color(0,val,255)
                elif temp>=100: 
                   textColor = graphics.Color(255,0,0)              
                elif temp<=32:  
                  textColor = graphics.Color(0,0,255)             
            
            # Print Data to Matrix
            graphics.DrawText(offscreen_canvas, font1, pos_x, pos_y, textColor, my_text)            
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            if weather["weather"][0]["main"] in cloud:  #ideally there would be functions for these
                ## Cloud Icon
                # Outer Edge
                graphics.DrawLine(canvas,7,13,23,13,medGray)
                graphics.DrawLine(canvas,6,12,6,11,medGray)
                graphics.DrawLine(canvas,7,10,7,9,medGray)
                graphics.DrawLine(canvas,8,8,9,8,medGray)
                graphics.DrawLine(canvas,10,7,10,6,medGray)
                graphics.DrawLine(canvas,11,5,11,5,medGray)
                graphics.DrawLine(canvas,12,4,14,4,medGray)
                graphics.DrawLine(canvas,15,5,16,6,medGray)
                graphics.DrawLine(canvas,17,5,19,5,medGray)
                graphics.DrawLine(canvas,20,6,21,7,medGray)
                graphics.DrawLine(canvas,21,8,21,9,medGray)
                graphics.DrawLine(canvas,22,9,24,11,medGray)
                graphics.DrawLine(canvas,24,12,24,12,medGray)
                graphics.DrawLine(canvas,15,7,16,7,medGray)
                # Highlights
                graphics.DrawLine(canvas,7,11,7,11,white)
                graphics.DrawLine(canvas,8,9,9,9,white)
                graphics.DrawLine(canvas,10,8,10,8,white)
                graphics.DrawLine(canvas,10,10,10,10,white)
                graphics.DrawLine(canvas,11,6,11,6,white)
                graphics.DrawLine(canvas,12,5,14,5,white)
                graphics.DrawLine(canvas,17,6,19,6,white)
                graphics.DrawLine(canvas,20,7,20,7,white)
                graphics.DrawLine(canvas,21,10,22,10,white)
                graphics.DrawLine(canvas,23,11,23,11,white)
                # Fill
                graphics.DrawLine(canvas,12,6,12,12,gray)
                graphics.DrawLine(canvas,13,6,13,12,gray)
                graphics.DrawLine(canvas,14,6,14,12,gray)
                graphics.DrawLine(canvas,11,7,11,12,gray)
                graphics.DrawLine(canvas,10,11,10,12,gray)
                graphics.DrawLine(canvas,9,10,9,12,gray)
                graphics.DrawLine(canvas,8,10,8,12,gray)
                graphics.DrawLine(canvas,7,12,7,12,gray)
                graphics.DrawLine(canvas,15,8,15,12,gray)
                graphics.DrawLine(canvas,16,8,16,12,gray)
                graphics.DrawLine(canvas,17,7,17,12,gray)
                graphics.DrawLine(canvas,18,7,18,12,gray)
                graphics.DrawLine(canvas,19,7,19,12,gray)
                graphics.DrawLine(canvas,20,8,20,12,gray)
                graphics.DrawLine(canvas,21,11,21,12,gray)
                graphics.DrawLine(canvas,22,11,22,12,gray)
                graphics.DrawLine(canvas,10,9,10,9,gray)
                graphics.DrawLine(canvas,15,6,15,6,gray)
                graphics.DrawLine(canvas,23,12,23,12,gray)
               
                if weather["weather"][0]["main"] in rain:
                    # Rain Drops
                    graphics.DrawLine(canvas,9,16,9,17,purple)
                    graphics.DrawLine(canvas,15,16,15,17,purple)
                    graphics.DrawLine(canvas,21,16,21,17,purple)
                    graphics.DrawLine(canvas,12,15,12,16,purple)
                    graphics.DrawLine(canvas,18,15,18,16,purple)
                
                elif weather["weather"][0]["main"] in 'Thunderstorm':
                    # Lightning Bolt
                    graphics.DrawLine(canvas,13,13,15,13,yellow)
                    graphics.DrawLine(canvas,14,14,11,17,yellow)
                    graphics.DrawLine(canvas,12,18,13,19,yellow)
                    graphics.DrawLine(canvas,12,20,12,20,yellow)
                    
                elif weather["weather"][0]["description"] in 'few clouds':
                    # Small Sun
                    graphics.DrawLine(canvas,19,4,21,6,orange)
                    graphics.DrawLine(canvas,20,4,21,5,orange)
                    graphics.DrawLine(canvas,20,3,22,5,orange)
                    graphics.DrawLine(canvas,21,3,22,4,orange)
                
            elif weather["weather"][0]["main"] in 'Clear':
                if weather["weather"][0]["icon"][2] == 'd': #if daytime
                    radius = 3
                    color = orange
                    # Diagonal Lines
                    graphics.DrawLine(canvas, 18, sun_y+11, 20, sun_y+13, orange)
                    graphics.DrawLine(canvas, 12, sun_y+11, 10, sun_y+13, orange)
                    graphics.DrawLine(canvas, 12, sun_y+5, 10, sun_y+3, orange)
                    graphics.DrawLine(canvas, 18, sun_y+5, 20, sun_y+3, orange)
                    # Straight Lines
                    graphics.DrawLine(canvas, 20, sun_y+8, 21, sun_y+8, orange)
                    graphics.DrawLine(canvas, 10, sun_y+8, 9, sun_y+8, orange)
                    graphics.DrawLine(canvas, 15, sun_y+13, 15, sun_y+14, orange)
                    graphics.DrawLine(canvas, 15, sun_y+3, 15, sun_y+2, orange)
                else: #if night
                    color = darkGray #Moon Color
                    radius = 5 #Moon Size
                    graphics.DrawCircle(canvas, 15, sun_y+8, radius-3, color)
                    graphics.DrawCircle(canvas, 15, sun_y+8, radius-4, color)
                    graphics.DrawLine(canvas, 13, sun_y+4, 11, sun_y+6, color)
                    graphics.DrawLine(canvas, 17, sun_y+4, 19, sun_y+6, color)
                    graphics.DrawLine(canvas, 13, sun_y+12, 11, sun_y+10, color)
                    graphics.DrawLine(canvas, 17, sun_y+12, 19, sun_y+10, color) 
                ## Sun/Moon Icon
                # Circle and Circle Fill
                graphics.DrawCircle(canvas, 15, sun_y+8, radius, color)
                graphics.DrawCircle(canvas, 15, sun_y+8, radius-1, color)
                graphics.DrawCircle(canvas, 15, sun_y+8, radius-2, color)
                graphics.DrawLine(canvas, 16, sun_y+7, 14, sun_y+9, color)
                graphics.DrawLine(canvas, 14, sun_y+7, 16, sun_y+9, color)
                                
            elif weather["weather"][0]["main"] in 'Snow':
                #Snow Flake
                graphics.DrawLine(canvas,16,snow_y+4,16,snow_y+12,cyan)
                graphics.DrawLine(canvas,12,snow_y+8,20,snow_y+8,cyan)
                graphics.DrawLine(canvas,13,snow_y+5,19,snow_y+11,cyan)
                graphics.DrawLine(canvas,13,snow_y+11,19,snow_y+5,cyan)
                graphics.DrawLine(canvas,13,snow_y+4,12,snow_y+5,cyan)
                graphics.DrawLine(canvas,19,snow_y+4,20,snow_y+5,cyan)
                graphics.DrawLine(canvas,12,snow_y+11,13,snow_y+12,cyan)
                graphics.DrawLine(canvas,19,snow_y+12,20,snow_y+11,cyan)

                graphics.DrawLine(canvas,15,snow_y+3,15,snow_y+3,cyan)
                graphics.DrawLine(canvas,17,snow_y+3,17,snow_y+3,cyan)
                
                
            # Update Every 2 Seconds (interval arbitrary)
            time.sleep(2)
            
# Main function
if __name__ == "__main__":
    time.sleep(10)
    run_matrix = RunMatrix()
    if (not run_matrix.process()):
        run_matrix.print_help()

        
