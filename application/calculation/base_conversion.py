def base_conversion(base,before_conversion):
    try:
        if base=="binary":
            bin = before_conversion
            oct = format(int(bin,2),"o")
            dec = int(bin,2)
            hex = format(int(bin,2),"x")
        elif base=="octal":
            oct = before_conversion
            bin = format(int(oct,8),"b")
            dec = int(oct,8)
            hex = format(int(oct,8),"x")
        elif base=="decimal":
            dec = before_conversion
            bin = format(int(dec), 'b')
            oct = format(int(dec), 'o')
            hex = format(int(dec), 'x')
        elif base=="hexadecimal":
            hex = before_conversion
            bin = format(int(hex,16),"b")
            oct = format(int(hex,16),"o")
            dec = int(hex,16)
        anser=[bin,oct,dec,hex]
    except:
        anser=["Error","Error","Error","Error"]
    return anser
