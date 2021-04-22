

def get_or_none(model, **kwargs):
    """
    :param model: name of the Model
    :param kwargs: lookup_fields
    :return: instance or None
    """
    try:
        obj = model.objects.get(**kwargs)
    except model.DoesNotExist:
        obj = None
    return obj
