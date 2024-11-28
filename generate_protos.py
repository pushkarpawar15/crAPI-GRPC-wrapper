import os
import re
import subprocess

def generate_python_from_protos(proto_directory, output_directory):
    if not os.path.exists(output_directory):
            os.makedirs(output_directory)

    # Collect all .proto files in the proto_directory and its subdirectories
    proto_files = []
    for root, _, files in os.walk(proto_directory):
        for filename in files:
            if filename.endswith('.proto'):
                proto_files.append(os.path.join(root, filename))

    # Run grpc_tools.protoc for each .proto file
    for proto_file in proto_files:
        try:
            subprocess.run([
                'python', '-m', 'grpc_tools.protoc',
                f'-I={proto_directory}',  # Input directory for .proto files
                f'--python_out={output_directory}',  # Output directory for Python files
                f'--grpc_python_out={output_directory}',  # Output directory for gRPC files
                proto_file  # .proto file to process
            ], check=True)
            print(f"Successfully generated code for: {proto_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error generating code for {proto_file}: {e}")

import re

def update_import_statements(file_path):
    """
    Updates the import statement in the generated Python files to use relative imports.

    Args:
        file_path: Path to the generated Python file.
    """
    # Pattern to match the old import statements
    old_import_pattern = r'^import\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+as\s+([a-zA-Z_][a-zA-Z0-9_]*)__pb2$'
    # New import statement format
    new_import_statement = r'from . import \1 as \2__pb2'

    try:
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Process each line and replace matching import statements
        updated_content = [
            re.sub(old_import_pattern, new_import_statement, line)
            for line in content
        ]

        # Check if the content changed
        if updated_content != content:
            with open(file_path, 'w') as file:
                file.writelines(updated_content)
            print(f"Updated imports in: {file_path}")
        else:
            print(f"No changes needed for: {file_path}")
    except Exception as e:
        print(f"Failed to update {file_path}: {e}")


def process_generated_files(output_directory):
    """
    Processes all generated Python files and updates import statements.

    Args:
        output_directory: Directory where the generated Python files are stored.
    """
    for root, _, files in os.walk(output_directory):
        for filename in files:
            if filename.endswith('.py'):
                file_path = os.path.join(root, filename)
                update_import_statements(file_path)

def generate_and_update_imports(proto_directory, output_directory):
    """
    Combines the process of generating Python files and updating import statements.
    """
    generate_python_from_protos(proto_directory, output_directory)
    process_generated_files(output_directory)

# Example usage
proto_directory = './protos'  # Directory containing your .proto files
output_directory = './generated'  # Directory to store the generated Python files

generate_and_update_imports(proto_directory, output_directory)
