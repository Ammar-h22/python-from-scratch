def calculation(num):
    try:
        if num:
            return num + 10
        else:
            return 'Please enter number'
    except TypeError as err:
        return err
