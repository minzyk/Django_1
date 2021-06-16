from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True     # username 을 비활성화 시킨것 (정보수정 할 경우에 ID 는 수정하지 못하도록) - disabled를 true로 바꿔주면 수정을 해도 서버에 반영이 되지 않는다
