import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g = np.array(g_coeffs, dtype=float)
    h = np.array(h_coeffs, dtype=float)

    g_x = np.polyval(g, x)
    h_x = np.polyval(h, x)

    g_prime = np.polyder(g)
    h_prime = np.polyder(h)

    g_x_prime = np.polyval(g_prime, x)
    h_x_prime = np.polyval(h_prime, x)

    return (g_x_prime * h_x - g_x * h_x_prime) / (h_x ** 2)