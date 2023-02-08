#1 Create a function to calculate the average of an inputted list and that also calculates the average of an inputted tuple (handles both cases)

#2 create a function that outputs the max, min, and median of a given list


import statistics as stats

class SummerTemps:
    def __init__(self, temps_dict):
        self.temps_dict = temps_dict
        self.daily_lows = [temp[0] for temp in temps_dict.values()]
        self.daily_highs = [temp[1] for temp in temps_dict.values()]

    def mean_daily_low(self):
        return sum(self.daily_lows) / len(self.daily_lows)

    def mode_daily_low(self):
        try:
            return stats.mode(self.daily_lows)
        except stats.StatisticsError:
            return None

    def median_daily_low(self):
        return stats.median(self.daily_lows)

    def mean_daily_high(self):
        return sum(self.daily_highs) / len(self.daily_highs)

    def mode_daily_high(self):
        try:
            return stats.mode(self.daily_highs)
        except stats.StatisticsError:
            return None

    def median_daily_high(self):
        return stats.median(self.daily_highs)

    def daily_temp_diff(self):
        return [high - low for high, low in zip(self.daily_highs, self.daily_lows)]

    def mean_daily_temp_diff(self):
        return sum(self.daily_temp_diff()) / len(self.daily_temp_diff())

summer_temps = {'2020-04-01': [72,83], '2020-04-02': [64,72], '2020-04-03': [66,69], '2020-04-04': [70,88], '2020-04-05': [75,79], '2020-04-06': [71,80], '2020-04-07': [68,74], '2020-04-08': [69,76], '2020-04-09': [62,80], '2020-04-10': [71,84], '2020-04-11': [70,88], '2020-04-12': [65,73], '2020-04-13': [67,85], '2020-04-14': [76,89], '2020-04-15': [74,88]}

summer_temps_obj = SummerTemps(summer_temps)

print("Mean daily low: ", summer_temps_obj.mean_daily_low())
print("Mode daily low: ", summer_temps_obj.mode_daily_low())
print("Median daily low: ", summer_temps_obj.median_daily_low())
print("\nMean daily high: ", summer_temps_obj.mean_daily_high())
print("Mode daily high: ", summer_temps_obj.mode_daily_high())
print("Median daily high: ", summer_temps_obj.median_daily_high())
print("\nDaily temperature difference: ", summer_temps_obj.daily_temp_diff())
print("\nMean daily temperature difference", summer_temps_obj.mean_daily_temp_diff())
