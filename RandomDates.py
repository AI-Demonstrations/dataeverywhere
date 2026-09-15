# Python3 code to demonstrate working of
# Random K dates in Range
# Using choices() + timedelta() + loop
from datetime import date, timedelta
from random import choices

class RandomDates:
    def __init__(self, test_date1, test_date2):
        self.test_date1 = test_date1
        self.test_date2 = test_date2
    
 
    # initializing dates ranges 
    #test_date1, test_date2 = date(2024, 9, 1), date(2024, 12, 31)
    def makeRandomDates(self):
        # printing dates 
        #print("The original range : " + str(self.test_date1) + " " + str(self.test_date2))

        # initializing K
        K = 1000

        self.res_dates = [self.test_date1]

        # loop to get each date till end date
        while self.test_date1 != self.test_date2:
            self.test_date1 += timedelta(days=1)
            self.res_dates.append(self.test_date1)

        # random K dates from pack
        resO = choices(self.res_dates, k=K)
        return resO
    
    def selectRandomDate(self):
        return choices(self.res_dates, k=1)
        
if __name__ == "__main__":
    r = RandomDates(date(2024, 9, 1),date(2024, 12, 31))
    r.makeRandomDates()
    print (r.selectRandomDate()[0])
    print(type(r.selectRandomDate()))
