import logging
import otherMod

def main():
    """
    The main entry point of the application
    """

    logging.basicConfig(filename="myApp.log", level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7, 8)
    print(result)
    result = otherMod.div(7, 0)
    print(result)
    logging.info("Done!")


if __name__ == "__main__":
    main()