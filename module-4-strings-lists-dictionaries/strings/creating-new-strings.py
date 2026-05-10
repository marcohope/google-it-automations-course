# message = "A kong string with a silly typo"
# message[2] = "l"
# #This will throw an error

# message = "A kong string with a silly typo"
# new_message = message[0:2] + "l" + message[3:]
# print(new_message)

# message = "This is a new message"
# print(message)
# message = "And another one"
# print(message)

pets="Cats & Dogs"
pets.index("&")
# pets.index("C")
# pets.index("Dog")
# pets.index("s")

# pets="Cats & Dogs"
# pets.index("x")
# #This will throw an error

# pets="Cats & Dogs"
# "Dragons" in pets
# "Cats" in pets

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email