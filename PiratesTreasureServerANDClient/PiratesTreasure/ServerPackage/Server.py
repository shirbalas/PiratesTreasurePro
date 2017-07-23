from PiratesTreasure.ServerPackage import ConnectionThread
from PiratesTreasure.ServerPackage.Session import Session


def main():
    SerSOCK = Session()
    try:
        SerSOCK.ConnectionToClient_bind()
        SerSOCK.ConnectionToClient_listen()
        ConnectionThread.start()
    finally:
        SerSOCK.CloseTheSocket(SerSOCK)

    main()
