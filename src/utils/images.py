# notes
'''
This file is used for handling anything image related.
I suggest handling the local file encoding/decoding here as well as fetching any external images.
'''

# package imports
import base64
import os

# image CDNs
image_cdn = 'https://images.dog.ceo/breeds'

# logo information
cwd = os.getcwd()
logo_path = os.path.join(cwd, 'assets', 'logos', 'logo_main.png')
logo_tunel = base64.b64encode(open(logo_path, 'rb').read())
logo_encoded = 'data:image/png;base64,{}'.format(logo_tunel.decode())
