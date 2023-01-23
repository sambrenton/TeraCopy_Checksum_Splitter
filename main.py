import os

# Define Root directory
src = 'PATH/TO/FILES'

# Iterate over all contents
for root, dirs, files in os.walk(src):
        for file in files:

            # Find checksum files
            if file.endswith('.md5'):

                # Read length of checksum files to check for files that contain more than one checksum
                with open(os.path.join(root, file), 'r') as f: s = f.read()
                if len(s) > 32:

                    # Filter out files from DPX film scans
                    if not '.dpx' in s:
                        if not '01of01' in s:
                            
                            # Open the files with multiple checksums and split them into a list
                            with open (os.path.join(root, file), 'r') as fil: teracopy_file = fil.readlines()

                            # Remove the TeraCopy header
                            teracopy_file = teracopy_file[3:]

                            # Fetch the filename and checksum from the file and write it to it's own md5 file
                            for line in teracopy_file:
                                md5, filename = line.strip().split()
                                with open(os.path.join(root,f'{os.path.basename(filename[1:])}.md5'), 'w') as md5_file: md5_file.write(md5)

                            # Delete the original file (optional)
                            os.remove(os.path.join(root, file))
