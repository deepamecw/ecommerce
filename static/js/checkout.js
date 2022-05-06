$(document).ready(function () {

    $('.paywithrazorpay').click(function (e) { 
        e.preventDefault();

        var fname=$("[name='fname']").val();
        var lname=$("[name='lname']").val();
        var email=$("[name='email']").val();
        var phone=$("[name='phone']").val();
        var address=$("[name='address']").val();
        var city=$("[name='city']").val();
        var state=$("[name='state']").val();
        var country=$("[name='country']").val();
        var pincode=$("[name='pincode']").val();
        var token=$('input[name=csrfmiddlewaretoken]').val();

        if (fname == "" || lname == "" || email == "" || phone == "" || address == "" || city =="" || state == "" || country == "" || pincode == "")   
        {
            
            swal("Alert!", "All Fields are Mandatory!", "error");
            return false;
        }
        else
        {
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                data:{
                    csrfmiddlewaretoken: token
                },
                success: function (response) {
                    //console.log(response);
                    var options = {
                        "key": "rzp_test_2hSRxGQdiskqxt",  //Enter the Key ID generated from the Dashboard
                        "amount": 1*100,// response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Deepa coder",
                        "description": "Thank you for shopping with us",
                        "image": "https:example.com/your_logo",
                        //"order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data = {
                                "fname" : fname,
                                "lname" : lname,
                                "email" : email,
                                "phone" : phone,
                                "address" :address,
                                "city" :city,
                                "state": state,
                                "country": country,
                                "pincode": pincode,
                                "token": token,
                                "payment_mode": 'Paid by Razorpay',
                                "payment_id":responseb.razorpay_payment_id,
                                 csrfmiddlewaretoken: token

                            }
                            $.ajax({
                                method: "POST", 
                                url: "/place-order",
                                data: data,
                                success: function (responsec) {
                                    swal("Congratulations!", responsec.status, "success").then((value) => {
                                        window.location.href = '/my-orders'
                                      });
                                }
                            });
                           //alert(response.razorpay_order_id);
                           // alert(response.razorpay_signature)
                        },
                        "prefill": {
                            "name": fname +" "+ lname,
                            "email": email,
                            "contact": phone
                        },
                        //"notes": {
                            //"address": "Razorpay Corporate Office"
                        //},
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                  
                    rzp1.open();
                }
            });
              
            
        }
    


        
    });
});