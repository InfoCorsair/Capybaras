def convert_to_teaspoons(quantity, unit):
    teaspoons_per_unit = {
        "teaspoon": 1,
	"tsp": 1,
        "tablespoon": 3,
	"tbs": 3,
	"tablespoons": 3,
        "fluid ounce": 6,
	"fl oz": 6,
        "cup": 48,
	"cups": 48,
        "pint": 96,
	"pt": 96,
	"pints" : 96,
        "quart": 192,
	"qt": 192,
        "gallon": 768,
	"gal": 768
    }
    return quantity * teaspoons_per_unit.get(unit, 1)

def convert_from_teaspoons(quantity):
    units = ["gallon", "quart", "cup", "tablespoon", "teaspoon"] #pint fluid ounce
    result = {}
    remaining_teaspoons = quantity
    for unit in units:
        teaspoons_per_unit = {
            "teaspoon": 1,
            "tablespoon": 3,
            "fluid ounce": 6,
            "cup": 48,
            "pint": 96,
            "quart": 192,
            "gallon": 768
        }
        unit_quantity = remaining_teaspoons // teaspoons_per_unit[unit]
        if unit_quantity:
            result[unit] = unit_quantity
            remaining_teaspoons %= teaspoons_per_unit[unit]
    return result

def optimize_measurements(quantity, unit):
    if unit == "teaspoon":
        return convert_from_teaspoons(quantity), "cup"
    elif unit == "tsp":
        return convert_from_teaspoons(quantity), "cup"
    else:
        teaspoons = convert_to_teaspoons(quantity, unit)
        return teaspoons, "teaspoon"

def format_output(quantity, unit):
    if unit == "teaspoon":
        if isinstance(quantity, int):
            return f"{quantity} teaspoons"
        else:
            return f"{quantity:.1f} teaspoons"  # Treat float as remaining teaspoons directly
    else:
        output_str = ""
        for unit, value in quantity.items():
            if value:
                output_str += f"{value} {unit}" if value == 1 else f"{value} {unit}s"
                output_str += ", "
        return output_str[:-2]  # Remove trailing comma and space

def main():
    while True:
        try:
            input_str = input("Enter quantity and unit (e.g., '3 cup'): ")
            if input_str.lower() == "quit":
                break
            quantity, unit = input_str.split(maxsplit=1)
            quantity = float(quantity)  # Allow floating-point quantities
            optimized_quantity, optimized_unit = optimize_measurements(quantity, unit)
            output_str = format_output(optimized_quantity, optimized_unit)
            print(output_str)
        except ValueError as e:
            print("Error:", e)
            continue

if __name__ == "__main__":
    main()

