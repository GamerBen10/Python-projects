"""
myList = [1, 2, 3, 4, 5]

print(myList)
myList

revList=myList
revList.reverse()
print(revList)
print(7 % 10)


import sys

a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(a)} bytes")
print(f"Tuple size: {sys.getsizeof(b)} bytes")


# List size: 52 bytes
# Tuple size: 40 bytes

def total(*args):
  
  result = 0
  for arg in args:
    result += arg
  return result

print(total(1, 2, 3, 4, 5))
print(total(1, 2, 3, 4, 5, 6, 7))
print(total(1, 2, 3))

# Basic multiple assignment
a, b, c = [10, 20, 30]

# Extended unpacking with the * (splat) operator
first, *middle, last = [1, 2, 3, 4, 5]

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5def show_items(category, *items):
  print("Category: " + category)
  for item in items:
    print(item)

show_items("Electronics", "Laptop", "Smartphone", "Tablet")

#**kwargs is a dictionary
def display_info(**kwargs):
  #kwargs.items() returns the key:valie pairs
  for key, value in kwargs.items():
    print(key, ":", value)

display_info(name="Alice", age=30, city="New York")
 
# Ternqry operator
age = 20
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)


def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

@uppercase
def greet():
    return "Welcome!"

# Using the decorated function
print(greet())


score = int(input("Enter score: "))
status = "Pass" if score >= 50 else "Fail"
print(status)

"""

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>In-Browser Python Runner</title>
  
  <script src="https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js"></script>

  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      background-color: #f4f6f8;
      color: #333;
    }

    h1 {
      margin-bottom: 8px;
    }

    .status {
      font-size: 0.9rem;
      margin-bottom: 20px;
      color: #666;
    }

    textarea {
      width: 100%;
      height: 180px;
      box-sizing: border-box;
      font-family: 'Courier New', Courier, monospace;
      font-size: 14px;
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 6px;
      background: #fff;
      resize: vertical;
    }

    button {
      margin-top: 10px;
      padding: 10px 20px;
      font-size: 15px;
      font-weight: 600;
      color: #fff;
      background-color: #0070f3;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background-color 0.2s;
    }

    button:hover:not(:disabled) {
      background-color: #0051a2;
    }

    button:disabled {
      background-color: #aaa;
      cursor: not-allowed;
    }

    .output-container {
      margin-top: 20px;
    }

    pre {
      background-color: #1e1e1e;
      color: #00ff66;
      padding: 15px;
      border-radius: 6px;
      min-height: 80px;
      overflow-x: auto;
      font-family: 'Courier New', Courier, monospace;
      font-size: 14px;
      white-space: pre-wrap;
    }
  </style>
</head>
<body>

  <h1>Python Web Runner</h1>
  <div id="status" class="status">Loading Python runtime... please wait.</div>

  <textarea id="code" spellcheck="false"># Write Python code here
name = "World"
print(f"Hello, {name}!")

# Simple math / loop test
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("Squares:", squares)</textarea>

  <button id="runBtn" disabled onclick="runPython()">Run Code</button>

  <div class="output-container">
    <h3>Output:</h3>
    <pre id="output">Output will appear here...</pre>
  </div>

  <script>
    let pyodide;
    const statusEl = document.getElementById("status");
    const outputEl = document.getElementById("output");
    const runBtn = document.getElementById("runBtn");
    const codeEl = document.getElementById("code");

    // Initialize Pyodide
    async function initPyodide() {
      try {
        pyodide = await loadPyodide();
        statusEl.textContent = "Python runtime loaded and ready.";
        statusEl.style.color = "green";
        runBtn.disabled = false;
      } catch (err) {
        statusEl.textContent = "Failed to load Python runtime.";
        statusEl.style.color = "red";
        console.error(err);
      }
    }

    // Execute the user's Python code
    async function runPython() {
      if (!pyodide) return;
      
      outputEl.textContent = "Running...";
      
      const userCode = codeEl.value;
      
      // Redirect standard Python stdout/stderr to JS string
      const wrappedCode = `
import sys
import io

sys.stdout = io.StringIO()
sys.stderr = io.StringIO()

try:
${userCode.split('\n').map(line => '    ' + line).join('\n')}
except Exception as e:
    import traceback
    traceback.print_exc()

sys.stdout.getvalue() + sys.stderr.getvalue()
      `;

      try {
        const result = await pyodide.runPythonAsync(wrappedCode);
        outputEl.textContent = result || "[Execution finished with no output]";
      } catch (err) {
        outputEl.textContent = "Error executing code:\n" + err;
      }
    }

    // Start loading runtime on page load
    initPyodide();
  </script>
</body>
</html>





