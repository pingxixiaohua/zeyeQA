// alert("register.js")
function bindEmailCaptchaClick(){
    $("#captcha-btn").click(function (event) {
        let $this = $(this);
        // 阻止默认时间
        event.preventDefault();
        // $("#exampleInputEmail1")
        var email = $("input[name='email']").val();
        // alert(email)
        $.ajax({
            url: "/auth/cpatcha/email?email="+email,
            method: "GET",
            success: function (result){
                var code = result['code']
                if(code==200){
                    let countdown = 60;
                    $this.off("click");
                    let timer = setInterval(function () {
                        $this.text(countdown);
                        countdown -=1;
                        console.log(countdown)
                        if (countdown <= 0) {
                            clearInterval(timer);
                            $this.text("获取验证码");
                            bindEmailCaptchaClick()
                        }
                    }, 1000)
                    // alert("发送成功")
                }else {
                    alert(result['message'])
                }
            },
            fail: function (error) {
                console.log(error);
            }
        })
    })
}
$(function (){
    bindEmailCaptchaClick()
})



