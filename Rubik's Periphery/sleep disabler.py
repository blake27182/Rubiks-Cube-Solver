import RPi.GPIO as G
from time import sleep


def main():
    G.setmode(G.BCM)
    G.setup(4, G.OUT)
    G.setup(14, G.OUT)
    G.setup(22, G.OUT)
    G.setup(25, G.OUT)
    G.setup(13, G.OUT)
    G.setup(16, G.OUT)

    G.output(4, 1)
    G.output(14, 1)
    G.output(22, 1)
    G.output(25, 1)
    G.output(13, 1)
    G.output(16, 1)

    try:
        sleep(120)
    except KeyboardInterrupt:
        G.cleanup()
        return

    G.cleanup()


if __name__ == '__main__':
    main()
