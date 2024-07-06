# # ex 1
# class MyShows:
#     def __init__(self, name, platform, year, episode=1, rating=None, actors=None):
#         self.__name = name
#         self.__platform = platform
#         self.__release_year = year
#         self.__current_episode = episode
#         self.__rating = rating
#         self.__actors = actors
#
#     def get_name(self):
#         return self.__name
#
#     def get_platform(self):
#         return self.__platform
#
#     def get_release_year(self):
#         return self.__release_year
#
#     def get_current_episode(self):
#         return self.__current_episode
#
#     def get_rating(self):
#         return self.__rating
#
#     def get_actors(self):
#         return self.__actors
#
#     def set_current_episode(self, episode):
#         self.__current_episode = episode
#
#     def set_rating(self, rating):
#         if 1 <= rating <= 10:
#             self.__rating = rating
#         else:
#             raise ValueError
#
#     def del_rating(self):
#         self.__rating = None
#
#     def add_actor(self, actor):
#         if actor not in self.__actors:
#             self.__actors.append(actor)
#
#     def remove_actor(self, actor):
#         if actor in self.__actors:
#             self.__actors.remove(actor)
#
#     def get_show_info(self):
#         return (f"Name: {self.__name}, platform: {self.__platform}, year: {self.__release_year}, episode:"
#                 f"{self.__current_episode}, rating: {self.__rating}, actors: {', '.join(self.__actors)}")
#
#
# show = MyShows("Breaking Bad", "Netflix", 2008, 5, 9, ["Bryan Cranston", "Aaron Paul"])
#
# print(show.get_show_info())
# show.set_current_episode(6)
# show.set_rating(4)
# show.add_actor("Elon Musk")
# show.remove_actor("Elon Musk 2")
# print(show.get_show_info())


# ex 2
class Car:
    _id_init = 1

    def __init__(self):
        self.car_id = Car._id_init
        Car._id_init += 1


class ParkingLot:
    def __init__(self, texer):
        self.texer = texer
        self.parked = {}
        self.cash = 0

    def park(self, car):
        if len(self.parked) < self.texer:
            self.parked[car.car_id] = car
            print(f"Car {car.car_id} parked")
        else:
            print("Parking is full")

    def durs_gal(self, car):
        if car.car_id in self.parked:
            hours = int(input("Enter hours:"))
            summ = hours * 500
            self.cash += summ
            del self.parked[car.car_id]
            print(f"Gumary {summ} dram.")
        else:
            print("Car is not found")

    def tex_mnac(self):
        return self.texer - len(self.parked)

    def summa(self):
        return self.cash


c1 = Car()
c2 = Car()
c3 = Car()

parking_lot = ParkingLot(2)

parking_lot.park(c1)
parking_lot.park(c2)
parking_lot.park(c3)

print(f"Tex mnac : {parking_lot.tex_mnac()}")

parking_lot.durs_gal(c1)
print(f"Tex mnac : {parking_lot.tex_mnac()}")

print(parking_lot.summa())
