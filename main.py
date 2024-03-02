from s3_interaction import interact_with_s3
import sys, traceback


def main():
    try:
        interact_with_s3()
    except KeyboardInterrupt:
        print ("Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == '__main__':
    main()
