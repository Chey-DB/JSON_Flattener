# JSON Flattener

## Overview

The JSON Flattener script extracts specific key paths from a nested JSON structure and outputs a flattened version of the JSON. It is designed to handle complex nested JSON objects, including lists, and ensures only specified key-value pairs are included in the output.

---

## Features

- **Modular Design**: Each component of the script is isolated for readability, reusability, and maintainability.
- **Dot-Path Navigation**: Supports dot-separated key paths to access nested keys.
- **List Handling**: Traverses lists to find the desired key-value pairs.
- **Error Handling**: Gracefully handles invalid paths or malformed JSON files.
- **Customizable Key Extraction**: Allows you to specify the exact keys you want to extract.

---

## Requirements

- Python 3.7 or higher

---

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python installed on your system.
3. Install any required dependencies (none are required for this script as it uses standard libraries).

---

## Usage

### Input

1. Prepare a **JSON file** (e.g., `products.json`) with the nested structure you want to process.
2. Create a **list of keys** (dot-separated paths) that you want to extract from the JSON.

### Running the Script

To run the script, call the `flatten` function with the following arguments:

- **`json_file_path`**: Path to the input JSON file (e.g., `products.json`).
- **`keys`**: List of dot-separated keys to extract.
- **`output_file_path`**: Path to the output JSON file (e.g., `flattened_output.json`).

#### Example

```python
keys = [
    "attributes.primaryAttributes.skuName",
    "attributes.feedSkuBaseAttributeSet.skuCode",
    "attributes.primaryAttributes.productName",
    "attributes.feedProductBaseAttributeSet.productCode",
    "attributes.primaryAttributes.supplier",
    "attributes.productDescriptiveAttributes.Brand",
    "attributes.primaryAttributes.ean",
    "attributes.FormattedDimensions.BoxDimensions.height",
    "attributes.FormattedDimensions.BoxDimensions.length",
    "attributes.FormattedDimensions.BoxDimensions.quantity",
    "attributes.FormattedDimensions.BoxDimensions.weight",
    "attributes.FormattedDimensions.BoxDimensions.width",
    "attributes.FormattedDimensions.NumberOfBoxes",
    "hierarchicalCategories.lvl0",
    "hierarchicalCategories.lvl1",
    "hierarchicalCategories.lvl2",
    "hierarchicalCategories.lvl3"
]

```

flatten("products.json", keys, "flattened_output.json")

### Output

The script generates a flattened JSON file (e.g., `flattened_output.json`) containing only the specified key-value pairs.

---

## Testing

The script includes a comprehensive suite of unit tests to ensure its core functionality works as expected. The tests validate key features such as extracting values from nested structures, handling lists, and saving/loading JSON files.

### Running the Tests

1. Save the test script as `test_json_flattener.py` in the same directory as your main script.
2. Run the tests using the following command:
   ```bash
   python -m unittest test_json_flattener.py

```

### Test Cases

The test suite includes the following test cases:
- **Key Path Traversal**: Verifies that `get_value_by_path` can correctly navigate nested JSON structures and handle lists.
- **Key Extraction**: Tests that `extract_keys_from_json` correctly extracts the specified keys.
- **JSON File Operations**:
  - **`load_json`**: Ensures JSON files are loaded correctly.
  - **`save_json`**: Verifies that flattened data is saved to a file in the expected format.

### Expected Output

If all tests pass, you’ll see output like this:
```bash
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK

```
