// const elementsOrder = [
//   "hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen", "fluorine", "neon",
//   "sodium", "magnesium", "aluminium", "silicon", "phosphorus", "sulfur", "chlorine", "argon", "potassium", "calcium",
//   "scandium", "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel", "copper", "zinc",
//   "gallium", "germanium", "arsenic", "selenium", "bromine", "krypton", "rubidium", "strontium", "yttrium", "zirconium",
//   "niobium", "molybdenum", "technetium", "ruthenium", "rhodium", "palladium", "silver", "cadmium", "indium", "tin",
  // "antimony", "tellurium", "iodine", "xenon", "cesium", "barium", "lanthanum", "cerium", "praseodymium", "neodymium",
  // "promethium", "samarium", "europium", "gadolinium", "terbium", "dysprosium", "holmium", "erbium", "thulium",
  // "ytterbium", "lutetium", "hafnium", "tantalum", "tungsten", "rhenium", "osmium", "iridium", "platinum", "gold",
//   "mercury", "thallium", "lead", "bismuth", "polonium", "astatine", "radon", "francium", "radium", "actinium",
  // "thorium", "protactinium", "uranium", "neptunium", "plutonium", "americium", "curium", "berkelium", "californium",
  // "einsteinium", "fermium", "mendelevium", "nobelium", "lawrencium", "rutherfordium", "dubnium", "seaborgium",
  // "bohrium", "hassium", "meitnerium", "darmstadtium", "roentgenium", "copernicium", "nihonium", "flerovium",
  // "moscovium", "livermorium", "tennessine", "oganesson", "ununennium"
// ];

const elementsOrder = [
  "hydrogen", null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, "helium",
  "lithium", "beryllium", null, null, null, null, null, null, null, null, null, null, "boron", "carbon", "nitrogen", "oxygen", "fluorine", "neon",
  "sodium", "magnesium", null, null, null, null, null, null, null, null, null, null, "aluminium", "silicon", "phosphorus", "sulfur", "chlorine", "argon",
  "potassium", "calcium", "scandium", "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel", "copper", "zinc", "gallium", "germanium", "arsenic", "selenium", "bromine", "krypton",
  "rubidium", "strontium", "yttrium", "zirconium", "niobium", "molybdenum", "technetium", "ruthenium", "rhodium", "palladium", "silver", "cadmium", "indium", "tin", "antimony", "tellurium", "iodine", "xenon",
  "cesium", "barium", "LANTHANIDES", "hafnium", "tantalum", "tungsten", "rhenium", "osmium", "iridium", "platinum", "gold", "mercury", "thallium", "lead", "bismuth", "polonium", "astatine", "radon",
  "francium", "radium", "ACTINIDES", "rutherfordium", "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium", "darmstadtium", "roentgenium", "copernicium", "nihonium", "flerovium", "moscovium", "livermorium", "tennessine", "oganesson",

  "HORIZGAP",

  null, null, null, "lanthanum" ,"cerium", "praseodymium", "neodymium", "promethium", "samarium", "europium", "gadolinium", "terbium", "dysprosium", "holmium", "erbium", "thulium", "ytterbium", "lutetium", null,
  null, null, null, "actinium" ,"thorium", "protactinium", "uranium", "neptunium", "plutonium", "americium", "curium", "berkelium", "californium", "einsteinium", "fermium", "mendelevium", "nobelium", "lawrencium", null,
]

const periodicTableContainer = document.getElementById('periodic-table');
const periodicTableContainer2 = document.getElementById('periodic-table2');
const container = document.getElementById('container');

elementsOrder.forEach((element) => {
  if(element === "LANTHANIDES"){
    const img = document.createElement('img');
    img.src = `elements/custom/lanthanides.svg`;
    img.classList.add('info_element');
    img.alt = element;
    periodicTableContainer.appendChild(img);
    return;
  }

  if(element === "ACTINIDES"){
    const img = document.createElement('img');
    img.src = `elements/custom/actinides.svg`;
    img.classList.add('info_element');
    img.alt = element;
    periodicTableContainer.appendChild(img);
    return;
  }

  if(element === "HORIZGAP"){
    const gap = document.createElement('div');
    gap.classList.add('horizgap');
    container.appendChild(gap)
    return;
  }

  const appendContainer = elementsOrder.indexOf(element) >= 126 ? periodicTableContainer2 : periodicTableContainer;

  if(element === null) {
    const div = document.createElement('div');
    div.classList.add('empty');
    appendContainer.appendChild(div)
  } else {
    const img = document.createElement('img');
    img.src = `elements/${element}.svg`;
    img.classList.add('element');
    img.alt = element;
    appendContainer.appendChild(img);
  }
});
