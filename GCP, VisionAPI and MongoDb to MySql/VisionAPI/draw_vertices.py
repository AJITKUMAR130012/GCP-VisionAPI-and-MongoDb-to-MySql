#import io
import io
#import Image,ImageDraw,ImageFont
from PIL import Image, ImageDraw, ImageFont
#function for draw vertices
def drawVertices(image_source, vertices, display_text=''):
    # variable for read the object
    pillow_img = Image.open(io.BytesIO(image_source))
    #calling the draw function and storing it into draw variable
    draw = ImageDraw.Draw(pillow_img)
    #iterating over the vertices
    for i in range(len(vertices) - 1):
        #calling to draw line function
        draw.line(((vertices[i].x, vertices[i].y), (vertices[i + 1].x, vertices[i + 1].y)),
                #drawing green line
                fill='green',
                #width of line is 8
                width=8
        )
    # calling to draw line function
    draw.line(((vertices[len(vertices) - 1].x, vertices[len(vertices) - 1].y),
              #making a co-ordinate
               (vertices[0].x, vertices[0].y)),
               #filling the green line
               fill='green',
               #width 8
               width=8
    )
     #making a object front 
    font = ImageFont.truetype('arial.ttf', 16)
    #calling to draw nect function
    draw.text((vertices[0].x + 10, vertices[0].y),
              font=font, text=display_text, 
              fill=(255, 255, 255))
    #calling to show function
    pillow_img.show()