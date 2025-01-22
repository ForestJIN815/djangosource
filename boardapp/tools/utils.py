# 사용자 ip 추출 함수
def get_client_ip(request):
    ip = request.META.get("REMOTE_ADDR")
    return ip
