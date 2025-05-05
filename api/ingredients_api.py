from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Mock database
foods = [
    {
        "name": "Skimmed milk",
        "group": "Dairy",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Natural Yougurt",
        "group": "Dairy",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Evaporate milk",
        "group": "Dairy",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Powdered milk",
        "group": "Dairy",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Soft cheese",
        "group": "Dairy",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Chard",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Achogchas",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Artichokes",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Celery",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Aubergine",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Broccoli",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Onions",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cabbage",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cauliflower",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Spinach",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Asparagus",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Raddishes",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Lettuce Turnip",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Bell pepper",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cucumber",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Green beans",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "White carrots",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Zucchini",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Pumpkin",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tomato",
        "group": "Vegetables",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Babaco",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Plum",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Peach",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Strawberries",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Guava",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Currants",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Guaba",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Sweet granadilla",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Lime",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tangerine",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Mango",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Apple",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Melon",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Blackberries",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Passion fruit",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Orange",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Lulo",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Ovitos",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Papaya",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Pear",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Pineapple",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Watermelon",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tamarind",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Grapefruit",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tree tomato",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Prickly pear",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Banana passion fruit",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Prunes",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cherimoya",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Soursop",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Mamey",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Raisins",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Banana",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Small banana",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Grapes",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Sapote",
        "group": "Fruits",
        "isVegan": True,
        "isVegetarian": True,
        "isHalal": True,
        "isKosher": True,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Slice bread",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Pan redondo",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Crackers",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Rosquillas",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Pan de yuca",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tortilla",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cooked rice",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Spaghetti",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Flour",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Potato",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cassava",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Sweet potate",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Lupini beans",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tender beans",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Dried legumes",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cooked hominy",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Corn flakes",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tender corn",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Wheat germ",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Loose plantain",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Pop corn",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Roasted corn",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Mashed potato or carrot",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cereals",
        "group": "Grains",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Oil: soya, corn, sunflower, olive",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Butter",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "butterfat",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "cream",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Olives",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "capers (conserve)",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Avocado",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Cream cheese",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Grated coconut",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Mayonnaise or any other sauce",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Peanut",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Almonds",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "hazelnuts",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "pistachio",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Bacon",
        "group": "Fats",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Goat meat",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "pork",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "beef",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "lamb",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "liver",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "tongue",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Chicken",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "turkey",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "duck (with not skin)",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Fish",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "corvina",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "trout",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "sole",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "dried cod",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Ham",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "salami",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "cottage pie",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Sausages",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "chorizo",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Oysters",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "mussels",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "shells",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Medium prawns o small lobsters",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Tuna in water",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Crabs",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Sardines",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
        "name": "Lobster",
        "group": "Proteins",
        "isVegan": False,
        "isVegetarian": False,
        "isHalal": False,
        "isKosher": False,
        "fats_per_100g": 0,
        "proteins_per_100g": 0,
        "carbs_per_100g": 0,
        "calories_per_100g": 0,
        "suggested_portion": {
            "description": "",
            "weight_in_grams": 0,
            "fats": 0,
            "proteins": 0,
            "carbs": 0
        },
        "price_range": 0,
        "estimated_cost_per_portion": {
            "amount": 0,
            "currency": "GBP"
        }
    },
    {
    "name": "Egg",
    "group": "Proteins",
    "isVegan": False,
    "isVegetarian": True,
    "isHalal": True,
    "isKosher": True,
    "fats_per_100g": 9.5,
    "proteins_per_100g": 12.6,
    "carbs_per_100g": 0.7,
    "calories_per_100g": 143,
    "suggested_portion": {
        "description": "1 large egg",
        "weight_in_grams": 50,
        "fats": 4.8,
        "proteins": 6.3,
        "carbs": 0.4
    },
    "price_range": 2,
    "estimated_cost_per_portion": {
            "amount": 0.25,
            "currency": "GBP"
        }
    }
]

# Filtering logic
def filter_foods(
    food_list,
    vegan: bool = False,
    vegetarian: bool = False,
    halal: bool = False,
    kosher: bool = False,
    lactose_intolerant: bool = False,
    keto: bool = False
):
    excluded_groups = set()
    if lactose_intolerant:
        excluded_groups.add("Dairy")
    if keto:
        excluded_groups.add("Fruits")
        excluded_groups.add("Vegetables")

    filtered = []
    for food in food_list:
        if food["group"] in excluded_groups:
            continue
        if vegan and not food["isVegan"]:
            continue
        if vegetarian and not food["isVegetarian"]:
            continue
        if halal and not food["isHalal"]:
            continue
        if kosher and not food["isKosher"]:
            continue
        if keto and food["carbs_per_100g"] > 10:
            continue
        filtered.append(food)

    return filtered

# API endpoint
@app.get("/filtered-foods")
def get_filtered_foods(
    vegan: bool = Query(False),
    vegetarian: bool = Query(False),
    halal: bool = Query(False),
    kosher: bool = Query(False),
    lactose_intolerant: bool = Query(False),
    keto: bool = Query(False)
):
    return filter_foods(
        foods,
        vegan=vegan,
        vegetarian=vegetarian,
        halal=halal,
        kosher=kosher,
        lactose_intolerant=lactose_intolerant,
        keto=keto
    )



# endpoint to get all foods
@app.get("/foods")
def get_all_foods():
    return foods

# endpoint to get food by name
@app.get("/foods/{food_name}")
def get_food_by_name(food_name: str):
    food = next((food for food in foods if food["name"].lower() == food_name.lower()), None)
    if food:
        return food
    return {"error": "Food not found"}

# endpoint to get food by group
@app.get("/foods/group/{group_name}")
def get_foods_by_group(group_name: str):
    food_group = [food for food in foods if food["group"].lower() == group_name.lower()]
    if food_group:
        return food_group
    return {"error": "Group not found"}

# endpoint to get food by price range
@app.get("/foods/price/{min_price}/{max_price}")
def get_foods_by_price(min_price: float, max_price: float):
    food_price_range = [food for food in foods if min_price <= food["estimated_cost_per_portion"]["amount"] <= max_price]
    if food_price_range:
        return food_price_range
    return {"error": "No foods found in this price range"}

# endpoint to get food if partial coinsidence
@app.get("/foods/partial/{partial_name}")
def get_foods_partial(partial_name: str):
    food_partial = [food for food in foods if partial_name.lower() in food["name"].lower()]
    if food_partial:
        return food_partial
    return {"error": "No foods found with this partial name"}

# endpoint to filter foods by group and price range
@app.get("/foods/group-price/{group_name}/{min_price}/{max_price}")
def get_foods_by_group_and_price(group_name: str, min_price: float, max_price: float):
    food_group_price = [food for food in foods if food["group"].lower() == group_name.lower() and min_price <= food["estimated_cost_per_portion"]["amount"] <= max_price]
    if food_group_price:
        return food_group_price
    return {"error": "No foods found in this group and price range"}

#filter by group and price range
@app.get("/foods/group-price/{group_name}/{min_price}/{max_price}")
def get_foods_by_group_and_price(group_name: str, min_price: float, max_price: float):
    food_group_price = [food for food in foods if food["group"].lower() == group_name.lower() and min_price <= food["estimated_cost_per_portion"]["amount"] <= max_price]
    if food_group_price:
        return food_group_price
    return {"error": "No foods found in this group and price range"}

# To run this API: uvicorn ingredients_api:app --reload --port 8001