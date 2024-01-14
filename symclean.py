import os

def update_symlinks(directory, dry_run=False):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.islink(filepath):
                link_target = os.readlink(filepath)
                if link_target.startswith('/mount/torrents'): # Specify the old symlink directory here
                    updated_target = link_target.replace('/mount/torrents', '/mnt/remote/realdebrid/torrents', 1) # Specify what you want to rewrite it to here
                    if not dry_run:
                        os.unlink(filepath)
                        os.symlink(updated_target, filepath)
                        print(f"Updated symlink: {link_target} -> {updated_target}")
                    else:
                        print(f"Would update symlink: {link_target} -> {updated_target}")
                        return

# Specify the directory you want to search for symbolic links
target_directory = '/mnt/plex'

# Set dry_run to True to see what changes would be made without actually updating the symlinks
update_symlinks(target_directory, dry_run=True) # Change to False to run it without dry_run
