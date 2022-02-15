def wthrUI():
    import splash as ss
    import chk
    import threading

    # creating thread
    ssThread = threading.Thread(target=ss.splash())
    chkThread = threading.Thread(target=chk.chk())

    # starting threads
    chkThread.start()
    ssThread.start()

    # stopping threads.
    chkThread.join()
    ssThread.join()




    # both threads completely executed
    print("Done!")


wthrUI()
