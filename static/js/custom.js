$(document).ready(function(){

    $('.add-to-selection').on('click', function(){
        let room_id = $(this).attr("data-index");
        
        let hotel_id = $('.hotel-id').val()
        let hotel_name= $('.hotel-name').val()
        let room_type= $('.room-type').val()

        let room_price= $('.room-price').val() 
        let room_num = $('.room-num').val() 
        let room_view= $('.room-view').val()
        let num_of_bed= $('.beds-num').val()

        let checkin = $('.checkin').val()
        let checkout = $('.checkout').val() 
        let adults = $('.adults').val()
        let children = $('.children').val() 

        console.log(room_id);
        console.log(hotel_id);
        console.log(hotel_name);
        console.log(room_type);

        console.log(room_price);
        console.log(room_num);
        console.log(room_view);
        console.log(num_of_bed);

        console.log(checkin);
        console.log(checkout);
        console.log(adults);
        console.log(children);
    })
})