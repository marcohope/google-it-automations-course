file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}

# for extension, amount in file_counts.items():
#     print("There are {} files in {}.".format(amount, extension)) 

# print(file_counts.items()) ## key value pairs
# print(file_counts.keys()) ## keys
# print(file_counts.values()) ## values

for value in file_counts.values():
    print(value)


def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))