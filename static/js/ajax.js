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

    function getReplacedUrl(pre_url, before_text, after_text) {
        let splited_url = pre_url.split('/');
        let post_url = '';
        for (var i = 1; i < splited_url.length; i++) {
            if (splited_url[i] == before_text) {
                splited_url[i] = after_text;
            }
            post_url =  post_url + '/' + splited_url[i];
        }
        return post_url;
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
                if (res['is_liked']){
                    el.attr('data-action-url', getReplacedUrl(action_url, 'like', 'unlike'));
                }else{
                    el.attr('data-action-url', getReplacedUrl(action_url, 'unlike', 'like'));
                }
            }
        );
    });
});
