import json
import svgwrite
import os

groups = {
    "diatomic nonmetal": {
        "background_color": "#e2eeff",
        "text_color": "#0060f0"
    },
    "alkali metal": {
        "background_color": "#d8f8ff",
        "text_color": "#00758c"
    },
    "alkaline earth metal": {
        "background_color": "#ffe7e7",
        "text_color": "#d60024"
    },
    "transition metal": {
        "background_color": "#f3e8fd",
        "text_color": "#6232ec"
    },
    "post-transition metal": {
        "background_color": "#d6f9e8",
        "text_color": "#227754"
    },
    "metalloid": {
        "background_color": "#fef7e0",
        "text_color": "#945700"
    },
    "noble gas": {
        "background_color": "#ffe7eb",
        "text_color": "#cd1d5e"
    },
    "lanthanide": {
        "background_color": "#dff3ff",
        "text_color": "#003355"
    },
    "actinide": {
        "background_color": "#ffe6d4",
        "text_color": "#c73200"
    },
    "unknown": {
        "background_color": "#e7e7ea",
        "text_color": "#3f374f"
    },
    "unknown, probably metalloid": {
        "background_color": "#fef7e0",
        "text_color": "#945700"
    },
    "unknown, probably post-transition metal": {
        "background_color": "#d6f9e8",
        "text_color": "#227754"
    },
    "unknown, probably transition metal": {
        "background_color": "#f3e8fd",
        "text_color": "#6232ec"
    },
    "unknown, predicted to be noble gas": {
        "background_color": "#ffe7eb",
        "text_color": "#cd1d5e"
    },
    "unknown, but predicted to be an alkali metal": {
        "background_color": "#d8f8ff",
        "text_color": "#00758c"
    },
    "polyatomic nonmetal": {
        "background_color": "#e2eeff",
        "text_color": "#0060f0"
    }
}

def create_periodic_table_item(index, atomic_mass, symbol, name, text_color, background_color, output_file):
    atomic_mass_str = f"{atomic_mass:.6f}"[:6]
    
    # canvas
    dwg = svgwrite.Drawing(output_file, size=("70px", "70px"), profile="tiny")
    
    # rect
    dwg.add(dwg.rect(insert=(0, 0), size=("70px", "70px"), fill=background_color))
    # border
    dwg.add(dwg.rect(insert=(1, 1), size=("68px", "68px"), fill="none", stroke=text_color, stroke_width=0.4))
    # index number
    dwg.add(dwg.text(
        str(index),
        insert=(5, 15),
        fill=text_color,
        font_size="12px",
        font_family="Arial"
    ))
    
    # atomic mass
    dwg.add(dwg.text(
        atomic_mass_str,
        insert=(65, 15),
        fill=text_color,
        font_size="12px",
        font_family="Arial",
        text_anchor="end"
    ))
    
    # symbol
    dwg.add(dwg.text(
        symbol,
        insert=("35px", "40px"),
        fill=text_color,
        font_size="24px",
        font_family="Arial",
        font_weight="bold",
        text_anchor="middle"
    ))
    
    # element name
    dwg.add(dwg.text(
        name,
        insert=("35px", "60px"),
        fill=text_color,
        font_size="10px",
        font_family="Arial",
        text_anchor="middle"
    ))
    
    dwg.save()
    print(f"Generated {output_file}")

#now we will load the periodic table elements in order
# then generate svgs...
with open("table.json", "r") as f:
    data = json.load(f)

# will output to elements folder
output_dir = "elements"
os.makedirs(output_dir, exist_ok=True)

for element_key in data["order"]:
    element = data[element_key]
    category = element["category"]
    styles = groups.get(category, groups["unknown"]) # if no category found.
    
    create_periodic_table_item(
        index=element["number"],
        atomic_mass=element["atomic_mass"],
        symbol=element["symbol"],
        name=element["name"],
        text_color=styles["text_color"],
        background_color=styles["background_color"],
        output_file=os.path.join(output_dir, f"{element_key}.svg")
    )