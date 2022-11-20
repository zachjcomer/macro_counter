# workouts (main)
routines

+ chooseRoutine(int) -> routine
+ runRoutine(routine)

# routine
name
blocks

+ setName(string)
+ getName() -> string

+ run()
+ addBlock() -> self
+ delBlock() -> self
+ moveBlock() -> self

# block (Builder)
timer
action

+ run()

+ setTimer(timer)
+ setAction(action)
