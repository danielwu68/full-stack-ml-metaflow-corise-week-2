from metaflow import FlowSpec, step, card, current


class FanTest(FlowSpec):
    @step
    def start(self):
        print("Starting...")
        self.x = "start"

        print(f"in start: {self.x=}")

        self.next(self.fan_1, self.fan_2)

    @step
    def fan_1(self):
        self.x = "fan_1"
        print(f"in fan_1: {self.x=}")

        self.next(self.join)

    @step
    def fan_2(self):
        # self.x = "fan_2"
        print(f"in fan_2: {self.x=}")

        self.next(self.join)

    @step
    def join(self):
        print(f"in jon: {self.x=}")
        self.next(self.end)

    @step
    def end(self):
        print(f"in end: {self.x=}")


if __name__ == '__main__':
    FanTest()
