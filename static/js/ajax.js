$(function(){
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Like function
    $("[data-action='like']").on('click', function(e){
        e.preventDefault();
        const action_url = $(this).attr('data-action-url');
        const csrftoken = getCookie('csrftoken');
        const el = $(this);
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: 'POST',
            url: action_url,
            dataType: 'json'
        })
        .done(
            function (res) {
                el.children('i').toggleClass('text-danger fas far');
                el.children('span').text(res['likes_num']);
            }
        );
    });
});