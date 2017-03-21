from collections import OrderedDict

COLORS = [
    "white",
    "beige",
    "black",
    "brown",
    "grey",
    "blue",
    "navy",
    "teal",
    "green",
    "olive",
    "pink",
    "red",
    "maroon",
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

# ADD MORE MATERIALS?
MATERIALS = [
    "denim",
    "dry-fit",
    "cotton"
]

TOP_TYPE = [
    "short-sleeve-shirt",
    "long-sleeve-shirt",
    "short-sleeve-t-shirt",
    "long-sleeve-t-shirt",
    "polo",
    "singlet"
]

#this is more specific to t-shirts
TOP_FIT = [
    "slim-fit",
    "longline",
    "baggy"
]

#should we split into t-shirt and shirt style?
TOP_STYLE = [
    "oxford",
    "dress",
    "round-neck",
    "henley",
    "graphic",
    "pocket",
    "acid-wash",
    "granddad-collar",
    "placket",
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

TOPS = OrderedDict()
TOPS["top-primary-color"] = COLORS
TOPS["top-secondary-color"] = COLORS
TOPS["top-type"] = TOP_TYPE
TOPS["top-patterns"] = PATTERNS
TOPS["top-style"] = TOP_STYLE
TOPS["top-material"] = MATERIALS

BOTTOMS = OrderedDict()
BOTTOMS["bottom-primary-color"] = COLORS
BOTTOMS["bottom-secondary-color"] = COLORS
BOTTOMS["bottom-type"] = BOTTOM_TYPE
BOTTOMS["bottom-patterns"] = PATTERNS
BOTTOMS["bottom-style"] = BOTTOM_STYLE
BOTTOMS["bottom-material"] = MATERIALS

SHOES = OrderedDict()
SHOES["shoes-primary-color"] = COLORS
SHOES["shoes-secondary-color"] = COLORS
SHOES["shoes-type"] = SHOE_TYPE
SHOES["shoes-others"] = SHOE_OTHERS