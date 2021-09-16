class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        sec = 0

        while sec < 1:
            print(f'traffic light is switchng on')
            sec += 1
        if sec == 7:
            print('red color')
        elif sec == 2:
            print('yellow color')
        elif sec == 1:
            print('green color')
        else:
            sec += 1

my_traffic_time = TrafficLight('Mine')
my_traffic_time. running()