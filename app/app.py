from flask import Flask, render_template, request
from app.calculator import square_root, factorial, natural_log, power
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    # Initialize input values
    x_sqrt = ""
    x_fact = ""
    x_ln = ""
    x_pow = ""
    y_pow = ""

    if request.method == "POST":
        operation = request.form.get("operation", "")
        print(f"DEBUG: Operation = {operation}")  # Debug line
        
        try:
            if operation == "sqrt":
                x_sqrt = request.form.get("x_sqrt", "")
                print(f"DEBUG: x_sqrt = {x_sqrt}")  # Debug line
                if not x_sqrt.strip():
                    raise ValueError("Please enter a number for square root")
                x_val = float(x_sqrt)
                result = f"√{x_val} = {square_root(x_val)}"

            elif operation == "fact":
                x_fact = request.form.get("x_fact", "")
                print(f"DEBUG: x_fact = {x_fact}")  # Debug line
                if not x_fact.strip():
                    raise ValueError("Please enter an integer for factorial")
                x_val = int(x_fact)
                result = f"{x_val}! = {factorial(x_val)}"

            elif operation == "ln":
                x_ln = request.form.get("x_ln", "")
                print(f"DEBUG: x_ln = {x_ln}")  # Debug line
                if not x_ln.strip():
                    raise ValueError("Please enter a number for logarithm")
                x_val = float(x_ln)
                result = f"ln({x_val}) = {natural_log(x_val)}"

            elif operation == "pow":
                x_pow = request.form.get("x_pow", "")
                y_pow = request.form.get("y_pow", "")
                print(f"DEBUG: x_pow = {x_pow}, y_pow = {y_pow}")  # Debug line
                if not x_pow.strip() or not y_pow.strip():
                    raise ValueError("Please enter both base and exponent")
                x_val = float(x_pow)
                y_val = float(y_pow)
                result = f"{x_val}^{y_val} = {power(x_val, y_val)}"

        except Exception as e:
            result = f"Error: {e}"

    return render_template(
        "index.html",
        result=result,
        x_sqrt=x_sqrt,
        x_fact=x_fact,
        x_ln=x_ln,
        x_pow=x_pow,
        y_pow=y_pow
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    # Testing comments