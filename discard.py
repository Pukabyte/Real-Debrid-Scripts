import os
import argparse
import shutil
import traceback

def find_non_linked_files(src_folder, dst_folder, dry_run=False, no_confirm=False):
    # Get the list of links in the dst_folder
    dst_links = set()
    for root, dirs, files in os.walk(dst_folder):
        for file in files:
            dst_path = os.path.join(root, file)
            if os.path.islink(dst_path):
                dst_links.add(os.path.realpath(dst_path))

    # Check for non-linked files in the src_folder
    for root, dirs, files in os.walk(src_folder):
        # Get the subdirectory of the current root, relative to the src_folder
        subdirectory = os.path.relpath(root, src_folder)
        subdirectory_any_linked_files = False
        for file in files:
            src_file = os.path.realpath(os.path.join(root, file))

            if src_file in dst_links:
                subdirectory_any_linked_files = True
            # else:
                # print(f"File {src_file} is not used!")
        
        if any(files) and not subdirectory_any_linked_files:
            print(f"Directory {subdirectory} is not used!")
            if not dry_run:
                response = input("Do you want to delete this directory? (y/n): ") if not no_confirm else 'y'
                if response.lower() == 'y':
                    try:
                        for root, dirs, files in os.walk(root):
                            for f in files:
                               os.unlink(os.path.join(root, f))
                            for d in dirs:
                                shutil.rmtree(os.path.join(root, d))
                        print(f"Directory {subdirectory} deleted!")
                    except Exception as e:
                        print(f"Directory {subdirectory} error during deletion!")
                        print(traceback.format_exc())
                else:
                    print(f"Directory {subdirectory} not deleted!")

if __name__ == '__main__':
    src_folder = "/mnt/remote/realdebrid/torrents" #location of your debrid mount
    dst_folder = "/mnt/plex" #location of your media directory where imported symlinks live
    parser = argparse.ArgumentParser(description='Find and delete non-linked file directories.')
    parser.add_argument('--dry-run', action='store_true', help='print non-linked file directories without deleting')
    parser.add_argument('--no-confirm', action='store_true', help='delete non-linked file directories without confirmation')
    args = parser.parse_args()
    find_non_linked_files(src_folder, dst_folder, dry_run=args.dry_run, no_confirm=args.no_confirm)
