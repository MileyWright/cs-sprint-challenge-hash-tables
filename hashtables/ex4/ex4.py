def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    hash_table = {} #hash table
    result = []     #results


    for i in a:
        hash_table[i] = i         # for each i in a
        if i != 0 and -i in hash_table: # if i is not 0 and -i in hash_table, then
            print(i)              # print i
            result.append(abs(i)) # append absolute value of i

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
