# #import pytest

class DataCapture:
    capture = []
    stats = []
    count = 0

    def add(self):
        capture = self.capture
        while True:
            i = (input("Please enter a digit to be added to the list or hit enter to end the list "))
            if i == "": break
            self.capture.append(int(i))
            print(f"Hey", len(self.capture))
            print(self.capture)
        return self.capture

    def get_param(self):
        # Gathering parameters for stats calculations
        self.stats.append(int(input("Thank you!\nNow, please type the parameter for the less than stat: ")))
        self.stats.append(int(input("Please type the first parameter for the between stat: ")))
        self.stats.append(int(input("Please type the second parameter for the between stat: ")))
        self.stats.append(int(input("Please type the parameter for the greater stat: ")))
        return self.stats

    def build_stats(self):
        capture = sorted(self.capture)

        def less_stat():
            # Getting the amount of numbers less than stats
            count = 0
            for i in capture:
                if i < self.stats[0]:
                    count += 1
                else:
                    break
            return count

        def between_stat():
            # Getting the amount of numbers between two provided parameters
            count = 0
            for i in self.capture:
                if self.stats[1] <= i <= self.stats[2]:
                    count += 1
                else:
                    break
            return count

        def greater_stat():
            # Getting the amount of numbers for less than stats
            count = 0
            capture_inv = self.capture[::-1]
            for i in capture_inv:
                if i > self.stats[3]:
                    count += 1
                else:
                    break
            return count

        return less_stat(), between_stat(), greater_stat()


if __name__ == '__main__':
    capture = DataCapture()
    print("\tWelcome to the system able to capture a list of numbers and set the parameters to "
          "determine:\n","="*97,"\n- How many numbers on the list are less than a determined number, \n"
          "- How many numbers are between two determined numbers \n"
          "- How many numbers are greater then a determined number\n")
    my_list = capture.add()
    my_param = capture.get_param()
    less, between, greater = capture.build_stats()
    # sorted(my_list)
    # Print on the screen the stats provided as parameters
    print(f"\n*****************************\nOriginal Capture: ", my_list)
    print(f"Amount of numbers in the list Less than ", my_param[0], " are ", less)
    print(f"Amount of numbers in the list Between ", my_param[1], " and ", my_param[2], " are ", between)
    print(f"Amount of numbers in the list Greater than ", my_param[3], " are ", greater)
