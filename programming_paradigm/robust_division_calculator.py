def safe_divide(numerator, denominator):
    try:
        float(numerator)
        float(denominator)
        result = numerator / denominator
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        return result
