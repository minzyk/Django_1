from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])    # get을 받을때마다 pk를 확인해서 user가 request로 받은 user랑 동일한지 아닌지 확인하는 decorator 생성
        if not profile.user == request.user:
            return HttpResponseForbidden     # 동일하지 않을 경우레 forbudden으로
        return func(request, *args, **kwargs)   # 동일할 경우에는 내용 그대로 return
    return decorated