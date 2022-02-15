def getClearCmd():
    import platform

    try:
        # print("Getting OS..")
        # print(platform.system())
        plat = platform.system()
            
        if plat == "linux" or "darwin":  # darwin is macos for some reason?
            return "clear"

        elif plat == "Windows":
            return "cls"

        else:
            print("Unknown command to clear terminal. Applying 'clear'")
            return "clear"

    except Exception as err:
        import os
        print(f"ERR:// {err}")
        return f"ERR:// {err}"
