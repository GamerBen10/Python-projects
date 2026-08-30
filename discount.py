def apply_discount(price, discount):
    # Check if price is an int or float (excluding bool, which is a subclass of int in Python)
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"

    # Example discount calculation logic (assuming discount is a percentage, e.g., 20 for 20%)
    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
    
    if price <= 0:
        return "The price should be greater than 0"

    if (discount < 0) or (discount >100):
        return "The discount should be between 0 and 100" 

    return price * (1 - (discount / 100))



        
print(apply_discount(100, 10))

