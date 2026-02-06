def run_sectorization(V, A, C):
    b = len(V)
    B = [1]*b
    iteration = 2

    for i in range(b):
        if V[i] > C:
            B[i] = -2

    iteration = define_single_regions(B, iteration)
    define_regions(V, B, A, C, iteration)
    
def define_regions(V, B, A, C, iteration):
    reset_districts(B)

    while not_finished(B):
        build_region(V, B, A, C, iteration)
        define_regions(V, B, A, C, iteration + 1)

def define_single_regions(B, iteration):
    for i in range(len(B)):
        if B[i] == -2:
            print("Region", iteration-1, "District", i)
            B[i] = -3
            iteration += 1
    return iteration

def build_region(V, B, A, C, iteration):
    weight = select_global_max(B, V, iteration)

    while not_finished(B):
        chosen = select_adjacent_max(V, B, A, iteration)

        if chosen >= 0:
            if weight + V[chosen] <= C:
                B[chosen] = iteration
                weight += V[chosen]
                reset_districts(B)
            else:
                B[chosen] = 0

    print_region(B, iteration)
    
def reset_districts(B):
    for i in range(len(B)):
        if B[i] == 0 or B[i] == -1:
            B[i] = 1

def not_finished(B):
    return any(x == 1 for x in B)

def print_region(B, iteration):
    for i in range(len(B)):
        if B[i] == iteration or B[i] == -2:
            print("Region", iteration-1, "District", i)

def select_global_max(B, V, iteration):
    max_value = 0
    chosen = -1

    for i in range(len(B)):
        if B[i] == 1 and V[i] > max_value:
            max_value = V[i]
            chosen = i

    if chosen != -1:
        B[chosen] = iteration

    return max_value

def select_adjacent_max(V, B, A, iteration):
    max_value = 0
    chosen = -1

    for i in range(len(B)):
        if B[i] == 1:
            if is_adjacent(B, A, i, iteration):
                if V[i] > max_value:
                    max_value = V[i]
                    chosen = i
            else:
                B[i] = -1

    return chosen

def is_adjacent(B, A, i, iteration):
    for j in range(len(B)):
        if B[j] == iteration and A[i][j] == 1:
            return True
    return False


        