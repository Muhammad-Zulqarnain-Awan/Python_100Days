row1 = ['[]','[]','[]']
row2 = ['[]','[]','[]']
row3 = ['[]','[]','[]']

map = [row1,row2,row3]

position = input("Enter the position which you want to mark: ")

row = int(position[0])
col = int(position[1])

map[col-1][row-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
