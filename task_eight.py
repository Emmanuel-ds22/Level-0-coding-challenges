def hours_and_minutes(num):
    minutes = num % 60
    hours = num // 60
    if minutes == 1:
        if hours == 1:
            print(f"{hours} hour , {minutes}minute")
        else:
            print(f"{hours} hours , {minutes}minute")
    else:
        if hours == 1:
            print(f"{hours} hour , {minutes}minutes")
        else:
            print(f"{hours} hours , {minutes}minutes")
