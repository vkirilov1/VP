class InvalidParameterError(Exception):
    pass


class NutrientError(Exception):
    pass


class InvalidFoodError(Exception):
    pass


class Food:
    def __init__(self, carbs, protein, fats, salt, has_error=False):
        try:
            self.carbs = carbs
            self.protein = protein
            self.fats = fats
            self.salt = salt
            self.has_error = False

            if carbs == 0 and protein == 0 and fats == 0 and salt == 0:
                raise InvalidFoodError

            if type(carbs) != float:
                raise InvalidParameterError

            elif type(protein) != float:
                raise InvalidParameterError

            elif type(fats) != float:
                raise InvalidParameterError

            elif type(salt) != float:
                raise InvalidParameterError

            if carbs + protein + fats + salt > 100:
                raise NutrientError

        except InvalidParameterError:
            print("Macronutrients must be float!")
            self.has_error = True

        except NutrientError:
            print("The total sum of the macronutrients shouldn't exceed 100!")
            self.has_error = True

        except InvalidFoodError:
            print("All macronutrients can't be 0!")
            self.has_error = True

    def print_label(self):
        print(
            f"{self.__class__.__name__} info - (Carbs:{self.carbs}, Protein:{self.protein}, Fats:{self.fats}, Salt:{self.salt})")


for i in range(0, 120, 10):
    current_food = Food(5.2 + i, 1.2 + i, 4.1 + i, 0.1 + i)
    if current_food.has_error:
        continue
    current_food.print_label()
