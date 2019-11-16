def rebuild_dict(d, exclude=None):
    return {k: v for k, v in d.items() if k not in exclude}
