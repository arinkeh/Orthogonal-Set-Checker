"""
A project by Haleemat Oloyo
Completed on 8/5/2026

~ Definition of orthogonal set of vectors:
A set of nonzero vectors {u1, u2, ..., um} is called orthogonal if ui • uj = 0 whenever i!=j. 
Essentially, this means that the dot product of any two vectors in the set is zero.

~ Workplan
* Collect each vector (space-delimited numbers) through an input function. 
* Create a set of vectors using the inputs.
* Using the combination function, create pairs of vectors.
* Check the dot product of each pair of vectors.
* Create a list to store the dot products if they are not zero.
* Use an if/else block to check the list has any values
* If the list is empty, the set is orthogonal; otherwise, it is not.
"""

def check_set(v_set):
    from itertools import combinations

    count = 0

    for i in v_set:
        if len(i) != len(v_set[0]):
            count += 1

        else:
            continue

    if count == 0:
        pairs = list(combinations(v_set, 2))
        sums = []

        for pair in pairs:
            sum = 0

            for p in range(len(pair[0])):
                sum += pair[0][p] * pair[1][p]

            if sum != 0:
                sums.append(sum)

        if v_set:
            print ("\033[1mThis is an orthogonal set of vectors.\033[0m") if not sums else print("\033[1mThis is not an orthogonal set of vectors.\033[0m")

    else:
        print ("\033[1mThis set is not orthogonal because the vectors are not of equal length.\n  Please enter vectors of equal length.\033[0m")
        
def get_set():
    import time

    display = """\033[1mSeperate each entry in a vector by a space. e.g., 1 2 3 4 5 6\n  Enter 'done' after all vectors in the set have been entered\033[0m\n"""
    print (display)

    orthoset = []

    while True:
        user_input = (input("\033[1mPlease enter a vector to check for orthogonality: \033[0m")).strip()

        if user_input == "":
            print("\t\033[3mInput cannot be empty, please enter a vector.\033[0m")

        elif any(k.isalpha() for k in user_input.split(" ")) and user_input != "done":
            print ("\t\033[3mPlease enter only numbers, no words except 'done'\033[0m")

        elif user_input != "done":
            vector = [float(i) if "." in i else int(i) for i in user_input.split(" ")]
            orthoset.append(vector)
        
        else:
            break

    if not orthoset:
        print("\t\033[3mYou have not entered any vectors. Please rerun program.\033[0m")
        
    else:
        print(f"\t\033[3mYou have entered this set of vectors: {orthoset}\033[0m")
        time.sleep(1)
        print("\t\t\033[3mChecking for orthogonality...\033[0m")
        time.sleep(2)

    return orthoset


check_set(get_set())


