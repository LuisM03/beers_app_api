def beer_schema(beer) -> dict:
    return {
        "id": str(beer["_id"]),
        "name": beer["name"],
        "nickname": beer["nickname"],
        "unit_price": beer["unit_price"],
        "price_basket": beer["price_basket"],
        "structure": beer["structure"],
        "year_issue": beer["year_issue"],
        "image": beer["image"]
    }
    
def beers_schema(beers) -> list:
    return [beer_schema(beer) for beer in beers]