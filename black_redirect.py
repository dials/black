import sys


def patched_main():
    if sys.hexversion >= 0x3060000:
        # we are python3. this is fine. just do the thing.
        import black

        return black.patched_main()

    if sys.version_info[0] == 2:
        # so we're in python2 and can't run black.
        # but maybe there is a python3 out there that can.
        import procrunner

        clean_env = {"PYTHONPATH": "", "LD_LIBRARY_PATH": ""}
        try:
            have_black = not procrunner.run(
                ["python3", "-c", "import black"],
                print_stderr=False,
                print_stdout=False,
                environment_override=clean_env,
            )["exitcode"]
        except Exception:
            have_black = False
        if have_black:
            # guess what - there is!
            print("RUNNING", ["python3", "-m", "black"], sys.argv)
            sys.exit(
                procrunner.run(
                    ["python3", "-m", "black"] + sys.argv,
                    environment_override=clean_env,
                )["exitcode"]
            )

    # give up with exitcode==0 so the commit can go ahead
    print("Need Python 3.6+ to run black. Skipping.")
    sys.exit(0)
