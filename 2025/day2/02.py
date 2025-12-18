import pathlib

data = pathlib.Path("2025/day2/02.txt").read_text(encoding="utf-8")
range_input = data.strip().split(",")
prod_range = result = [tuple(x for x in r.split('-')) for r in range_input]

sum = 0

for begin, end in prod_range:
    begin = int(begin)
    end = int(end)
    for i in range(begin, end+1):
        num = str(i)
        length = len(num)

        if length % 2 != 0: 
            continue
        half = length // 2

        if num[: half] == num[half:]:
            sum += int(num)

# password is the total sum of the error number
print("The password is " + str(sum))
