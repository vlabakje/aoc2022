def snafu_to_base_10(snafu):
    b10 = 0
    for i, s in enumerate(snafu[::-1]):
        match s:
            case "=":
                b10 -= 5 ** i * 2
            case "-":
                b10 -= 5 ** i
            case _:
                b10 += int(s) * 5 ** i
        #print(f"{snafu=}, {b10=} {i=} {s=}")
    #print(f"{snafu=}, {b10=}")
    return b10

def int_to_snafu(n):
    snafu = ""
    b5 = ""
    while n > 0:
        n, d = divmod(n, 5)
        b5 = str(d) + b5
    carry = 0
    for i, x in enumerate(b5[::-1]):
        carry, x = 0, int(x) + carry
        if x == 3:
            carry += 1
            append = "="
        elif x == 4:
            carry += 1
            append = "-"
        elif x == 5:
            carry += 1
            append = "0"
        else:
            append = str(x)
        snafu = append + snafu
    if carry:
        snafu = str(carry) + snafu
    return snafu

def main(filename):
    total = 0
    for line in open(filename):
        total += snafu_to_base_10(line.strip())
    print(total, int_to_snafu(total))


main("example")
main("input")
