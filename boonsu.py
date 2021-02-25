X = int(input())
stage, key_X = 1, 1
while key_X + stage <= X:
    key_X += stage
    stage += 1
step = X - key_X
x, y = step + 1, stage - step
if stage % 2 == 0:
    print('{}/{}'.format(x, y))
else:
    print('{}/{}'.format(y, x))