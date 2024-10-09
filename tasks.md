- fix sending email to gmail error

1- add user_type(seller-user):
    - when user is created if he is a seller create to him a hotel
    - each seller can have only one hotel and can only update it and can't delete it 
    - remove creating a hotel from api 

2- update room_type api view
    - each seller can create a room_type and update, delete it 
    - each seller can change the avillability of a room 