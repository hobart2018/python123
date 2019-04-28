
def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）")
    return nums 

def mean(numbers):
    s = 0.0
    for i in numbers:
        s += i 
    return s / len(numbers)

def dev(numbers, mean):
    sdev = 0.0
    for i in numbers:
        sdev += pow((i - mean), 2)
    return pow(sdev / len(numbers), 0.5)

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        return (numbers[size // 2] + numbers[size // 2 - 1]) / 2
    else:
        return numbers[size // 2]

def main():
    a = getNum()
    m = mean(a)
    print("平均值：{:.20f}，方差：{:.2f}，中位数：{}".format(m, dev(a, m), median(a)))

main()