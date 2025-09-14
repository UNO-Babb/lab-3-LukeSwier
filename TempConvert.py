#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter Tempeture in Fahrenheit ")

  tempCintial = (float(tempF) - 32 ) * (5 / 9 )
  tempCfinal = round(tempCintial , 2)


  print(tempF, "is ", tempCfinal, "degrees celsius.")
if __name__ == '__main__':
  main()
