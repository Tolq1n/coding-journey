#492. Construct the Rectangle
import math
def constructRectangle(area):
        width = int(math.sqrt(area))
        length = int(math.ceil(area / width))

        while width * length != area:
            if width * length < area:
                length += 1
            else:
                width -= 1
        return [length, width]