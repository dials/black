import sys


def patched_main():
    if sys.hexversion < 0x3060000:
        print("Need Python 3.6+ to run black. Skipping.")
        sys.exit(0)
    import black

    return black.patched_main()
