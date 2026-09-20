# Question 2 (d)
# The two blanks in the original code are:  global  and  +

call_count = 0

def track_call():
    global call_count
    call_count = call_count + 1
    print("Called", call_count, "times")

track_call()      # Called 1 times
track_call()      # Called 2 times

# Without the global keyword, Python treats call_count as a local variable
# for the whole function body. The expression call_count + 1 then reads a
# local that has no value yet, so the first call raises UnboundLocalError
# and no output is produced.
