def remove_duplicate_folders(folders: dict, items: dict) -> dict:
    
    # The folders that are unique are added to this dict
    fixed_folders = dict()
    folder_counter = 0

    # This holds the copy folders IDs
    copy_folders_ids = list()


    # Search for unique folders
    for key in folders.keys():

        name   = folders[key]['name']
        id     = folders[key]['id']

        # Make sure we are not looking at a copy folder
        if id not in copy_folders_ids:
            
            # Search for the copy folders
            for copy_key in folders.keys():

                # Copy folder found
                if folders[copy_key]['name'] == name:
                    
                    copy_id = folders[copy_key]['id']
                    copy_folders_ids.append(copy_id)

                    # Clear up the items that are in the copy folders
                    for item_key in items.keys():

                        # Fix ID
                        if items[item_key]['folderId'] == copy_id:
                            items[item_key]['folderId'] = id

            # Since we found all the copy folders now, we append the original
            fixed_folders.update({folder_counter: {'name': name, 'id': id}})   
            folder_counter += 1


# Use this first, this will also replace all items with eqivalant
def remove_duplicate_items(items: dict) -> dict:

    new_items = dict()

    for key in items.keys():

        username = items[key]['login']['username']
        password = items[key]['login']['password']
        uris = items[key]['login']['uris']

        already_exist = True
        for new_key in new_items.keys():
            
            new_user = new_items[new_key]['login']['username']
            new_pass = new_items[new_key]['login']['password']
            new_uris = new_items[new_key]['login']['uris']

            # Check username and password
            if new_user == username and new_pass == password:

                # TODO : THIS 😁
                # Now check for overlapping uris
                for uri_key in 



        