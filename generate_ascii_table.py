# ==========================================
#   Pretty ASCII table - A python that creates a pretty ASCII SVG
#   Copyright (c) 2023 Alex Fabre
#   [Released under MIT License. Please refer to license.txt for details]
# ==========================================

# Define the contents of the SVG file as a string
svg_contents = '''
<!-- ASCII TABLE -->
<svg width="780" height="780" xmlns="http://www.w3.org/2000/svg">

    <style>
        .title {
            font: italic bold 70px sans-serif;
            fill: black;
        }

        .subtitle {
            font: italic 13px serif;
            fill: black;
        }

        .column_title {
            font: bold 13px sans-serif;
            fill: #1B6B93;
        }

        .decimal {
            font: bold 12px sans-serif;
            fill: #9370F6;
        }

        .hex {
            font: bold 12px sans-serif;
            fill: #E280E9;
        }

        .char {
            font: italic 12px sans-serif;
            fill: #22A699;
        }

        .bolddecimal {
            font: bold 12px sans-serif;
            fill: #F29727;
        }

        .boldhex {
            font: bold 12px sans-serif;
            fill: #F29727;
        }

        .boldchar {
            font: bold italic 12px sans-serif;
            fill: #F29727;
        }

    </style>

    <text x="5%" y="10%" class="title">ASCII</text>
    <text x="30%" y="10%" class="subtitle">American Standard Code for Information Interchange 1967   -   Robert (Bob) Bemer 1920 - 2004</text>

'''

descriptions = [
    "NULL",
    "START OF HEADING",
    "START OF TEXT",
    "END OF TEXT",
    "END OF TRANSMISSION",
    "ENQUIRY",
    "ACKNOWLEDGE",
    "BELL",
    "BACKSPACE",
    "HORIZONTAL TAB",
    "LINE FEED",
    "VERTICAL TAB",
    "FORM FEED",
    "CARRIAGE RETURN",
    "SHIFT OUT",
    "SHIFT IN",
    "DATA LINK ESCAPE",
    "DEVICE CONTROL 1",
    "DEVICE CONTROL 2",
    "DEVICE CONTROL 3",
    "DEVICE CONTROL 4",
    "NEGATIVE ACK.",
    "SYNCHRONOUS IDLE",
    "END OF TRANS. BLOCK",
    "CANCEL",
    "END OF MEDIUM",
    "SUBSTITUTE",
    "ESCAPE",
    "FILE SEPARATOR",
    "GROUP SEPARATOR",
    "RECORD SEPARATOR",
    "UNIT SEPARATOR",
    "SPACE"
]


for k in range(4):

    svg_contents += f'''
    <!-- Column {k+1} -->
    '''
    if k == 0:
        svg_contents += f'''
    <svg x="5%" y="12%" width="40%" height="80%">
    '''
    else:
        svg_contents += f'''
    <svg x="{45 + 20*(k-1)}%" y="12%" width="20%" height="80%">
    '''
    
    svg_contents += f'''
        <text x="0" y="2%" class="column_title">Dec</text>
        <text x="35" y="2%" class="column_title">Hex</text>
        <text x="70" y="2%" class="column_title">Char</text>
    '''

    # Loop through ASCII values
    t = 0
    for i in range((k*32), 32+(k*32)):
        t+=1
        decimal = str(i)
        hex_value = hex(i)[2:].upper()

        if (i < 128):
            char = chr(i) if (i > 32) and (i < 127) else descriptions[i] if (i<127) else "DEL"

            # Manage SVG special chars
            if char == '&':
                char = '&amp;'
            if char == '<':
                char = '&lt;'
            if char == '>':
                char = '&gt;'

            # Manage char to display in bold
            if decimal in ['97','65','48','13','10']:
                svg_contents += f'''
        <text x="0" y="{3 + 3*t}%" class="bolddecimal">{decimal}</text>
        <text x="35" y="{3 + 3*t}%" class="boldhex">{hex_value}</text>
        <text x="70" y="{3 + 3*t}%" class="boldchar">{char if char.isprintable() else '[Non-printable]'}</text>
    '''
            else:
                svg_contents += f'''
        <text x="0" y="{3 + 3*t}%" class="decimal">{decimal}</text>
        <text x="35" y="{3 + 3*t}%" class="hex">{hex_value}</text>
        <text x="70" y="{3 + 3*t}%" class="char">{char if char.isprintable() else '[Non-printable]'}</text>
    '''
    
    svg_contents += f'''
    </svg>
    '''

svg_contents += f'''
</svg>
'''

# Write the contents to a file
with open('ascii_table.svg', 'w') as svg_file:
    svg_file.write(svg_contents)

print("SVG file 'ascii_table.svg' created successfully.")
