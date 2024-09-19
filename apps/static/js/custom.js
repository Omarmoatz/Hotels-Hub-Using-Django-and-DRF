$(document).ready(function(){

// ADD room to selection
    $('.add-to-selection').on('click', function(){
        let button = $(this)
        let room_id = button.attr("data-index");
        
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
                
               button.html('<i class="fas fa-spinner fa-spin"></i> Processing')     
            },
            success : function(res){

                setTimeout(function() {
                    button.html('<i class="fa fa-check "></i> Added'); 
                    console.log(res.rooms_len);
                    $('.rooms-len').html(res.rooms_len)
                 }, 1000);
                
            }
        })
    })
})


// delete a booked room rom selection
$(document).on('click', '.delete-room', function(){
    let room_id = $(this).attr('data-item')
    let button = $(this)

    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
          confirmButton: "btn btn-success",
          cancelButton: "btn btn-danger"
        },
        buttonsStyling: false
      });

      swalWithBootstrapButtons.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, cancel!",
        reverseButtons: true
      }).then((result) => {
        if (result.isConfirmed) {
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
                        $('.rooms-booked').html(`<div class="text-center wow fadeInUp" data-wow-delay="0.1s">
                                                    <h1 class="my-5 fs-3">you deleted all your booked rooms 
                                                    <span class="text-primary text-uppercase"> you will be redirected to home page </span></h1>
                                                </div>`);
                        setTimeout(function() {
                            window.location.href = '/booking/selected_rooms/'; // Redirect to another page
                        }, 3000); // Wait for 3 seconds 
                    } else {
                        swalWithBootstrapButtons.fire({
                            title: "Deleted!",
                            text: "Your Booked Room has been deleted.",
                            icon: "success"
                          });
                        $('.rooms-booked').html(res.rendered_data);
                    }
                    $('.rooms-len').html(res.rooms_len)
                        
                },
                erorr: function(res){
                    console.log('server error');
                }
            })
          
        } else if (
          result.dismiss === Swal.DismissReason.cancel
        ) {
          swalWithBootstrapButtons.fire({
            title: "Cancelled",
            text: "Your Booked Room is safe :)",
            icon: "error"
          });
        }
      });

    
})


// check coupon 
$(document).on('submit', '#check-coupun', function(e){
    e.preventDefault()
    let coupon_code = $('#coupon-code').val()
    let booking_id = $('#booking-id').val()
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    let btn = $('#apply-coupon')

    $.ajax({
        url :'/booking/check_coupun/',
        method: 'POST',
        data :{
            'booking_id':booking_id,
            'coupon_code':coupon_code,
            'csrfToken':csrfToken
        },
        dataType: 'json',
        beforeSend: function(){

            console.log('applying.....');
            btn.html('<i class="fas fa-spinner fa-spin "></i>')
            

        },
        success: function(res){
            setTimeout(function(){
                console.log(res.status)
                if(res.status === 'success') {
                    Swal.fire({
                        icon: 'success',
                        title: res.message,
                        timer: 2000,
                    });

                    btn.html('<i class="fa fa-check"></i>')
                    $('#booking-summery').html(res.html)

                } else {
                    Swal.fire({
                        icon: 'error',
                        title: res.message,
                        timer: 2000,
                    });
                    btn.html('Apply')
                }
                          
            },1000)
            
            
        }
    })

})
