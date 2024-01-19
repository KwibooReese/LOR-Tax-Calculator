regions_tax_rate = {"the_shire":0.2, "mirkwood":0.9, "mordor":0.9}

def calculate_tax(gross_pay, region_string):
    if region_string == "mordor":
        tax = gross_pay * 0.9 + 500
        return tax
    else:
        tax = gross_pay * regions_tax_rate.get(region_string)
        return tax


def report_pay(gross_pay, region_string):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay, region_string)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"

print(f"{regions_tax_rate}\nThis shows the tax for each region")
print("Frodo's Pay:")
print(report_pay(5000.0, "the_shire"))
# Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

print("Bombadil's Pay:")
print(report_pay(4320.0, "mirkwood"))
# Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

print("Mount Doom's Pay:")
print(report_pay(5000.0, "mordor"))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0

