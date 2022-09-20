class Controltower:
    def __init__(self):
        self.to_land = []
        self.to_take_off = []

    def reconocimiento(self,airplane,status):
        if status == 1:
            self.to_land.append(airplane)
        elif status == 2:
            self.to_take_off.append(airplane)

    def action(self):
        if len(self.to_land) > 0:
            try:
                self.to_land.pop(0)
                print("Airplane landed succesfully")
            except IndexError:
                print("Landing queue is empty")

        elif len(self.to_take_off) > 0:
            try:
                self.to_take_off.pop(0)
                print(ValueError("Airplane took off succesfully"))
            except IndexError:
                print(ValueError("Take off queue is empty"))

        else:
            print("Landing and taking off queues are empty")

    def __str__(self):
        print("Landing queue status is:" + str(len(self.to_land)))
        print("Take off queue status is:" + str(len(self.to_take_off)))
