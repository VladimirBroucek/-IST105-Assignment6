import sys
import cgi

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

if len(sys.argv) != 6:
    print("Content-type: text/html\n")
    print("<html><body><h2>Error: Incorrect number of inputs provided.</h2></body></html>")
    sys.exit()

numbers = sys.argv[1:]
if not all(is_numeric(num) for num in numbers):
    print("Content-type: text/html\n")
    print("<html><body><h2>Error: All inputs must be numeric.</h2></body></html>")
    sys.exit()

numbers = [float(num) for num in numbers]

has_negative = any(num < 0 for num in numbers)
negative_msg = "Warning: There are negative numbers in the input." if has_negative else "No negative numbers found."

average = sum(numbers) / len(numbers)
avg_msg = f"Average: {average:.2f} (Greater than 50)" if average > 50 else f"Average: {average:.2f} (Less than or equal to 50)"

positive_count = sum(1 for num in numbers if num > 0)
parity_msg = "Even count of positive numbers" if (positive_count & 1) == 0 else "Odd count of positive numbers"

filtered_list = sorted([num for num in numbers if num > 10])

html_output = f"""
<html>
<head><title>Data Management Results</title></head>
<body>
    <h1>Data Analysis Results</h1>
    <p>{negative_msg}</p>
    <p>{avg_msg}</p>
    <p>{parity_msg}</p>
    <h3>Original List:</h3>
    <p>{numbers}</p>
    <h3>Filtered & Sorted List (Values > 10):</h3>
    <p>{filtered_list}</p>
</body>
</html>
"""

print("Content-type: text/html\n")
print(html_output)