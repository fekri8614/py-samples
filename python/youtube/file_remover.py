import os

file_path = '/users/fekri86/Downloads/Zoom_cm_fo42anktZ9vvrZo4_m2umeO4Zp9lWtcdrK4QiOc6FE2ii8lXwZuy+D' \
            '@IdP73vMpF9IUWS49_k3ed56a7679723bc3_.exe '

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been removed.")
else:
    print("This file does NOT exist!")
