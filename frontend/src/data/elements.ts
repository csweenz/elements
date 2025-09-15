export type Category =
  | "alkali"
  | "alkaline-earth"
  | "transition"
  | "post-transition"
  | "metalloid"
  | "nonmetal"
  | "halogen"
  | "noble"
  | "lanthanide"
  | "actinide"
  | "unknown";

export interface ElementData {
  number: number;
  symbol: string;
  name: string;
  x: number;   // column (1..18)
  y: number;   // row
  category: Category;
}

export const categories: readonly { key: Category; label: string }[] = [
  { key: "alkali",          label: "Alkali metal" },
  { key: "alkaline-earth",  label: "Alkaline earth" },
  { key: "transition",      label: "Transition metal" },
  { key: "post-transition", label: "Post-transition" },
  { key: "metalloid",       label: "Metalloid" },
  { key: "nonmetal",        label: "Reactive nonmetal" },
  { key: "halogen",         label: "Halogen" },
  { key: "noble",           label: "Noble gas" },
  { key: "lanthanide",      label: "Lanthanide" },
  { key: "actinide",        label: "Actinide" },
  { key: "unknown",         label: "Unknown/undetermined" },
];

export const categoryClass = (c: Category) => `pt-cat-${c}`;

// --- Main body (periods 1–7) ---
export const ELEMENTS: readonly ElementData[] = [
  // Period 1
  { number: 1,  symbol: "H",  name: "Hydrogen",      x: 1,  y: 1, category: "nonmetal" },
  { number: 2,  symbol: "He", name: "Helium",        x: 18, y: 1, category: "noble" },

  // Period 2
  { number: 3,  symbol: "Li", name: "Lithium",       x: 1,  y: 2, category: "alkali" },
  { number: 4,  symbol: "Be", name: "Beryllium",     x: 2,  y: 2, category: "alkaline-earth" },
  { number: 5,  symbol: "B",  name: "Boron",         x: 13, y: 2, category: "metalloid" },
  { number: 6,  symbol: "C",  name: "Carbon",        x: 14, y: 2, category: "nonmetal" },
  { number: 7,  symbol: "N",  name: "Nitrogen",      x: 15, y: 2, category: "nonmetal" },
  { number: 8,  symbol: "O",  name: "Oxygen",        x: 16, y: 2, category: "nonmetal" },
  { number: 9,  symbol: "F",  name: "Fluorine",      x: 17, y: 2, category: "halogen" },
  { number: 10, symbol: "Ne", name: "Neon",          x: 18, y: 2, category: "noble" },

  // Period 3
  { number: 11, symbol: "Na", name: "Sodium",        x: 1,  y: 3, category: "alkali" },
  { number: 12, symbol: "Mg", name: "Magnesium",     x: 2,  y: 3, category: "alkaline-earth" },
  { number: 13, symbol: "Al", name: "Aluminum",      x: 13, y: 3, category: "post-transition" },
  { number: 14, symbol: "Si", name: "Silicon",       x: 14, y: 3, category: "metalloid" },
  { number: 15, symbol: "P",  name: "Phosphorus",    x: 15, y: 3, category: "nonmetal" },
  { number: 16, symbol: "S",  name: "Sulfur",        x: 16, y: 3, category: "nonmetal" },
  { number: 17, symbol: "Cl", name: "Chlorine",      x: 17, y: 3, category: "halogen" },
  { number: 18, symbol: "Ar", name: "Argon",         x: 18, y: 3, category: "noble" },

  // Period 4
  { number: 19, symbol: "K",  name: "Potassium",     x: 1,  y: 4, category: "alkali" },
  { number: 20, symbol: "Ca", name: "Calcium",       x: 2,  y: 4, category: "alkaline-earth" },
  { number: 21, symbol: "Sc", name: "Scandium",      x: 3,  y: 4, category: "transition" },
  { number: 22, symbol: "Ti", name: "Titanium",      x: 4,  y: 4, category: "transition" },
  { number: 23, symbol: "V",  name: "Vanadium",      x: 5,  y: 4, category: "transition" },
  { number: 24, symbol: "Cr", name: "Chromium",      x: 6,  y: 4, category: "transition" },
  { number: 25, symbol: "Mn", name: "Manganese",     x: 7,  y: 4, category: "transition" },
  { number: 26, symbol: "Fe", name: "Iron",          x: 8,  y: 4, category: "transition" },
  { number: 27, symbol: "Co", name: "Cobalt",        x: 9,  y: 4, category: "transition" },
  { number: 28, symbol: "Ni", name: "Nickel",        x: 10, y: 4, category: "transition" },
  { number: 29, symbol: "Cu", name: "Copper",        x: 11, y: 4, category: "transition" },
  { number: 30, symbol: "Zn", name: "Zinc",          x: 12, y: 4, category: "transition" },
  { number: 31, symbol: "Ga", name: "Gallium",       x: 13, y: 4, category: "post-transition" },
  { number: 32, symbol: "Ge", name: "Germanium",     x: 14, y: 4, category: "metalloid" },
  { number: 33, symbol: "As", name: "Arsenic",       x: 15, y: 4, category: "metalloid" },
  { number: 34, symbol: "Se", name: "Selenium",      x: 16, y: 4, category: "nonmetal" },
  { number: 35, symbol: "Br", name: "Bromine",       x: 17, y: 4, category: "halogen" },
  { number: 36, symbol: "Kr", name: "Krypton",       x: 18, y: 4, category: "noble" },

  // Period 5
  { number: 37, symbol: "Rb", name: "Rubidium",      x: 1,  y: 5, category: "alkali" },
  { number: 38, symbol: "Sr", name: "Strontium",     x: 2,  y: 5, category: "alkaline-earth" },
  { number: 39, symbol: "Y",  name: "Yttrium",       x: 3,  y: 5, category: "transition" },
  { number: 40, symbol: "Zr", name: "Zirconium",     x: 4,  y: 5, category: "transition" },
  { number: 41, symbol: "Nb", name: "Niobium",       x: 5,  y: 5, category: "transition" },
  { number: 42, symbol: "Mo", name: "Molybdenum",    x: 6,  y: 5, category: "transition" },
  { number: 43, symbol: "Tc", name: "Technetium",    x: 7,  y: 5, category: "transition" },
  { number: 44, symbol: "Ru", name: "Ruthenium",     x: 8,  y: 5, category: "transition" },
  { number: 45, symbol: "Rh", name: "Rhodium",       x: 9,  y: 5, category: "transition" },
  { number: 46, symbol: "Pd", name: "Palladium",     x: 10, y: 5, category: "transition" },
  { number: 47, symbol: "Ag", name: "Silver",        x: 11, y: 5, category: "transition" },
  { number: 48, symbol: "Cd", name: "Cadmium",       x: 12, y: 5, category: "transition" },
  { number: 49, symbol: "In", name: "Indium",        x: 13, y: 5, category: "post-transition" },
  { number: 50, symbol: "Sn", name: "Tin",           x: 14, y: 5, category: "post-transition" },
  { number: 51, symbol: "Sb", name: "Antimony",      x: 15, y: 5, category: "metalloid" },
  { number: 52, symbol: "Te", name: "Tellurium",     x: 16, y: 5, category: "metalloid" },
  { number: 53, symbol: "I",  name: "Iodine",        x: 17, y: 5, category: "halogen" },
  { number: 54, symbol: "Xe", name: "Xenon",         x: 18, y: 5, category: "noble" },

  // Period 6
  { number: 55, symbol: "Cs", name: "Cesium",        x: 1,  y: 6, category: "alkali" },
  { number: 56, symbol: "Ba", name: "Barium",        x: 2,  y: 6, category: "alkaline-earth" },
  // (x=3 reserved for f-block)
  { number: 72, symbol: "Hf", name: "Hafnium",       x: 4,  y: 6, category: "transition" },
  { number: 73, symbol: "Ta", name: "Tantalum",      x: 5,  y: 6, category: "transition" },
  { number: 74, symbol: "W",  name: "Tungsten",      x: 6,  y: 6, category: "transition" },
  { number: 75, symbol: "Re", name: "Rhenium",       x: 7,  y: 6, category: "transition" },
  { number: 76, symbol: "Os", name: "Osmium",        x: 8,  y: 6, category: "transition" },
  { number: 77, symbol: "Ir", name: "Iridium",       x: 9,  y: 6, category: "transition" },
  { number: 78, symbol: "Pt", name: "Platinum",      x: 10, y: 6, category: "transition" },
  { number: 79, symbol: "Au", name: "Gold",          x: 11, y: 6, category: "transition" },
  { number: 80, symbol: "Hg", name: "Mercury",       x: 12, y: 6, category: "transition" },
  { number: 81, symbol: "Tl", name: "Thallium",      x: 13, y: 6, category: "post-transition" },
  { number: 82, symbol: "Pb", name: "Lead",          x: 14, y: 6, category: "post-transition" },
  { number: 83, symbol: "Bi", name: "Bismuth",       x: 15, y: 6, category: "post-transition" },
  { number: 84, symbol: "Po", name: "Polonium",      x: 16, y: 6, category: "post-transition" },
  { number: 85, symbol: "At", name: "Astatine",      x: 17, y: 6, category: "halogen" },
  { number: 86, symbol: "Rn", name: "Radon",         x: 18, y: 6, category: "noble" },

  // Period 7
  { number: 87, symbol: "Fr", name: "Francium",      x: 1,  y: 7, category: "alkali" },
  { number: 88, symbol: "Ra", name: "Radium",        x: 2,  y: 7, category: "alkaline-earth" },
  // (x=3 reserved for f-block)
  { number: 104, symbol: "Rf", name: "Rutherfordium", x: 4,  y: 7, category: "transition" },
  { number: 105, symbol: "Db", name: "Dubnium",       x: 5,  y: 7, category: "transition" },
  { number: 106, symbol: "Sg", name: "Seaborgium",    x: 6,  y: 7, category: "transition" },
  { number: 107, symbol: "Bh", name: "Bohrium",       x: 7,  y: 7, category: "transition" },
  { number: 108, symbol: "Hs", name: "Hassium",       x: 8,  y: 7, category: "transition" },
  { number: 109, symbol: "Mt", name: "Meitnerium",    x: 9,  y: 7, category: "transition" },
  { number: 110, symbol: "Ds", name: "Darmstadtium",  x: 10, y: 7, category: "transition" },
  { number: 111, symbol: "Rg", name: "Roentgenium",   x: 11, y: 7, category: "transition" },
  { number: 112, symbol: "Cn", name: "Copernicium",   x: 12, y: 7, category: "transition" },
  { number: 113, symbol: "Nh", name: "Nihonium",      x: 13, y: 7, category: "unknown" },
  { number: 114, symbol: "Fl", name: "Flerovium",     x: 14, y: 7, category: "unknown" },
  { number: 115, symbol: "Mc", name: "Moscovium",     x: 15, y: 7, category: "unknown" },
  { number: 116, symbol: "Lv", name: "Livermorium",   x: 16, y: 7, category: "unknown" },
  { number: 117, symbol: "Ts", name: "Tennessine",    x: 17, y: 7, category: "halogen" },
  { number: 118, symbol: "Og", name: "Oganesson",     x: 18, y: 7, category: "noble" },

  // Lanthanides (display row 8)
  { number: 57, symbol: "La", name: "Lanthanum",     x: 3,  y: 8, category: "lanthanide" },
  { number: 58, symbol: "Ce", name: "Cerium",        x: 4,  y: 8, category: "lanthanide" },
  { number: 59, symbol: "Pr", name: "Praseodymium",  x: 5,  y: 8, category: "lanthanide" },
  { number: 60, symbol: "Nd", name: "Neodymium",     x: 6,  y: 8, category: "lanthanide" },
  { number: 61, symbol: "Pm", name: "Promethium",    x: 7,  y: 8, category: "lanthanide" },
  { number: 62, symbol: "Sm", name: "Samarium",      x: 8,  y: 8, category: "lanthanide" },
  { number: 63, symbol: "Eu", name: "Europium",      x: 9,  y: 8, category: "lanthanide" },
  { number: 64, symbol: "Gd", name: "Gadolinium",    x: 10, y: 8, category: "lanthanide" },
  { number: 65, symbol: "Tb", name: "Terbium",       x: 11, y: 8, category: "lanthanide" },
  { number: 66, symbol: "Dy", name: "Dysprosium",    x: 12, y: 8, category: "lanthanide" },
  { number: 67, symbol: "Ho", name: "Holmium",       x: 13, y: 8, category: "lanthanide" },
  { number: 68, symbol: "Er", name: "Erbium",        x: 14, y: 8, category: "lanthanide" },
  { number: 69, symbol: "Tm", name: "Thulium",       x: 15, y: 8, category: "lanthanide" },
  { number: 70, symbol: "Yb", name: "Ytterbium",     x: 16, y: 8, category: "lanthanide" },
  { number: 71, symbol: "Lu", name: "Lutetium",      x: 17, y: 8, category: "lanthanide" },

  // Actinides (display row 9)
  { number: 89,  symbol: "Ac", name: "Actinium",      x: 3,  y: 9, category: "actinide" },
  { number: 90,  symbol: "Th", name: "Thorium",       x: 4,  y: 9, category: "actinide" },
  { number: 91,  symbol: "Pa", name: "Protactinium",  x: 5,  y: 9, category: "actinide" },
  { number: 92,  symbol: "U",  name: "Uranium",       x: 6,  y: 9, category: "actinide" },
  { number: 93,  symbol: "Np", name: "Neptunium",     x: 7,  y: 9, category: "actinide" },
  { number: 94,  symbol: "Pu", name: "Plutonium",     x: 8,  y: 9, category: "actinide" },
  { number: 95,  symbol: "Am", name: "Americium",     x: 9,  y: 9, category: "actinide" },
  { number: 96,  symbol: "Cm", name: "Curium",        x: 10, y: 9, category: "actinide" },
  { number: 97,  symbol: "Bk", name: "Berkelium",     x: 11, y: 9, category: "actinide" },
  { number: 98,  symbol: "Cf", name: "Californium",   x: 12, y: 9, category: "actinide" },
  { number: 99,  symbol: "Es", name: "Einsteinium",   x: 13, y: 9, category: "actinide" },
  { number: 100, symbol: "Fm", name: "Fermium",       x: 14, y: 9, category: "actinide" },
  { number: 101, symbol: "Md", name: "Mendelevium",   x: 15, y: 9, category: "actinide" },
  { number: 102, symbol: "No", name: "Nobelium",      x: 16, y: 9, category: "actinide" },
  { number: 103, symbol: "Lr", name: "Lawrencium",    x: 17, y: 9, category: "actinide" },
];
