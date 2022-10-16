# NumberLine.py
import NumberLine

tests = []
tests[0] = NumberLine()

tests[1] = NumberLine(1.0)

tests[2] = NumberLine(0.0, 5.0, 1.0, 2.5)

tests[3] = NumberLine(0.0, 5.0, 1.0, -10.0, False, 10.0, False, 2.5)

tests[4] = NumberLine(0.0, 5.0, 1.0, -10.0, False, 10.0, False, 2.0, 2.5)

tests[5] = NumberLine()
tests[5] = tests[5].origin(1.5)
tests[5] = tests[5].major_display_tick_period(10.0)
tests[5] = tests[5].major_display_tick_period(2.0)
tests[5] = tests[5].min_limit(True)
tests[5] = tests[5].min(-15.0)
tests[5] = tests[5].max_limit(True)
tests[5] = tests[5].max(15.0)
tests[5] = tests[5].period(5.0)
tests[5] = tests[5].value(6.0)

print(tests[5].full_value())
print(tests[5].value())
print(tests[5].revolutions())
