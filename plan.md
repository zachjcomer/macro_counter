# manager
routines

+ createRoutine()
+ deleteRoutine()
+ moveRoutine(i, j)
+ runRoutine(i)

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
