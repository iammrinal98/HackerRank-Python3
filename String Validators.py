if __name__ == '__main__':
    s = input()
    checks = {
        "alnum": False,
        "alpha": False,
        "digit": False,
        "lower": False,
        "upper": False
    }

…            checks["lower"] = True

        if not checks["upper"] and char.isupper():
            checks["upper"] = True 

    keys = list(checks.keys())
    keys.sort()

    for key in keys:
        print(checks[key])