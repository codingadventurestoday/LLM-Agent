from functions.get_files_info import get_files_info

test_1 = get_files_info("calculator", ".")
test_2 = get_files_info("calculator", "pkg")
test_3 = get_files_info("calculator", "/bin")
test_4 = get_files_info("calculator", "../")

print(test_1)
print("___________")
print(test_2)
print("___________")
print(test_3)
print("___________")
print(test_4)
print("___________")