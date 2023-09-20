import pandas as pd

#print("Enter the dimensions and the cell values (press Enter finish):")

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

input_data = "\n".join(lines)

lines = input_data.strip().split('\n')

rows, cols = map(int, lines[0].split())

data = []
for line in lines[1:]:
    row = list(map(int, line.split()))
    data.append(row)

df = pd.DataFrame(data)

count = 0
for i in range(rows):
    for j in range(cols):
        if df.iloc[i, j] == 1:
            if j + 1 < cols and df.iloc[i, j + 1] == 0:
                count += 1
            if j - 1 >= 0 and df.iloc[i, j - 1] == 0:
                count += 1
            if i + 1 < rows and df.iloc[i + 1, j] == 0:
                count += 1
            if i - 1 >= 0 and df.iloc[i - 1, j] == 0:
                count += 1

print(count)
