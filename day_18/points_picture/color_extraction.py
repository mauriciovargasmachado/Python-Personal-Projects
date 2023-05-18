import colorgram      

rgb_colors = []

colors = colorgram.extract("picture_1.jpg",6)

for color in colors:

    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_colors =(r,g,b)
    rgb_colors.append(new_colors)

#    rgb_colors.append(color.rgb)

print(rgb_colors)
