# OS 

## Read binary

```python
def print_hex(file_path):
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(10)
            if not chunk:
                break
            hex_representation = ' '.join(f'{byte:02x}' for byte in chunk)
            print(hex_representation)

# Example usage
print_hex('path_to_your_binary_file')
```