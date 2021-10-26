def get_city_info(city, country, population = None):
    """Возвращает строку с информацией о городе."""
    info = f"{city.title()}, {country.title()}"
    if population:
        info += f" - population {population}"
    return info
