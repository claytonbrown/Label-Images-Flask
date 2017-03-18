from collections import OrderedDict

COLORS = [
    "white",
    "beige",
    "black",
    "brown",
    "grey",
    "blue",
    "navy-blue",
    "teal",
    "green",
    "olive-green",
    "pink",
    "red",
    "burgundy",
    "purple",
    "orange",
    "yellow",
]

PATTERNS = [
    "animal-print",
    "argyle",
    "horizontal-stripe",
    "vertical-stripe",
    "checkered",
    "dotted",
    "floral",
    "plaid"
]

MATERIALS = [
    "denim",
    "dry-fit"
]

TOP_TYPE = [
    "short-sleeve-shirt",
    "long-sleeve-shirt",
    "short-sleeve-t-shirt",
    "long-sleeve-t-shirt",
    "polo",
    "singlet"
]

TOP_STYLE = [
    "oxford",
    "dress",
    "round-neck",
    "henley",
    "graphic",
    "pocket",
    "acid-wash",
    "granddad-collar",
    "placket"
]

BOTTOM_TYPE = [
    "pants",
    "shorts",
    "jeans"
]

BOTTOM_STYLE = [
    "cargo",
    "dress",
    "chinos",
    "sweatpants",
    "ripped",
    "acid-wash",
    "washed"
]

SHOE_TYPE = [
    "boat",
    "boots",
    "loafers",
    "trainers",
    "sandals",
    "dress-shoes",
    "casual-shoes",
    "plimsolls"
]

SHOE_OTHERS = [
    "leather",
    "canvas"
]

DEFAULTS = OrderedDict()
DEFAULTS["top-primary-color"] = COLORS
DEFAULTS["top-secondary-color"] = COLORS
DEFAULTS["top-type"] = TOP_TYPE
DEFAULTS["top-patterns"] = PATTERNS
DEFAULTS["top-style"] = TOP_STYLE
DEFAULTS["top-material"] = MATERIALS
DEFAULTS["bottom-primary-color"] = COLORS
DEFAULTS["bottom-secondary-color"] = COLORS
DEFAULTS["bottom-type"] = BOTTOM_TYPE
DEFAULTS["bottom-patterns"] = PATTERNS
DEFAULTS["bottom-style"] = BOTTOM_STYLE
DEFAULTS["bottom-material"] = MATERIALS
DEFAULTS["shoes-primary-color"] = COLORS
DEFAULTS["shoes-secondary-color"] = COLORS
DEFAULTS["shoes-type"] = SHOE_TYPE
DEFAULTS["shoes-others"] = SHOE_OTHERS

# DEFAULTS = {
#     "top-primary-color": COLORS,
#     "top-secondary-color": COLORS,
#     "top-type": TOP_TYPE,
#     "top-style": TOP_STYLE,
#     "top-material": MATERIALS,
#     "bottom-primary-color": COLORS,
#     "bottom-secondary-color": COLORS,
#     "bottom-type": BOTTOM_TYPE,
#     "bottom-style": BOTTOM_STYLE,
#     "bottom-material": MATERIALS,
#     "shoes-primary-color": COLORS,
#     "shoes-secondary-color": COLORS,
#     "shoe-type": SHOE_TYPE,
#     "shoe-others": SHOE_OTHERS
# }
