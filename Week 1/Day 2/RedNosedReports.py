def is_only_increase_or_decrease(levels):
    i = 1
    increase = 0
    decrease = 0
    while i < len(levels):
        if levels[i-1] < levels[i]:
            increase += 1
        elif levels[i-1] > levels[i]:
            decrease += 1
        i += 1
    if decrease > 0 and increase > 0:
        return False
    else:
        return True

def is_jump_safe(level1, level2):
    jump_distance = abs(level1 - level2)
    if jump_distance > 3 or jump_distance == 0:
        return False
    else:
        return True

def is_all_safe_jumps(levels):
    i = 1
    unsafe_jumps = 0
    while i < len(levels):
        if not(is_jump_safe(levels[i-1], levels[i])):
            unsafe_jumps += 1
        i += 1
    if(unsafe_jumps > 0):
        return False
    else:
        return True

def is_safe(line):
    levels = [int(level.strip()) for level in line.split()]
    if is_only_increase_or_decrease(levels) and is_all_safe_jumps(levels):
        return True
    else:
        return False

result = 0

with open("input", "r") as file:
    for line in file:
        if (is_safe(line)):
            result += 1
print(result)