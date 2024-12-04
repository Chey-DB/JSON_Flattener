import json
from typing import List, Any


def load_json(file_path: str) -> Any:
    """
    Load JSON data from a file.
    
    :param file_path: Path to the JSON file.
    :return: Parsed JSON data.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data: dict, file_path: str) -> None:
    """
    Save data to a JSON file.
    
    :param data: The dictionary to save.
    :param file_path: Path to save the JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_value_by_path(data: Any, key_path: str) -> Any:
    """
    Traverse a nested JSON structure to extract the value corresponding to a dot-separated key path.
    If a list is encountered, iterate through it to find the key at the correct index.
    
    :param data: The JSON data (nested structure).
    :param key_path: Dot-separated key path (e.g., "key1.key2").
    :return: The value corresponding to the key path, or None if not found.
    """
    keys = key_path.split('.')
    for key in keys:
        if isinstance(data, list):
            # Iterate through the list to find the dictionary that contains the desired key
            found = False
            for item in data:
                if isinstance(item, dict) and key in item:
                    data = item[key]
                    found = True
                    break
            if not found:
                return None  # Key not found in the list
        elif isinstance(data, dict):
            # Navigate the dictionary
            data = data.get(key)
        else:
            return None  # Key path is invalid
    return data


def extract_keys_from_json(data: dict, keys: List[str]) -> dict:
    """
    Extract specific keys from a nested JSON structure.
    
    :param data: The JSON data (nested structure).
    :param keys: A list of JSON key paths to extract.
    :return: A flattened dictionary with the specified keys and their values.
    """
    flattened_data = {}
    for key in keys:
        value = get_value_by_path(data, key)
        if value is not None:
            flattened_data[key] = value
    return flattened_data


def flatten(json_file_path: str, keys: List[str], output_file_path: str) -> bool:
    """
    Extract specific key paths from a nested JSON file and save the flattened result to an output file.
    
    :param json_file_path: Path to the nested JSON input file.
    :param keys: A list of JSON key paths to extract (e.g., ["key1.key2", "key3.key4"]).
    :param output_file_path: Path to save the flattened JSON.
    :return: True if the flatten operation completed successfully, False otherwise.
    """
    try:
        # Load the JSON data from the file
        data = load_json(json_file_path)

        # Extract the specified keys
        flattened_data = extract_keys_from_json(data, keys)

        # Save the flattened result to the output file
        save_json(flattened_data, output_file_path)

        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False


# List of keys to extract
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

# Run the function
flatten("products.json", keys, "flattened_output.json")
