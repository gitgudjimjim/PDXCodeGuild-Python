# unit_converter.py

meter_dict = {'feet': 3.28, 'inches': 39.37}
in_unit = input("convert from >")
out_unit = input("convert to >")

in_num = int(input("how many units?>"))
out_num = ((in_num / meter_dict[in_unit]) * (meter_dict[out_unit]))

print(f"(in_num) + (in_unit) + 'is' + (out_num) + (out_unit)"")
