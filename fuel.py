import re
def main():
    answer = checkfuel()
    # answer = eval(results) * 100
    if answer >= 99:
        print("F")
    elif answer <= 1:
        print("E")
    else:
        print(f"{int(answer)}%")




def checkfuel():
    while True:
        try:
            fuel = input("Fraction: ")
            res, res2 = re.split("/", fuel)
            res = int(res)
            res2 = int(res2)
            answer = res / res2 * 100
            return answer
        except (ValueError, ZeroDivisionError):
            continue



if __name__ == "__main__":
    main()
