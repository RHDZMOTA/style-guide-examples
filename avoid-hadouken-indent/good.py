

def example_function(age_value: int) -> str:
    # TODO: Use datastore to declare the product age restriction.
    if age_value < 18:
        return "Product A"
    if age_value < 20:
        return "Product B"
    if age_value < 40:
        return "Product C"
    if age_value < 60:
        return "Product D"
    if age_value < 80:
        return "Product E"
    if age_value < 100:
        return "Product F"
    return "Unassigned"
