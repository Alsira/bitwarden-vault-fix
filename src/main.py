import json
import sys
import os
from output import Output
import duplicates


if __name__ == "__main__":

    # Helps us with output
    out = Output()

    files = sys.argv[1:]

    for file in files:

        try: 
    
            data    = json.loads(file)
            items   = data['items']
            folders = data['folders']


            # Clear up the folders and items
            new_folders = duplicates.remove_duplicate_folders(folders, items)
            new_items   = duplicates.remove_duplicate_items(items)

            # Create the new file
            open('new-' + file, 'w').close()

            # Write out the new data
            json.dump({'encrypted': False, 'folders': new_folders, 'items': new_items}, 'new_' + file) 

        except:

            out.fatal("idk this just died.")
            os.exit(-1)

