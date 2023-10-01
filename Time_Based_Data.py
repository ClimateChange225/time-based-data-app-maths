import pandas as pd
import numpy as np
# https://colab.research.google.com/drive/1dwNLK0ZC3z8KwMehqneRTeEnoYxyDopK#scrollTo=JdB4G8uaIvlu

def main():
    df = input_t_and_y()
    df = adding_x(df)
    df = adding_xsqr(df)
    df = adding_xy(df)
    df = adding_a_plus_bx(df)

    print(df)


def input_t_and_y():
    while True:
        try:
            n = input("Enter number of t values: ")
            n = int(n)
            break
        except:
            print("Please enter a valid number!")
            continue

    t_values = []
    y_values = []

    for _ in range(1, n+1):
        while True:
            try:
                t = input(f"Enter t value (no. {_}): ")
                t = int(t)
                break
            except:
                print("Please enter a valid t value!")
                continue

        t_values.append(t)

        while True:
            try:
                y = input(f"Enter y value (no. {_}): ")
                y = int(y)
                break
            except:
                print("Please enter a valid y value!")
                continue

        y_values.append(y)

    d1 = {"t":t_values, "y":y_values}

    return(pd.DataFrame(d1))


def adding_x(df):
    if len(df)%2 == 0:
        n = (df.iat[int(((len(df)/2)-1)), 0] + df.iat[int(((len(df)/2))), 0])/2
        df.loc[:, "x"] = df.t-n

    else:
        n = df.iat[int((len(df))/2), 0]
        df.loc[:, "x"] = df.t-n

    return df


def adding_xsqr(df):
    df.loc[:, "x^2"] = df.x*df.x
    return df


def adding_xy(df):
    df.loc[:, "xy"] = df.x*df.y
    return df


def adding_a_plus_bx(df):
    a = (df.y).sum()/len(df)
    b = (df.xy).sum()/df["x^2"].sum()
    df.loc[:, "a+bx"] = a + (df.loc[:, ["x"]])*b
    return df

if __name__=="__main__":
    main()
