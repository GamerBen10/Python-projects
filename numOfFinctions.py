import builtins
print(len([f for f in dir(builtins) if callable(getattr(builtins, f)) and not f.startswith("_")]))
