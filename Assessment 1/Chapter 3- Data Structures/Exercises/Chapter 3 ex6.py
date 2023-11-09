# Exercise 6: Shrinking Guest List,

# List of people whom are to be invited to dinner
Guest_invitation_list=["Anas","Awais","Mehran","Ali","Omar","Shahab", "Tayyab", "Asad"]

# Printing the name of person who is not able to join
print(Guest_invitation_list[2],"will not be able to join the dinner party due to an emergency")

# replacing the name of the guest who won't be coming to the dinner with the person who is coming to the party
Guest_invitation_list.remove(Guest_invitation_list[2])
Guest_invitation_list.insert(2,"Shamir")
# Sending new invitations for dinner
for person in Guest_invitation_list:
    print("Dear",person,"you are invited to a dinner party at my newly opened resturant. It will be a great honour having you at the party. Please join for a wonderful evening.")
# Printing a message that we can only invite two people for dinner
print("\nUnfortunately, the dinner table won't be there in time, and therefore we can only accommodate two people for dinner.\n")
# Using pop() function to remove guests until only two guests remain
while len(Guest_invitation_list) > 2:
    removed_person = Guest_invitation_list.pop()
    print("My apologies dear,",removed_person+'.',"This time we can't invite you to the dinner.")
print("\n")
# Sending dinner invitations to the remaining guests which are two
for person in Guest_invitation_list:
    print("Dear", person+',', "despite of all the issues encountered so far, you are still invited to dinner. It will be a great honour having you at the party. Please join for a wonderful evening")
#To remove the last two names function del is being used
del Guest_invitation_list[:]
# Printing the list to ensure it's empty
print("\nThe guest list is empty now:",Guest_invitation_list)
