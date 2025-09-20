# Load Dynamic Environmental Variables

Reads variables from a `.env` file and checks if anything is missing. Prints results to `stdout`.

---

## How to Run

1. Create a Python virtual environment:

```bash
python3 -m venv venv
```

2. Activate the virtual environment (Linux/macOS):

```bash
source venv/bin/activate
```

(Windows PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install python-dotenv
```

4. Create a `.env` file in your project and add your variables, for example:

```
API_KEY=your_api_key_here
DB_HOST=localhost
DB_PORT=5432
DB_USER=root
```

---

## `load_env` Function

The `load_env` function takes **2 arguments**:

1. **Path to `.env` file**  
   - Relative paths work fine, e.g., `"../.env"`.

2. **List of variable names**  
   - Example: `["API_KEY", "DB_HOST", "DB_PORT", "DB_USER"]`

It will check each variable and print if any are **missing or empty**.

---

### Example Usage

```python
from load_env_module import load_env  # replace with your actual module

env_vars = load_env("../.env", ["API_KEY", "DB_HOST", "DB_PORT", "DB_USER"])
```

The function will print:

```
API_KEY = 123456
DB_HOST = localhost
DB_PORT is missing or empty!
DB_USER = root
```

---

## Notes

- Make sure `.env` file exists and is readable.  
- Variables already present in `os.environ` will not be overwritten.  
- Works recursively with `.env` files in parent directories.