//プロジェクト固有のjsファイル

function action_openTaskManagement() {
    window.open('https://tnroot01.pythonanywhere.com/TaskManagement/', '_blank');
}

//ユーザ登録
function userTork() {
    document.getElementById('form').action = "{% url 'teachersapp:signUp' %}";
    document.getElementById('form').submit();
}
