BEGIN MAIN
   continue = true
   WHILE continue:
        choice = input("Do you want to Load the Array, Print the Array, Sum the array, Find the max of the array, find the min of the array")
        CASEWHERE choice is
        load: loadArray
     Print: printArray
     Sum: sumArray
     Max: maxArray
     Min: minArray
     Q: continue = False
     END CASEWHERE
     
     END WHILE
     
     END CASEWHERE
     END WHILE
     END MAIN PROGRAM

BEGIN loadArray

  runSubroutine = true
  WHILE runsubroutine:
      inputNum = input("Enter the number you wish to add or Q to return to main program")
      IF inputNum -- 