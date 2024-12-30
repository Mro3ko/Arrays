meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

def day_meal_plan(meal_plan, day_number):
   result=weekday(day_number)+": "
   for day in meal_plan[day_number-1]:
      result+=day+", "
   return result[0:-2]

print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for i in range(1,8):
    print(day_meal_plan(meal_plan, i))