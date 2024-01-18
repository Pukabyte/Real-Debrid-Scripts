Scripts I use to help maintain symlinks with Real-debrid and organise my library.

# Discard
Created by @west.
- Removes torrents from Real-Debrid that do not have a symlink attached to them.

Change `path/to/debrid/mount` to the parent folder where all your links/symlinks point to.

Change `path/to/symlinks` to the parent media (plex) folder where all your symlinks are.

# Symclean
- rewrites symlinks if some were made using the old volume mapping method (/mount/torrents) to the new volume mapping method (/mnt/remote/realdebrid)
- read the code and make the neccessary changes as per needed for your use case.

# Start/Stop/Restart
- does the action for all the containers that access Zurg in case of failed order of start where zurg/rclone starts after the other containers on a reboot.

# Zurgupdate
- Stops all containers accessing zurg, cd into zurg directory, compose zurg down, prunes unused images, prunes unused volume data, docker compose up -d, waits 60seconds and then starts the stopped containers.
