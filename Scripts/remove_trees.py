from lxml import etree
import os
import sys

def remove_trees_from_save(file_path, output_path):
    # Parse the XML save file
    tree = etree.parse(file_path)
    root = tree.getroot()

    # Tree definitions to remove
    tree_definitions = ["Plant_TreePine", "Plant_TreeBirch", "Plant_TreeMaple"]

    # Find and remove trees
    for thing in root.findall(".//thing"):
        def_tag = thing.find('def')
        if def_tag is not None and def_tag.text in tree_definitions:
            parent = thing.getparent()  # Get the parent of the tree element
            if parent is not None:
                parent.remove(thing)  # Remove the tree element

    # Save the modified XML to a new file
    tree.write(output_path, pretty_print=True, xml_declaration=True, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Drag and drop your RimWorld save file onto this script.")
        sys.exit(1)

    # Get the input file from the command line argument (drag and drop)
    input_file = sys.argv[1]

    # Ensure the file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    # Generate output file name by appending '_modified' to the original name
    file_dir, file_name = os.path.split(input_file)
    name, ext = os.path.splitext(file_name)
    output_file = os.path.join(file_dir, f"{name}_modified{ext}")

    # Call the function to remove trees and save to output
    remove_trees_from_save(input_file, output_file)
    
    print(f"Trees (Pine, Birch, Maple) removed and saved to {output_file}.")
