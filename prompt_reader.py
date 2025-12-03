import os

def extract_prompts(base_dir):
    tree_structure = []

    # Walk through the directory structure
    for root, dirs, files in os.walk(base_dir):
        # Only process directories named 'prompts'
        if os.path.basename(root) == 'prompts':
            # Get the parent directories for grouping
            checklist_type = os.path.basename(os.path.dirname(root))
            checklist_category = os.path.basename(os.path.dirname(os.path.dirname(root)))

            # Create header if not already present
            header = f"- {checklist_category}\n    - {checklist_type}"
            if header not in tree_structure:
                tree_structure.append(header)

            # Read each .txt file in the prompts directory
            for file in sorted(files):
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        prompt_text = f.read().strip()
                    entry = f"        - {file.replace('.txt', '')}\n            {prompt_text}"
                    tree_structure.append(entry)

    return tree_structure

# Define the base directory
base_directory = 'soda_mmqc/data/checklist'

# Extract the prompts and build the tree
tree_output = extract_prompts(base_directory)

# Save the result to a text file
with open('prompt_checks_tree.txt', 'w', encoding='utf-8') as out_file:
    out_file.write('\n'.join(tree_output))