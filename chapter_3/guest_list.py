guest_list = ['dad', 'mum', 'reginald', 'dorothy', 'tom']
print(guest_list)

print(
    f"Hi {guest_list[0].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[1].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[2].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[3].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[4].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")

# Decided he can't make it
print(guest_list[3].title())

# New guest!
guest_list[3] = 'raymond'
print(guest_list)

print(
    f"Hi {guest_list[0].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[1].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[2].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[3].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[4].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")

print("Hey everyone! Christal and I found a bigger table!")

guest_list.insert(0, "paul")
guest_list.insert(3, "aileen")
guest_list.insert(8, "ron")

print(guest_list)
print(
    f"Hi {guest_list[0].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[1].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[2].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[3].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[4].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[5].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[6].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")
print(
    f"Hi {guest_list[7].title()}! You're invited to dinner with Adrian and Christal this weekend on Saturday! Come come!")

print("Can only invite two other people to dinner...")

uninvited_guest = guest_list.pop(0)
print(
    f"Sorry you can't come to dinner anymore {uninvited_guest.title()}! Maybe next time when the table arrives!")
uninvited_guest = guest_list.pop(2)
print(
    f"Sorry you can't come to dinner anymore {uninvited_guest.title()}! Maybe next time when the table arrives!")
uninvited_guest = guest_list.pop(2)
print(
    f"Sorry you can't come to dinner anymore {uninvited_guest.title()}! Maybe next time when the table arrives!")
uninvited_guest = guest_list.pop(2)
print(
    f"Sorry you can't come to dinner anymore {uninvited_guest.title()}! Maybe next time when the table arrives!")
uninvited_guest = guest_list.pop(2)
print(
    f"Sorry you can't come to dinner anymore {uninvited_guest.title()}! Maybe next time when the table arrives!")
uninvited_guest = guest_list.pop(2)
print(
    f"Sorry you can't come to dinner anymore {uninvited_guest.title()}! Maybe next time when the table arrives!")

print(f"Gret news {guest_list[0].title()}! Dinner is still on!")
print(f"Gret news {guest_list[1].title()}! Dinner is still on!")

del guest_list[0]
del guest_list[0]

print(guest_list)
