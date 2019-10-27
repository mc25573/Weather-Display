#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
   
            
class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        #self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()        
        font = graphics.Font()
        font.LoadFont("../../../fonts/5x8.bdf")
        textColor = graphics.Color(70, 150, 25)        
        pos_y = 31
        temp = 31   
        my_text = str(temp) + u"\u00b0" +"F" #u"\u2109" for F. u"\u2103" for C
        pos_x = len(my_text)+2
        canvas = self.matrix
        orange = graphics.Color(255,165,0)

        while True:
            offscreen_canvas.Clear()
            length = graphics.DrawText(offscreen_canvas, font, pos_x, pos_y, textColor, my_text)    
            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            #circle and circle fill
            graphics.DrawCircle(canvas, 15, 8, 3, orange)
            graphics.DrawCircle(canvas, 15, 8, 2, orange)
            graphics.DrawCircle(canvas, 15, 8, 1, orange)
            graphics.DrawLine(canvas, 16, 7, 14, 9, orange)
            graphics.DrawLine(canvas, 14, 7, 16, 9, orange)
                    
            #diagonal lines
            graphics.DrawLine(canvas, 18, 11, 20, 13, orange)
            graphics.DrawLine(canvas, 12, 11, 10, 13, orange)
            graphics.DrawLine(canvas, 12, 5, 10, 3, orange)
            graphics.DrawLine(canvas, 18, 5, 20, 3, orange)

            #straight lines
            graphics.DrawLine(canvas, 20, 8, 21, 8, orange)
            graphics.DrawLine(canvas, 10, 8, 9, 8, orange)
            graphics.DrawLine(canvas, 15, 13, 15, 14, orange)
            graphics.DrawLine(canvas, 15, 3, 15, 2, orange)

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()


        
