from django.db import migrations

ELEMENTS = [
  {
    "AtomicNumber": 1,
    "Symbol": "H",
    "Name": "Hydrogen"
  },
  {
    "AtomicNumber": 2,
    "Symbol": "He",
    "Name": "Helium"
  },
  {
    "AtomicNumber": 3,
    "Symbol": "Li",
    "Name": "Lithium"
  },
  {
    "AtomicNumber": 4,
    "Symbol": "Be",
    "Name": "Beryllium"
  },
  {
    "AtomicNumber": 5,
    "Symbol": "B",
    "Name": "Boron"
  },
  {
    "AtomicNumber": 6,
    "Symbol": "C",
    "Name": "Carbon"
  },
  {
    "AtomicNumber": 7,
    "Symbol": "N",
    "Name": "Nitrogen"
  },
  {
    "AtomicNumber": 8,
    "Symbol": "O",
    "Name": "Oxygen"
  },
  {
    "AtomicNumber": 9,
    "Symbol": "F",
    "Name": "Fluorine"
  },
  {
    "AtomicNumber": 10,
    "Symbol": "Ne",
    "Name": "Neon"
  },
  {
    "AtomicNumber": 11,
    "Symbol": "Na",
    "Name": "Sodium"
  },
  {
    "AtomicNumber": 12,
    "Symbol": "Mg",
    "Name": "Magnesium"
  },
  {
    "AtomicNumber": 13,
    "Symbol": "Al",
    "Name": "Aluminum"
  },
  {
    "AtomicNumber": 14,
    "Symbol": "Si",
    "Name": "Silicon"
  },
  {
    "AtomicNumber": 15,
    "Symbol": "P",
    "Name": "Phosphorus"
  },
  {
    "AtomicNumber": 16,
    "Symbol": "S",
    "Name": "Sulfur"
  },
  {
    "AtomicNumber": 17,
    "Symbol": "Cl",
    "Name": "Chlorine"
  },
  {
    "AtomicNumber": 18,
    "Symbol": "Ar",
    "Name": "Argon"
  },
  {
    "AtomicNumber": 19,
    "Symbol": "K",
    "Name": "Potassium"
  },
  {
    "AtomicNumber": 20,
    "Symbol": "Ca",
    "Name": "Calcium"
  },
  {
    "AtomicNumber": 21,
    "Symbol": "Sc",
    "Name": "Scandium"
  },
  {
    "AtomicNumber": 22,
    "Symbol": "Ti",
    "Name": "Titanium"
  },
  {
    "AtomicNumber": 23,
    "Symbol": "V",
    "Name": "Vanadium"
  },
  {
    "AtomicNumber": 24,
    "Symbol": "Cr",
    "Name": "Chromium"
  },
  {
    "AtomicNumber": 25,
    "Symbol": "Mn",
    "Name": "Manganese"
  },
  {
    "AtomicNumber": 26,
    "Symbol": "Fe",
    "Name": "Iron"
  },
  {
    "AtomicNumber": 27,
    "Symbol": "Co",
    "Name": "Cobalt"
  },
  {
    "AtomicNumber": 28,
    "Symbol": "Ni",
    "Name": "Nickel"
  },
  {
    "AtomicNumber": 29,
    "Symbol": "Cu",
    "Name": "Copper"
  },
  {
    "AtomicNumber": 30,
    "Symbol": "Zn",
    "Name": "Zinc"
  },
  {
    "AtomicNumber": 31,
    "Symbol": "Ga",
    "Name": "Gallium"
  },
  {
    "AtomicNumber": 32,
    "Symbol": "Ge",
    "Name": "Germanium"
  },
  {
    "AtomicNumber": 33,
    "Symbol": "As",
    "Name": "Arsenic"
  },
  {
    "AtomicNumber": 34,
    "Symbol": "Se",
    "Name": "Selenium"
  },
  {
    "AtomicNumber": 35,
    "Symbol": "Br",
    "Name": "Bromine"
  },
  {
    "AtomicNumber": 36,
    "Symbol": "Kr",
    "Name": "Krypton"
  },
  {
    "AtomicNumber": 37,
    "Symbol": "Rb",
    "Name": "Rubidium"
  },
  {
    "AtomicNumber": 38,
    "Symbol": "Sr",
    "Name": "Strontium"
  },
  {
    "AtomicNumber": 39,
    "Symbol": "Y",
    "Name": "Yttrium"
  },
  {
    "AtomicNumber": 40,
    "Symbol": "Zr",
    "Name": "Zirconium"
  },
  {
    "AtomicNumber": 41,
    "Symbol": "Nb",
    "Name": "Niobium"
  },
  {
    "AtomicNumber": 42,
    "Symbol": "Mo",
    "Name": "Molybdenum"
  },
  {
    "AtomicNumber": 43,
    "Symbol": "Tc",
    "Name": "Technetium"
  },
  {
    "AtomicNumber": 44,
    "Symbol": "Ru",
    "Name": "Ruthenium"
  },
  {
    "AtomicNumber": 45,
    "Symbol": "Rh",
    "Name": "Rhodium"
  },
  {
    "AtomicNumber": 46,
    "Symbol": "Pd",
    "Name": "Palladium"
  },
  {
    "AtomicNumber": 47,
    "Symbol": "Ag",
    "Name": "Silver"
  },
  {
    "AtomicNumber": 48,
    "Symbol": "Cd",
    "Name": "Cadmium"
  },
  {
    "AtomicNumber": 49,
    "Symbol": "In",
    "Name": "Indium"
  },
  {
    "AtomicNumber": 50,
    "Symbol": "Sn",
    "Name": "Tin"
  },
  {
    "AtomicNumber": 51,
    "Symbol": "Sb",
    "Name": "Antimony"
  },
  {
    "AtomicNumber": 52,
    "Symbol": "Te",
    "Name": "Tellurium"
  },
  {
    "AtomicNumber": 53,
    "Symbol": "I",
    "Name": "Iodine"
  },
  {
    "AtomicNumber": 54,
    "Symbol": "Xe",
    "Name": "Xenon"
  },
  {
    "AtomicNumber": 55,
    "Symbol": "Cs",
    "Name": "Cesium"
  },
  {
    "AtomicNumber": 56,
    "Symbol": "Ba",
    "Name": "Barium"
  },
  {
    "AtomicNumber": 57,
    "Symbol": "La",
    "Name": "Lanthanum"
  },
  {
    "AtomicNumber": 58,
    "Symbol": "Ce",
    "Name": "Cerium"
  },
  {
    "AtomicNumber": 59,
    "Symbol": "Pr",
    "Name": "Praseodymium"
  },
  {
    "AtomicNumber": 60,
    "Symbol": "Nd",
    "Name": "Neodymium"
  },
  {
    "AtomicNumber": 61,
    "Symbol": "Pm",
    "Name": "Promethium"
  },
  {
    "AtomicNumber": 62,
    "Symbol": "Sm",
    "Name": "Samarium"
  },
  {
    "AtomicNumber": 63,
    "Symbol": "Eu",
    "Name": "Europium"
  },
  {
    "AtomicNumber": 64,
    "Symbol": "Gd",
    "Name": "Gadolinium"
  },
  {
    "AtomicNumber": 65,
    "Symbol": "Tb",
    "Name": "Terbium"
  },
  {
    "AtomicNumber": 66,
    "Symbol": "Dy",
    "Name": "Dysprosium"
  },
  {
    "AtomicNumber": 67,
    "Symbol": "Ho",
    "Name": "Holmium"
  },
  {
    "AtomicNumber": 68,
    "Symbol": "Er",
    "Name": "Erbium"
  },
  {
    "AtomicNumber": 69,
    "Symbol": "Tm",
    "Name": "Thulium"
  },
  {
    "AtomicNumber": 70,
    "Symbol": "Yb",
    "Name": "Ytterbium"
  },
  {
    "AtomicNumber": 71,
    "Symbol": "Lu",
    "Name": "Lutetium"
  },
  {
    "AtomicNumber": 72,
    "Symbol": "Hf",
    "Name": "Hafnium"
  },
  {
    "AtomicNumber": 73,
    "Symbol": "Ta",
    "Name": "Tantalum"
  },
  {
    "AtomicNumber": 74,
    "Symbol": "W",
    "Name": "Tungsten"
  },
  {
    "AtomicNumber": 75,
    "Symbol": "Re",
    "Name": "Rhenium"
  },
  {
    "AtomicNumber": 76,
    "Symbol": "Os",
    "Name": "Osmium"
  },
  {
    "AtomicNumber": 77,
    "Symbol": "Ir",
    "Name": "Iridium"
  },
  {
    "AtomicNumber": 78,
    "Symbol": "Pt",
    "Name": "Platinum"
  },
  {
    "AtomicNumber": 79,
    "Symbol": "Au",
    "Name": "Gold"
  },
  {
    "AtomicNumber": 80,
    "Symbol": "Hg",
    "Name": "Mercury"
  },
  {
    "AtomicNumber": 81,
    "Symbol": "Tl",
    "Name": "Thallium"
  },
  {
    "AtomicNumber": 82,
    "Symbol": "Pb",
    "Name": "Lead"
  },
  {
    "AtomicNumber": 83,
    "Symbol": "Bi",
    "Name": "Bismuth"
  },
  {
    "AtomicNumber": 84,
    "Symbol": "Po",
    "Name": "Polonium"
  },
  {
    "AtomicNumber": 85,
    "Symbol": "At",
    "Name": "Astatine"
  },
  {
    "AtomicNumber": 86,
    "Symbol": "Rn",
    "Name": "Radon"
  },
  {
    "AtomicNumber": 87,
    "Symbol": "Fr",
    "Name": "Francium"
  },
  {
    "AtomicNumber": 88,
    "Symbol": "Ra",
    "Name": "Radium"
  },
  {
    "AtomicNumber": 89,
    "Symbol": "Ac",
    "Name": "Actinium"
  },
  {
    "AtomicNumber": 90,
    "Symbol": "Th",
    "Name": "Thorium"
  },
  {
    "AtomicNumber": 91,
    "Symbol": "Pa",
    "Name": "Protactinium"
  },
  {
    "AtomicNumber": 92,
    "Symbol": "U",
    "Name": "Uranium"
  },
  {
    "AtomicNumber": 93,
    "Symbol": "Np",
    "Name": "Neptunium"
  },
  {
    "AtomicNumber": 94,
    "Symbol": "Pu",
    "Name": "Plutonium"
  },
  {
    "AtomicNumber": 95,
    "Symbol": "Am",
    "Name": "Americium"
  },
  {
    "AtomicNumber": 96,
    "Symbol": "Cm",
    "Name": "Curium"
  },
  {
    "AtomicNumber": 97,
    "Symbol": "Bk",
    "Name": "Berkelium"
  },
  {
    "AtomicNumber": 98,
    "Symbol": "Cf",
    "Name": "Californium"
  },
  {
    "AtomicNumber": 99,
    "Symbol": "Es",
    "Name": "Einsteinium"
  },
  {
    "AtomicNumber": 100,
    "Symbol": "Fm",
    "Name": "Fermium"
  },
  {
    "AtomicNumber": 101,
    "Symbol": "Md",
    "Name": "Mendelevium"
  },
  {
    "AtomicNumber": 102,
    "Symbol": "No",
    "Name": "Nobelium"
  },
  {
    "AtomicNumber": 103,
    "Symbol": "Lr",
    "Name": "Lawrencium"
  },
  {
    "AtomicNumber": 104,
    "Symbol": "Rf",
    "Name": "Rutherfordium"
  },
  {
    "AtomicNumber": 105,
    "Symbol": "Db",
    "Name": "Dubnium"
  },
  {
    "AtomicNumber": 106,
    "Symbol": "Sg",
    "Name": "Seaborgium"
  },
  {
    "AtomicNumber": 107,
    "Symbol": "Bh",
    "Name": "Bohrium"
  },
  {
    "AtomicNumber": 108,
    "Symbol": "Hs",
    "Name": "Hassium"
  },
  {
    "AtomicNumber": 109,
    "Symbol": "Mt",
    "Name": "Meitnerium"
  },
  {
    "AtomicNumber": 110,
    "Symbol": "Ds",
    "Name": "Darmstadtium"
  },
  {
    "AtomicNumber": 111,
    "Symbol": "Rg",
    "Name": "Roentgenium"
  },
  {
    "AtomicNumber": 112,
    "Symbol": "Cn",
    "Name": "Copernicium"
  },
  {
    "AtomicNumber": 113,
    "Symbol": "Nh",
    "Name": "Nihonium"
  },
  {
    "AtomicNumber": 114,
    "Symbol": "Fl",
    "Name": "Flerovium"
  },
  {
    "AtomicNumber": 115,
    "Symbol": "Mc",
    "Name": "Moscovium"
  },
  {
    "AtomicNumber": 116,
    "Symbol": "Lv",
    "Name": "Livermorium"
  },
  {
    "AtomicNumber": 117,
    "Symbol": "Ts",
    "Name": "Tennessine"
  },
  {
    "AtomicNumber": 118,
    "Symbol": "Og",
    "Name": "Oganesson"
  }
]
FEEDSTOCKS = [
  {
    "feedstock_id": 1,
    "key": "electricity",
    "name": "Electricity"
  },
  {
    "feedstock_id": 2,
    "key": "naturalgas",
    "name": "NaturalGas"
  },
  {
    "feedstock_id": 3,
    "key": "alumina",
    "name": "Alumina"
  },
  {
    "feedstock_id": 4,
    "key": "ironore",
    "name": "IronOre"
  },
  {
    "feedstock_id": 5,
    "key": "water",
    "name": "Water"
  },
  {
    "feedstock_id": 6,
    "key": "bauxite",
    "name": "Bauxite"
  },
  {
    "feedstock_id": 7,
    "key": "coal",
    "name": "Coal"
  },
  {
    "feedstock_id": 8,
    "key": "salt",
    "name": "Salt"
  },
  {
    "feedstock_id": 9,
    "key": "fluorite",
    "name": "Fluorite"
  },
  {
    "feedstock_id": 10,
    "key": "potash",
    "name": "Potash"
  },
  {
    "feedstock_id": 11,
    "key": "dolomite",
    "name": "Dolomite"
  },
  {
    "feedstock_id": 12,
    "key": "phosphaterock",
    "name": "PhosphateRock"
  },
  {
    "feedstock_id": 13,
    "key": "carbon",
    "name": "Carbon"
  },
  {
    "feedstock_id": 14,
    "key": "quartz",
    "name": "Quartz"
  },
  {
    "feedstock_id": 15,
    "key": "genericore",
    "name": "GenericOre"
  }
]

def seed_forward(apps, schema_editor):
    Element = apps.get_model("core", "Element")
    Feedstock = apps.get_model("core", "Feedstock")

    # Elements
    for e in ELEMENTS:
        Element.objects.update_or_create(
            atomic_number=e["AtomicNumber"],
            defaults={"symbol": e["Symbol"], "name": e["Name"]}
        )
    # Feedstocks
    for f in FEEDSTOCKS:
        Feedstock.objects.update_or_create(
            feedstock_id=f["feedstock_id"],
            defaults={"key": f["key"], "name": f["name"]}
        )

def seed_backward(apps, schema_editor):
    Element = apps.get_model("core", "Element")
    Feedstock = apps.get_model("core", "Feedstock")
    # Optional: we keep masters; if you want to remove, uncomment:
    # Element.objects.all().delete()
    # Feedstock.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(seed_forward, seed_backward),
    ]
