import random


# Opens chromosome file
def open_file(file_name, character_limit=10000):
    with open(file_name, 'r') as f:
        return f.readlines()

# list of lists having indices of all blank spaces
# blank_idxs = []
# Hides random sequences of bases in the genome
def hide_random_sequence(genome, max_length=8):
    # number of times we should hide a sequence
    iters = int(len(genome) / 100)
    i = 0
    while (i < iters):
        flag = False
        # hide sequences of random length from 1 to max_length
        hidden_sequence_length = random.randint(3, max_length)
        # pick a random position and hide sequence starting from there
        start_index = random.randint(21, len(genome) - hidden_sequence_length - 21)
        new_genome = genome[:start_index]

        #creating a list with indices of all blank spaces in given iteration
        idxs = []
        for j in range(hidden_sequence_length):
            for space in blank_idxs:
                #checking to see if space is already a blank, if so, we will leave it be and start over with new random values
                if (start_index + j) in space:
                    flag = True
                    break
            if flag == True:
                break
            idxs.append(start_index + j)

        #starting over if blank spaces overlap
        if flag == True:
            i -= 1
            continue

        blank_idxs.append(idxs)

        # add blank spaces for hidden part
        for j in range(hidden_sequence_length):
            new_genome += ' '
        # add in everything else
        new_genome += genome[start_index + hidden_sequence_length:]
        genome = new_genome
        i += 1
    return genome


def missing_values_array(genome, new_genome):
    correct_values = []
    i = 0
    while(i < len(new_genome)):
        if new_genome[i] == ' ':
            blank_len = 0
            for j in range(i, len(new_genome)):
                if new_genome[j] == ' ':
                    blank_len += 1
                else:
                    break
            correct_values.append(genome[i:i+blank_len])
            i += blank_len
        i += 1
    return correct_values
