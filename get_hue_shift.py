import sys
import colorsys
from PIL import ImageColor

def main(base, target):
    from_color = base  #"4177BD"
    to_color = target    #"5C2D91"

    if from_color[0] != '#':
        from_color = '#' + from_color
    if to_color[0] != '#':
        to_color = '#' + to_color

    from_rgb = [i/256 for i in ImageColor.getrgb(from_color)]
    to_rgb = [i/256 for i in ImageColor.getrgb(to_color)]

    #print(f"From: {from_color}, To: {to_rgb}")

    from_hsv = colorsys.rgb_to_hsv(from_rgb[0], from_rgb[1], from_rgb[2])
    to_hsv = colorsys.rgb_to_hsv(to_rgb[0], to_rgb[1], to_rgb[2])

    #print(f"From: {from_hsv}, To: {to_hsv}")

    shift_turn = (to_hsv[0] - from_hsv[0])

    #print(f"shift: {shift_value}")
    if __name__ == "__main__":
        print(shift_turn)
        print(shift_turn * 360)
    else:
        return {
            "shift_turn": shift_turn,
            "shift_value": shift_turn * 360
        }

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])


