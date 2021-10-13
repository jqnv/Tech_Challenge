class DataCapture():
    get_stats = {"capture": [], "stats": [], "build_stats": {"less": 0, "between": 0, "greater": 0}}
    """
    Class DataCapture contains the attribute get_stats, a dictionary containing:
     - The first element is a list named "capture" as the key, and a user input 
       list of integers to be evaluated to get stats.
    - The second element is a list named "stats" as the key and a list of integers provided
      by the user to determine what are the parameters to evaluate the list of integers of first element.
    - The third element is a dictionary named "build_stats" which contains three elements:
      - First element have the key "less" and the value is the amount of numbers in the list provided
        which are less than the first value provided.
      - Second element have the key "between" and the value is the amount of numbers in the list provided
        which are between the second and third parameter provided by the user.
      - Third element have the key "greater" and the value is the amount of numbers in the list provided
        which are greater than the fourth parameter provided by the user.

    """

    def add(self):
        """
        Function add() get the list of integers from the user input and store it into the first element
        of the dictionary get_stats. The function will add a new element converted to integer until the
        user hit enter, ending the loop.
        :return:
        The list with the key "capture" within the dictionary get_stats

        """
        while True:
            i = (input("Please enter a digit to be added to the list or hit enter to end the list "))
            if i == "": break
            self.get_stats["capture"].append(int(i))
        return self.get_stats

    def get_param(self):
        """
        Function get_param() get the parameters for the stats calculated by the class DataCapture, parameters obtained
        by user input are how the integers list will be evaluated: less(1 parameter), between(2 parameters), greater(1 parameter)
        all parameters are integers.
        :return:
        A list of 4 integers with the parameters to evaluate the "capture" list
        """
        self.get_stats["stats"].append(
            int(input("Thank you!\nNow, please type the parameter for the less than stat: ")))
        self.get_stats["stats"].append(int(input("Please type the first parameter for the between stat: ")))
        self.get_stats["stats"].append(int(input("Please type the second parameter for the between stat: ")))
        self.get_stats["stats"].append(int(input("Please type the parameter for the greater stat: ")))
        return self.get_stats

    def build_stats(self):
        """
        Function build_stats() contain the attribute capture_build, the list of integer sorted in ascending order,
        and three functions to calculate the stats.
        :return:
        The dictionary get_stats containing al the necessary information to run the program.

        """
        capture_build = sorted(self.get_stats["capture"])

        def less_stat():
            """
            Function less_stats() calculate how many numbers in the capture list are less than the parameter
            captured in the command line as the less than parameter.
            :return:
            The amount of numbers less than the "less" parameter, updated in the value for the "less" key

            """
            for i in capture_build:
                if i < self.get_stats["stats"][0]: self.get_stats["build_stats"]["less"] += 1

        less_stat()

        def between_stat():
            """
            Function between_stats() calculate how many numbers in the capture list are between the parameters
            captured in the command line as the between parameters.
            :return:
            The amount of numbers between the parameters provided, updated in the value for the "between" key

            """
            for i in capture_build:
                if self.get_stats["stats"][1] <= i <= self.get_stats["stats"][2]: self.get_stats["build_stats"][
                    "between"] += 1

        between_stat()

        def greater_stat():
            """
            Function greater_stats() calculate how many numbers in the capture list are greater than the parameter
            captured in the command line as the greater than parameter.
            The "captured" list have been inverted in order to reduce the amount of
            :return:
            The amount of numbers greater than the "greater" parameter, updated in the value for the "greater" key

            """
            capture_inv = self.get_stats["capture"][::-1]
            for i in capture_inv:
                if i > self.get_stats["stats"][3]: self.get_stats["build_stats"]["greater"] += 1

        greater_stat()

        return self.get_stats


if __name__ == '__main__':
    """
    Creates an instance of the class DataCapture, providing a welcome message and the explanation of what
    will be obtained at the end of the program.
    Call the add() function storing the return to my_list variable.
    Call the get_param() function.
    Get the parameters provided by the user storing it in the variable my_stats.
    Call the build_stats() function storing the information in the my build_stats dictionary.
    Print the list entered by the user in the original order.
    Print the amount of numbers in the list which fall under the parameters provied by the user.

    """
    capture = DataCapture()
    print("\tWelcome to the system able to capture a list of numbers and set the parameters to "
          "determine:\n", "=" * 97, "\n- How many numbers on the list are less than a determined number, \n"
                                    "- How many numbers are between two determined numbers \n"
                                    "- How many numbers are greater then a determined number\n")
    my_list = capture.add()
    capture.get_param()
    my_stats = DataCapture().get_stats["stats"]
    my_build_stats = capture.build_stats()

    # Print on the screen the stats provided as parameters
    print(f"\n*****************************\nOriginal Capture: ", my_list["capture"])
    print(f"Amount of numbers in the list Less than ", my_stats[0], " are ", my_build_stats["build_stats"]["less"])
    print(f"Amount of numbers in the list Between ", my_stats[1], " and ", my_stats[2], " are ",
          my_build_stats["build_stats"]["between"])
    print(f"Amount of numbers in the list Greater than ", my_stats[3], " are ",
          my_build_stats["build_stats"]["greater"])