MARCAS = ["JIM", "BLU MONT", "JIMMISS", "MISS"]

DIVISIONES = ["CABALLERO", "BEBE", "RECIEN NACIDO", "PREESCOLAR", "NIÑAS", "NIÑOS"]

SERIES = ["JIM ACTIVE", "ORANGUTAN", "FESTA", "CEREMONIA", "ELEPHANT", "JIRAFA", "PREMATURO", "DOG", "MARIPOSA",
          "BASIC", "CASITAS", "FLOR", "FRENCH", "ENRREDADERA", "TEAM"]

COMPOSICIONES = ["100% ALGODON", "CHIFON LIKRA"]

COLORES = [
    {"TITLE": "BLANCO", "SKU_SUFIX": "BLA", "HEX": "#FFF"},
    {"TITLE": "MARINO", "SKU_SUFIX": "MAR", "HEX": "#000"},
    {"TITLE": "HUESO", "SKU_SUFIX": "HUE", "HEX": "#000"},
    {"TITLE": "CIELO", "SKU_SUFIX": "CIE", "HEX": "#000"},
    {"TITLE": "ROSA", "SKU_SUFIX": "ROS", "HEX": "#000"},
    {"TITLE": "PAJA", "SKU_SUFIX": "PAJ", "HEX": "#000"},
]

TALLAS = [
    {"TITLE": "CHICA", "SKU_SUFIX": "CH", "SHORT": "Ch", "ORDER": 0},
    {"TITLE": "MEDIANA", "SKU_SUFIX": "ME", "SHORT": "Md", "ORDER": 1},
    {"TITLE": "GRANDE", "SKU_SUFIX": "GR", "SHORT": "G", "ORDER": 2},
    {"TITLE": "EXTRA GRANDE", "SKU_SUFIX": "EG", "SHORT": "XG", "ORDER": 3},

    {"TITLE": "RECIEN NACIDO", "SKU_SUFIX": "1P", "SHORT": "RECIEN NACIDO", "ORDER": 0},

    {"TITLE": "0 MESES", "SKU_SUFIX": "00", "SHORT": "0 Meses", "ORDER": 0},
    {"TITLE": "1 MES", "SKU_SUFIX": "01", "SHORT": "1 Mes", "ORDER": 0},
    {"TITLE": "3 MESES", "SKU_SUFIX": "03", "SHORT": "3 Meses", "ORDER": 1},
    {"TITLE": "6 MESES", "SKU_SUFIX": "06", "SHORT": "6 Meses", "ORDER": 2},
    {"TITLE": "12 MESES", "SKU_SUFIX": "12", "SHORT": "12 Meses", "ORDER": 3},
    {"TITLE": "18 MESES", "SKU_SUFIX": "18", "SHORT": "18 Meses", "ORDER": 4},

    {"TITLE": "1 AÑO", "SKU_SUFIX": "01", "SHORT": "1 Año", "ORDER": 0},
    {"TITLE": "2 AÑOS", "SKU_SUFIX": "02", "SHORT": "2 Años", "ORDER": 0},
    {"TITLE": "3 AÑOS", "SKU_SUFIX": "03", "SHORT": "3 Años", "ORDER": 0},
    {"TITLE": "4 AÑOS", "SKU_SUFIX": "04", "SHORT": "4 Años", "ORDER": 0},
    {"TITLE": "6 AÑOS", "SKU_SUFIX": "06", "SHORT": "6 Años", "ORDER": 0},
    {"TITLE": "8 AÑOS", "SKU_SUFIX": "08", "SHORT": "8 Años", "ORDER": 0},
    {"TITLE": "10 AÑOS", "SKU_SUFIX": "10", "SHORT": "10 Años", "ORDER": 0},
    {"TITLE": "12 AÑOS", "SKU_SUFIX": "12", "SHORT": "12 Años", "ORDER": 0},
    {"TITLE": "14 AÑOS", "SKU_SUFIX": "14", "SHORT": "14 Años", "ORDER": 0},
]

