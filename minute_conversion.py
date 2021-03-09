def calculate_last_sale_time(last_sales_minutes):
    for minutes in last_sales_minutes:
        minute_conversion=round((minutes/60),2)
        hours= int(minute_conversion)
        minute=round((minute_conversion-hours)*60)
        time=str(hours)+ ":"+str(minute)
        print("Last sale was at: "+ time)

calculate_last_sale_time([320, 478, 1390, 995])