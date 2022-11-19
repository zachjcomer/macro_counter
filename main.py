import routine

def main():
    r1 = routine.Routine()
    r1.setName('Richard')
    r1.addBlock()
    r1.addBlock()
    r1.addBlock()
    r1.addBlock()
    r1.moveBlock(0, 2)
    r1.delBlock(1)
    r1.run()

if __name__ == '__main__':
    main()