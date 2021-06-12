import numpy as np

n = 64
pos = list(input().upper())
#print(pos)

pos[1] = int(pos[1])
pos[3] = int(pos[3])

d = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
key_list = list(d.keys())
val_list = list(d.values())
#print(d.keys())

x1 = d[pos[0]]+1
y1 = pos[1]+1
x2 = d[pos[2]]+1
y2 = pos[3]+1

'''forming matrix filled with zeros initially.
   12X12 matrix, Surrounding excessive rows and columns by NaN,
   to avoid wrong positioning which arises due to IndexOutOfBounds'''

mat = np.zeros((12,12)) 

mat[0:2] = None
mat[10::] = None
for i in range(2,10):
  mat[i][:2] = None
  mat[i][10::] = None

'''To identify the positions of both the knights in the matrix..
   Specifies the respective indices in the knights' position'''
mat[x1][y1] = (x1-1)*10 + (y1-1)
mat[x2][y2] = (x2-1)*10 + (y2-1)

#print(mat)

'''positioning possible attacks..'''

mat[x1+2][y1-1] += 1
mat[x1+1][y1-2] += 1
mat[x1-2][y1-1] += 1
mat[x1-1][y1-2] += 1
mat[x1+2][y1+1] += 1
mat[x1+1][y1+2] += 1
mat[x1-2][y1+1] += 1
mat[x1-1][y1+2] += 1

mat[x2+2][y2-1] += 1
mat[x2+1][y2-2] += 1
mat[x2-2][y2-1] += 1
mat[x2-1][y2-2] += 1
mat[x2+2][y2+1] += 1
mat[x2+1][y2+2] += 1
mat[x2-2][y2+1] += 1
mat[x2-1][y2+2] += 1

#print(map)

'''prints excluding NaN and aligns as per the view of gameplay..'''
print(np.flip(mat[2:10,2:10].transpose(),0))

'''calculate number of playable moves and no. of unattacked positions'''
moves = np.count_nonzero(mat[2:10,2:10])-2
#print(moves)
print("\nNumber of unattacked positions :",n-moves)

'''Maximum number of knight attacks'''
if np.count_nonzero(mat == 2) > 1:
  print("\n-1")
elif np.count_nonzero(mat == 2) == 0:
  print("\nNone of the positions is maximum attackable")
else:
  result = np.where(mat == 2)
  #print(result)
  print("\nMaximum attacked position : ",end = "")
  print(key_list[(result[0][0]-2)],end = "")
  print(result[1][0]-1)