SKU = {
    "909501": {
        "MARCA": "JIM",
        "DIVISION": "CABALLERO",
        "DESCRIPCION": "CAMISETA TIRANTES",
        "SERIE": "JIM ACTIVE",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 81,
        "PRECIO": 135,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["CHICA", "MEDIANA", "GRANDE", "EXTRA GRANDE"]
            },
        }
    },
    "909801": {
        "MARCA": "JIM",
        "DIVISION": "CABALLERO",
        "DESCRIPCION": 'CAMISETA "V" M/C',
        "SERIE": "JIM ACTIVE",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 119.40,
        "PRECIO": 199,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["CHICA", "GRANDE", "MEDIANA"]
            },
            "MARINO": {
                "TALLAS": ["CHICA", "GRANDE", "MEDIANA"]
            }
        }
    },
    "910001": {
        "MARCA": "JIM",
        "DIVISION": "CABALLERO",
        "DESCRIPCION": 'TRUSA',
        "SERIE": "ORANGUTAN",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 81,
        "PRECIO": 135,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["CHICA", "GRANDE", "MEDIANA"]
            },
            "MARINO": {
                "TALLAS": ["CHICA", "GRANDE", "MEDIANA"]
            }
        }
    },
    "910101": {
        "MARCA": "JIM",
        "DIVISION": "CABALLERO",
        "DESCRIPCION": 'BOXER',
        "SERIE": "ORANGUTAN",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 93,
        "PRECIO": 155,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["CHICA", "GRANDE", "MEDIANA"]
            },
            "MARINO": {
                "TALLAS": ["CHICA", "GRANDE", "MEDIANA"]
            }
        }
    },
    "C60080": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY SM',
        "SERIE": "FESTA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 75,
        "PRECIO": 125,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 MES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "C60180": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY MC',
        "SERIE": "FESTA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 87,
        "PRECIO": 145,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 MES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "C60280": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY ML',
        "SERIE": "FESTA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 89.40,
        "PRECIO": 149,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 MES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "C68080": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY SM',
        "SERIE": "CEREMONIA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 75,
        "PRECIO": 125,
        "COLORES": {
            "HUESO": {
                "TALLAS": ["1 MES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "C68180": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY MC',
        "SERIE": "CEREMONIA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 81,
        "PRECIO": 135,
        "COLORES": {
            "HUESO": {
                "TALLAS": ["1 MES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "C68280": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY ML',
        "SERIE": "CEREMONIA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 83.40,
        "PRECIO": 139,
        "COLORES": {
            "HUESO": {
                "TALLAS": ["1 MES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "D21080": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY SM',
        "SERIE": "ELEPHANT",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 71.40,
        "PRECIO": 119,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "D21180": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY MC',
        "SERIE": "ELEPHANT",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 75,
        "PRECIO": 125,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "D21280": {
        "MARCA": "BLU MONT",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY ML',
        "SERIE": "ELEPHANT",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 77.40,
        "PRECIO": 129,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
        }
    },
    "102832": {
        "MARCA": "JIMMISS",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'BODY MC',
        "SERIE": "JIRAFA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 75,
        "PRECIO": 125,
        "COLORES": {
            "CIELO": {
                "TALLAS": ["0 MESES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
            "ROSA": {
                "TALLAS": ["0 MESES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            }
        }
    },
    "103032": {
        "MARCA": "JIMMISS",
        "DIVISION": "BEBE",
        "DESCRIPCION": 'MALLA CON PIES',
        "SERIE": "JIRAFA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 57,
        "PRECIO": 95,
        "COLORES": {
            "CIELO": {
                "TALLAS": ["0 MESES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            },
            "ROSA": {
                "TALLAS": ["0 MESES", "3 MESES", "6 MESES", "12 MESES", "18 MESES"]
            }
        }
    },
    "556132": {
        "MARCA": "JIMMISS",
        "DIVISION": "RECIEN NACIDO",
        "DESCRIPCION": 'BODY ML',
        "SERIE": "PREMATURO",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 63,
        "PRECIO": 105,
        "COLORES": {
            "PAJA": {
                "TALLAS": ["RECIEN NACIDO"]
            },
            "CIELO": {
                "TALLAS": ["RECIEN NACIDO"]
            },
            "ROSA": {
                "TALLAS": ["RECIEN NACIDO"]
            },
        }
    },
    "556532": {
        "MARCA": "JIMMISS",
        "DIVISION": "RECIEN NACIDO",
        "DESCRIPCION": 'MALLAS CON PIE',
        "SERIE": "PREMATURO",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 45,
        "PRECIO": 75,
        "COLORES": {
            "PAJA": {
                "TALLAS": ["RECIEN NACIDO"]
            },
            "CIELO": {
                "TALLAS": ["RECIEN NACIDO"]
            },
            "ROSA": {
                "TALLAS": ["RECIEN NACIDO"]
            },
        }
    },
    "E11032": {
        "MARCA": "JIMMISS",
        "DIVISION": "PREESCOLAR",
        "DESCRIPCION": 'CAMISETA MC',
        "SERIE": "DOG",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 59.40,
        "PRECIO": 99,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 AÑO", "2 AÑOS", "3 AÑOS", "4 AÑOS"]
            }
        }
    },
    "E11132": {
        "MARCA": "JIMMISS",
        "DIVISION": "PREESCOLAR",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "DOG",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 53.40,
        "PRECIO": 89,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 AÑO", "2 AÑOS", "3 AÑOS", "4 AÑOS"]
            }
        }
    },
    "E11232": {
        "MARCA": "JIMMISS",
        "DIVISION": "PREESCOLAR",
        "DESCRIPCION": 'CAMISETA ML',
        "SERIE": "DOG",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 63,
        "PRECIO": 105,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 AÑO", "2 AÑOS", "3 AÑOS", "4 AÑOS"]
            }
        }
    },
    "E1133": {
        "MARCA": "JIMMISS",
        "DIVISION": "PREESCOLAR",
        "DESCRIPCION": 'BOXER',
        "SERIE": "DOG",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 57,
        "PRECIO": 95,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["1 AÑO", "2 AÑOS", "3 AÑOS", "4 AÑOS"]
            }
        }
    },
    "J59032": {
        "MARCA": "JIMMISS",
        "DIVISION": "PREESCOLAR",
        "DESCRIPCION": 'PANTALETA',
        "SERIE": "MARIPOSA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 45,
        "PRECIO": 75,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "3 AÑOS", "4 AÑOS", "6 AÑOS"]
            }
        }
    },
    "J59132": {
        "MARCA": "JIMMISS",
        "DIVISION": "PREESCOLAR",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "MARIPOSA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 57,
        "PRECIO": 95,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "3 AÑOS", "4 AÑOS", "6 AÑOS"]
            }
        }
    },
    "119123": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "BASIC",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 45,
        "PRECIO": 75,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "119220": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'PANTALETA',
        "SERIE": "BASIC",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 39,
        "PRECIO": 65,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "616123": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "CASITAS",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 51.01,
        "PRECIO": 85,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "616420": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'PANTALETA',
        "SERIE": "CASITAS",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 41.40,
        "PRECIO": 65,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "680020": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'PANTALETA',
        "SERIE": "FLOR",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 45,
        "PRECIO": 75,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "680123": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "FLOR",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 53.39,
        "PRECIO": 89,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "874220": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'PANTALETA',
        "SERIE": "FRENCH",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 51.01,
        "PRECIO": 85,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "874423": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "FRENCH",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 57,
        "PRECIO": 95,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "872620": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'PANTALETA',
        "SERIE": "ENRREDADERA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 53.39,
        "PRECIO": 89,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "872823": {
        "MARCA": "MISS",
        "DIVISION": "NIÑAS",
        "DESCRIPCION": 'CAMISETA T',
        "SERIE": "ENRREDADERA",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 53.39,
        "PRECIO": 89,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS"]
            }
        }
    },
    "875604": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'CAMISETA TIRANTES',
        "SERIE": "TEAM",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 59.40,
        "PRECIO": 99,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "118704": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'CAMISETA MC',
        "SERIE": "BASIC",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 53.39,
        "PRECIO": 89,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "118804": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'CAMISETA S/M',
        "SERIE": "BASIC",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 51.01,
        "PRECIO": 85,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "118904": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'TRUSA',
        "SERIE": "BASIC",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 39,
        "PRECIO": 65,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["2 AÑOS", "4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "E21004": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'CAMISETA MC',
        "SERIE": "BASIC",
        "COMPOSICION": "100% ALGODON",
        "COSTO": 65.40,
        "PRECIO": 109,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "E21304": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'BOXER (PZA)',
        "SERIE": "DOG",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 63,
        "PRECIO": 105,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    },
    "E21604": {
        "MARCA": "JIM",
        "DIVISION": "NIÑOS",
        "DESCRIPCION": 'CAMISETA ML',
        "SERIE": "DOG",
        "COMPOSICION": "CHIFON LIKRA",
        "COSTO": 69,
        "PRECIO": 115,
        "COLORES": {
            "BLANCO": {
                "TALLAS": ["4 AÑOS", "6 AÑOS", "8 AÑOS", "10 AÑOS", "12 AÑOS", "14 AÑOS"]
            }
        }
    }
}
