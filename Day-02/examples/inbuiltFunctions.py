text = "DevOps"
print(len(text))   # 6

text = "devops"
print(text.upper())   # DEVOPS

text = "PYTHON"
print(text.lower())   # python

text = "  hello world  "
print(text.strip())   # "hello world"
print(text.lstrip())
print(text.rstrip())

text = "I love Docker"
print(text.replace("Docker", "Kubernetes"))
# I love Kubernetes

text = "apple,banana,orange"
print(text.split(","))
# ['apple', 'banana', 'orange']

items = ["CI", "CD", "DevOps"]
print(" - ".join(items))
# CI - CD - DevOps

text = "Kubernetes"
print(text.find("net"))   # 4

text = "deploy.sh"
print(text.startswith("deploy"))  # True
print(text.endswith(".sh"))       # True

text = "error error warning"
print(text.count("error"))   # 2

text = "DevOps"
print(text.isalpha())   # True

text = "12345"
print(text.isdigit())   # True

text = "DevOps123"
print(text.isalnum())   # True

text = "python"
print(text.capitalize())   # Python

text = "devops engineer role"
print(text.title())
# Devops Engineer Role

role = "DevOps"
exp = 10
print("{} engineer with {} years experience".format(role, exp))

print(f"Next year exp: {exp + 1}")

print("{} engineer with {} years experience".format("DevOps", 10))

print("{role} engineer with {exp} years experience".format(
    role="DevOps", exp=10
))


log = "  ERROR: Disk Full  "
clean_log = log.strip().lower()
print(clean_log)
# error: disk full
