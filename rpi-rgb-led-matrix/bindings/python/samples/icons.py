from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
from samplebase import SampleBase

orange = graphics.Color(255,165,0)
medGray = graphics.Color(50,50,50)
gray = graphics.Color(130,130,130)
white = graphics.Color(255,255,255)

options = RGBMatrixOptions()
options.hardware_mapping = 'adafruit-hat'
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.row_address_type = 0
options.multiplexing = 0
options.pwm_bits = 11
options.brightness = 60
options.pwm_lsb_nanoseconds = 50
options.led_rgb_sequence = "RGB"
options.pixel_mapper_config = ""
options.scan_mode = 0

canvas = RGBMatrix(options = options)
'''        
class RunIcon(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunIcon, self).__init__(*args, **kwargs)        
'''
def printSun(sun_y):
    # Circle and Circle Fill
    graphics.DrawCircle(canvas, 15, sun_y+8, 3, orange)
    graphics.DrawCircle(canvas, 15, sun_y+8, 2, orange)
    graphics.DrawCircle(canvas, 15, sun_y+8, 1, orange)
    graphics.DrawLine(canvas, 16, sun_y+7, 14, sun_y+9, orange)
    graphics.DrawLine(canvas, 14, sun_y+7, 16, sun_y+9, orange)                    
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
    return

def printCloud():    
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
               
            
            
            
            
