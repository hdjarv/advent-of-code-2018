print("Advent of Code 2018 - Day 1")

def read_file_into_int_list(name):
  input_file = open(name)

  indata = input_file.read();
  indata = indata.splitlines()
  ix=0
  while ix < len(indata):
    indata[ix] = int(indata[ix])
    ix += 1

  input_file.close()
  return indata

indata = read_file_into_int_list("aoc-01-input.txt")

# Below the message, the device shows a sequence of changes in frequency (your puzzle input). A value like +6 means the current frequency increases by 6; a value like -3 means the current frequency decreases by 3.

# For example, if the device displays frequency changes of +1, -2, +3, +1, then starting from a frequency of zero, the following changes would occur:

# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.
# In this example, the resulting frequency is 3.

# Here are other example situations:

# +1, +1, +1 results in  3
# +1, +1, -2 results in  0
# -1, -2, -3 results in -6
# Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?

print ("Part 1");
sum = 0
for value in indata:
  sum += value

print("The answer is: {0}".format(sum))

# 536 is the right answer



# --- Part Two ---

# You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

# For example, using the same list of changes above, the device would loop as follows:

# Current frequency  0, change of +1; resulting frequency  1.
# Current frequency  1, change of -2; resulting frequency -1.
# Current frequency -1, change of +3; resulting frequency  2.
# Current frequency  2, change of +1; resulting frequency  3.
# (At this point, the device continues from the start of the list.)
# Current frequency  3, change of +1; resulting frequency  4.
# Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
# In this example, the first frequency reached twice is 2. Note that your device might need to repeat its list of frequency changes many times before a duplicate frequency is found, and that duplicates might be found while in the middle of processing the list.

# Here are other examples:

# +1, -1 first reaches 0 twice.
# +3, +3, +4, -2, -4 first reaches 10 twice.
# -6, +3, +8, +5, -6 first reaches 5 twice.
# +7, +7, -2, -7, -4 first reaches 14 twice.
# What is the first frequency your device reaches twice?

print("Part 2")

currentFrequency = 0
table = {}
result = None
while(result is None):
  for value in indata:
    currentFrequency += value
    if currentFrequency in table:
      result = currentFrequency
      break
    table[currentFrequency] = 1

print("The answer is: {0}".format(result))

# 75108 is the right answer
