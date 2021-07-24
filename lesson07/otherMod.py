import logging

def add(x, y):
    """"""
    logging.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y

def div(x, y):
    """"""
    try:
        result = x/y
        logging.info("divide %s and %s to get %s" % (x, y, result))
        return result
    except Exception as e:
        logging.error("Divide  %s and %s exception % s" % (x, y, e))



