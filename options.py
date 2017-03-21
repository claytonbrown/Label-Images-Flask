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
TOP_MATERIAL = [
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
TSHIRT_FIT = [
    "slim-fit",
    "longline",
    "baggy"
]

SHIRT_FIT = [
    "slim-fit",
    "regular-fit"
]

#should we split into t-shirt and shirt style?
SHIRT_STYLE = [
    "oxford",
    "dress",
    "graphic",
    "pocket",
    "granddad-collar",
]

TSHIRT_STYLE = [
    "graphic-text",
    "graphic-image",
    "round-neck",
    "henley",
    "pocket",
]


BOTTOM_TYPE = [
    "long pants",
    "shorts",
]

BOTTOM_MATERIAL = [
    "denim/jeans",
    "cotton",
    "dry-fit"
]


BOTTOM_STYLE = [
    "cargo",
    "dress",
    "chinos",
    "sweatpants",
]

BOTTOM_FIT = [
    "skinny-fit",
    "slim-fit",
    "regular-fit",
    "baggy"
]

DENIM_STYLE = [
    "ripped",
    "acid-wash",
    "washed"
]

SHOE_TYPE = [
    "boat/loafer",
    "boots",
    "sneakers",
    "sport"
    "sandals",
    "dress-shoes",
    "casual-shoes",
]

SHOE_MATERIAL = [
    "leather",
    "canvas",
    "suede"
]

SHOE_OTHERS = [
    "toe-cap",
    "gum-sole",
    "with-logo"

]

# DEFAULTS = OrderedDict()
# DEFAULTS["top-primary-color"] = COLORS
# DEFAULTS["top-secondary-color"] = COLORS
# DEFAULTS["top-type"] = TOP_TYPE
# DEFAULTS["top-patterns"] = PATTERNS
# DEFAULTS["top-style"] = TOP_STYLE
# DEFAULTS["top-material"] = MATERIALS
# DEFAULTS["bottom-primary-color"] = COLORS
# DEFAULTS["bottom-secondary-color"] = COLORS
# DEFAULTS["bottom-type"] = BOTTOM_TYPE
# DEFAULTS["bottom-patterns"] = PATTERNS
# DEFAULTS["bottom-style"] = BOTTOM_STYLE
# DEFAULTS["bottom-material"] = MATERIALS
# DEFAULTS["shoes-primary-color"] = COLORS
# DEFAULTS["shoes-secondary-color"] = COLORS
# DEFAULTS["shoes-type"] = SHOE_TYPE
# DEFAULTS["shoes-others"] = SHOE_OTHERS

TOPS = OrderedDict()
TOPS["top-primary-color"] = COLORS
TOPS["top-secondary-color"] = COLORS
TOPS["top-type"] = TOP_TYPE
TOPS["t-shirt-style"] = TSHIRT_STYLE
TOPS["shirt-style"] = SHIRT_STYLE
TOPS["t-shirt-fit"] = TSHIRT_FIT
TOPS["shirt-fit"] = SHIRT_FIT
TOPS["top-patterns"] = PATTERNS
TOPS["top-material"] = TOP_MATERIAL

BOTTOMS = OrderedDict()
BOTTOMS["bottom-primary-color"] = COLORS
BOTTOMS["bottom-secondary-color"] = COLORS
BOTTOMS["bottom-type"] = BOTTOM_TYPE
BOTTOMS["bottom-material"] = BOTTOM_MATERIAL
BOTTOMS["denim-style"] = DENIM_STYLE
BOTTOMS["bottom-patterns"] = PATTERNS
BOTTOMS["bottom-style"] = BOTTOM_STYLE
BOTTOMS["bottom-fit"] = BOTTOM_FIT


SHOES = OrderedDict()
SHOES["shoes-primary-color"] = COLORS
SHOES["shoes-secondary-color"] = COLORS
SHOES["shoes-type"] = SHOE_TYPE
SHOES["shoes-others"] = SHOE_OTHERS