def run():
    import os

    print("Importing...")
    try:
        from src.code.main import main
        print("Running 'main()'...")
        os.system("")
        main()
    except Exception as err:
        print(f"ERR:// {err}")


if __name__ == "__main__":
    run()
