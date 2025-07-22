#given string is ARTICLE Now generate the all possible arrangements of this string
import itertools

def generate_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]  
if __name__ == "__main__":
    input_string = "ARTICLE"
    permutations = generate_permutations(input_string)
    print(f"Total permutations of '{input_string}': {len(permutations)}")
    for perm in permutations:
        print(perm)
              
