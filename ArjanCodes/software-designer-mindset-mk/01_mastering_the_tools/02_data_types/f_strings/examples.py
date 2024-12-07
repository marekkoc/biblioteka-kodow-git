# Define variables for demonstration
product_name = "Laptop"
quantity = 3
unit_price_cents = 79999  # Unit price in cents

# Using f-strings to create a formatted string
summary = f"Product: {product_name}, Quantity: {quantity}, Total Price: ${(quantity * unit_price_cents) / 100:.2f}"
print(summary)

# Example of using f-strings for dynamic expressions
tax_rate = 0.07  # 7% tax rate
total_cost_cents = quantity * unit_price_cents
total_cost_with_tax = total_cost_cents * (1 + tax_rate)

# Formatting the total cost with tax using f-strings
formatted_total_cost = f"Total Cost (with tax): ${total_cost_with_tax / 100:.2f}"
print(formatted_total_cost)

# Comparison without using personal details
feature = "battery life"
hours = 10

# Demonstrating use of f-strings for including variable values and expressions
feature_description = f"The {product_name} has a {feature} of up to {hours} hours."
print(feature_description)

# Type of f_strings are still strings
print(type(feature_description))
