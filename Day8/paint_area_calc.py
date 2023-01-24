import math

def paint_calc(height, width, cans):
    area = height * width
    num_cans = math.ceil(area / cans)
    print(f"Total number of cans {num_cans}.")


height = float(input("Wall height: "))
width = float(input("Wall width: "))
cans = 5
paint_calc(height=height, width=width, cans=cans)