#Exercise 5: Change Guest List, 

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