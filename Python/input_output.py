test_name = "login_validation"
status = "PASSED"
duration_ms = 1250

# Basic f-string
print(f"Test '{test_name}' {status} in {duration_ms} ms")
# Output: Test 'login_validation' PASSED in 1250 ms

# With format specifiers
print(f"Execution time: {duration_ms / 1000:.2f} seconds")
# Output: Execution time: 1.25 seconds



response_code = 404
print(f"{response_code}")
#output: 404
response_code = 404
print(f"{response_code=}")
# Output: response_code=404



print("Test {} finished with status {}".format("payment_test", "FAILED"))
#Test payment_test finished with status FAILED
print("{0} {1} {0}".format("FAILED", "retry"))
#FAILED retry FAILED


test_data = {"name": "data_driven_test", "iterations": 5}
print("Running {name} for {iterations} iterations".format(**test_data))
#Running data_driven_test for 5 iterations

for i in range(1, 4):
    print("{:<10} {:>5}".format(f"Test_{i}", i*100))
#Test_1       100
#Test_2       200
#Test_3       300

test_id = "TC001"
print(test_id.rjust(10))       # Right-justified in 10-char field
print(test_id.ljust(10, '-'))  # Left-justified with fill character
print(test_id.center(20))      # Centered

# Pad numbers with zeros
duration = "12"
print(duration.zfill(5))       # Output: 00012

#     TC001
#TC001-----
#       TC001        
#00012

with open('test_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)


with open('test_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        username, password, env, url = line.strip().split(',')
        print(username, password, env, url)
