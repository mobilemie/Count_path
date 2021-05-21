from collections import Counter
import matplotlib.pyplot as plt
import os
plt.rcdefaults()


def Count(log):
    import re
    num = []
    name = []
    rx = r'(api/[a-z.]\S+)'
    with open(log) as f:
        log = f.read()
        iplist = re.findall(rx, log)
        # print(iplist)
        ipcount = Counter(iplist)
        for k, v in ipcount.items():
            if "utils" in k:
                continue
                # print("yes")
            num.append(v)
            name.append(k)
            print(k, v)
    # print(num)
    # print(name)
    return(num, name)


def graph(y, x):

    left = []
    performance = []
    tick_label = []

    bar = 1
    for i in x:
        left.append(bar)
        bar += 1

    # heights of bars
    for i in y:
        performance.append(i)

    # labels for bars
    for i in x:
        tick_label.append(i)

    # plotting a bar chart
    plt.barh(left, performance, tick_label=tick_label,
             align="center", alpha=0.5)

    # naming the x-axis
    plt.xlabel('Access-Path')
    # naming the y-axis
    plt.ylabel('')
    # plot title
    plt.title('Chart')

    # function to show the plot
    plt.show()


def main():
    file_name = str(input("กรอกชื่อไฟล Log = "))
    my_path = os.path.abspath(file_name)
    # print(my_path)
    (y, x) = Count(my_path)
    graph(y, x)


if __name__ == "__main__":
    main()
