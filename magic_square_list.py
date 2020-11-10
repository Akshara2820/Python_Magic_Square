square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
col=0
row=0
i=0
l=len(square)
while i<l:
    j=0
    diagonal=0
    diagonal1=0
    while j<l:
        col+=square[j][i]
        row+=square[i][j]
        diagonal+=square[j][j]
        diagonal1+=square[len(square)-j-1][j]
        j+=1
    i+=1

print(row)
print(col)
print(diagonal)
print(diagonal1)

if diagonal1==diagonal and row==col:
    print("it is magic squre--")
else:
    print("not magic squre--")











