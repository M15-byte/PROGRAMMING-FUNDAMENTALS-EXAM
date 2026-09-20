# Question 4
# Stock record manager: reads records from a text file, converts them into
# dictionaries, queries them and writes them back.
#   (a) parse_record() / load_stock() - safe loading
#   (b) find_low_stock()              - query
#   (c) save_records()                - safe saving
#   (d) except Exception as e vs bare except


def parse_record(line):
    """Convert one CSV line into a product dictionary (raises
    ValueError if invalid)."""
    fields = line.strip().split(",")
    if len(fields) != 5:
        raise ValueError("expected 5 fields")
    return {
        "product_code": fields[0],
        "name": fields[1],
        "category": fields[2],
        "quantity": int(fields[3]),        # ValueError if not a whole number
        "unit_price": float(fields[4]),    # ValueError if not numeric
    }


def load_stock(filename):
    """Read every record in the file and return them as a list of
    dictionaries."""
    products = []
    try:
        with open(filename, "r") as file:
            for number, line in enumerate(file, start=1):
                if line.strip() == "":
                    continue                             # ignore blank lines
                try:
                    products.append(parse_record(line))
                except ValueError as error:
                    print(f"Skipping line {number}: {error}")
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
    except Exception as error:
        print(f"Unexpected error while reading {filename}: {error}")
    return products


def find_low_stock(products, threshold):
    """Print every product whose quantity is below the threshold."""
    found = False
    for product in products:
        if product["quantity"] < threshold:
            found = True
            print(f"{product['product_code']} {product['name']:<12}"
                  f"{product['category']:<12}Qty: {product['quantity']:>4}"
                  f" Price: UGX {product['unit_price']:,.0f}")
    if not found:
        print(f"No product is below {threshold} units.")


def save_records(filename, products):
    """Write the product dictionaries back to the file in CSV format."""
    try:
        with open(filename, "w") as file:      # closed even if writing fails
            for product in products:
                price = product["unit_price"]
                price_text = str(int(price)) if price == int(price) else str(price)
                file.write(f"{product['product_code']},{product['name']},"
                           f"{product['category']},{product['quantity']},{price_text}\n")
    except Exception as error:
        print(f"Error: the records could not be saved: {error}")


# Question 4 (d): the same file operation with a bare except and with a
# named handler.
def read_all_bad(filename):
    """Poor practice: a bare except swallows every failure without a trace."""
    try:
        with open(filename, "r") as file:
            data = file.readlines()
    except:
        data = []
    return data


def read_all_good(filename):
    """Better: the same failures are caught, and the reason is reported."""
    try:
        with open(filename, "r") as file:
            data = file.readlines()
    except Exception as e:
        print("Could not read", filename, ":", e)
        data = []
    return data


if __name__ == '__main__':
    records = load_stock("stock.txt")
    print("Records loaded:", len(records))
    find_low_stock(records, 20)
    save_records("stock.txt", records)
