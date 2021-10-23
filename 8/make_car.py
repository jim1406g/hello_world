def make_car (model,
              **car_info):
    """Делаем запись о тачке с произвольными свойствами, model - обязательный параметр."""
    car_info['model'] = model
    return car_info
