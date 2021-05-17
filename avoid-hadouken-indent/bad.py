

def example_function(age_value: int) -> str:
    if age_value < 100:
        if age_value < 80:
            if age_value < 60:
                if age_value < 40:
                    if age_value < 20:
                        if age_value < 18:
                            return "Product A"
                        return "Product B"
                    return "Product C"
                return "Product D"
            return "Product E"
        return "Product F"
    return "Unassigned"
