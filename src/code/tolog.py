def log(message: str, timestamp: bool):
    with open("../log.txt", "a") as logfile:
        import datetime

        if timestamp:
            timez = str(datetime.datetime.now().date()) + "-" + \
                    str(datetime.datetime.now().hour) + "-" + \
                    str(datetime.datetime.now().minute) + "-" + \
                    str(datetime.datetime.now().second) + "-" + \
                    str(datetime.datetime.now().microsecond)

            logfile.write(timez + ":===:" + message + "\n")

        elif not timestamp:
            logfile.write(message)

        logfile.close()
