import os


def find_extensions():
        all_extensions=[]
        for root, dirs, files in os.walk('cogs'):
                if root.endswith("__pycache__"): continue
                for file in files:
                    if file.endswith(".py") and file != "__init__.py":
                        module_path = root.replace(os.sep, ".")
                        all_extensions.append(f"{module_path}.{file[:-3]}")
        return all_extensions


def load_cogs(bot):
    all_extensions = find_extensions()

    for extension in all_extensions:
        try:
            bot.load_extension(f"{extension}")
            print("Загружено", f"{extension}")
        except Exception as e:
            print("Не загружено", f"{extension}", e)

