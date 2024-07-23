$(document).ready(function(){

    $('.add-to-selection').on('click', function(){
        let room_id = $(this).attr("data-index");
        
        let hotel_id = $('.hotel-id').val()
        let hotel_name= $('.hotel-name').val()
        let room_type= $('.room-type').val()

        let room_price= $('.room-price').val() 
        let room_num = $('.room-num').val() 
        let room_view= $('.room-view').val()
        let num_of_beds= $('.beds-num').val()

        let checkin = $('.checkin').val()
        let checkout = $('.checkout').val() 
        let adults = $('.adults').val()
        let children = $('.children').val() 

        $.ajax({
            url: '/booking/room_selection/',
            data : {
                'hotel_id' : hotel_id,
                'hotel_name' : hotel_name,
                'room_id' : room_id,
                'room_type' : room_type,
                'room_price' : room_price,
                'room_num' : room_num,
                'room_view' : room_view,
                'num_of_beds' : num_of_beds,
                'checkin' : checkin,
                'checkout' : checkout,
                'adults' : adults,
                'children' : children,
            },
            dataType : 'json',
            beforeSend : function() {
                console.log('sending data ......');
            },
            success : function(responce){
                console.log(responce);
            }
        })
    })
})

$(document).on('click', '.delete-room', function(){
    let room_id = $(this).attr('data-item')
    let button = $(this)

    $.ajax({
        url: '/booking/delete_room_from_session/',
        data:{
            'room_id':room_id
        },
        dataType: 'json',
        beforeSend: function(){
            console.log('deleteing...');
            button.html('<i class="fas fa-spinner fa-spin"></i>')
        },
        success: function(res){
            if (res.rooms_len == 0) {
                console.log('in ajax if');
                $('.rooms-booked').html('<h1>You have deleted all your booked rooms</h1>');
                setTimeout(function() {
                    window.location.href = '/booking/selected_rooms/'; // Redirect to another page
                }, 3000); // Wait for 3 seconds (3000 milliseconds)
            } else {
                $('.rooms-booked').html(res.rendered_data);
            }
                
        },
        erorr: function(res){
            console.log('server error');
        }
    })
})