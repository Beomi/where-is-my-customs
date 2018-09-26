import json

from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import (
    KakaoUser,
    PackageQuery,
)
from .utils import (
    find_by_hbl,
)

from .message_templates import (
    HBL_MESSAGE_TEMPLATE,
)

FIND_BY_HBL = "HBL(송장번호)로 찾기"
FIND_BY_MBL = "MBL로 찾기"
FIND_BY_CRG = "화물관리번호로 찾기"

FIND_BUTTONS = [FIND_BY_HBL, FIND_BY_MBL, FIND_BY_CRG]

QUERY_BY_HBL = 'HBL 번호를 입력후 메시지를 전송해주세요.'

DEFAULT_KEYBOARD = {
    "type": "buttons",
    "buttons": [
        FIND_BY_HBL,
    ]
}

NEW_INPUT = '새 값 입력하기'


def keyboard(request):
    return JsonResponse(DEFAULT_KEYBOARD)


@csrf_exempt
def message(request):
    params = json.loads(request.body)
    user_key = params['user_key']
    content = params['content']

    user, created = KakaoUser.objects.get_or_create(user_key=user_key)

    # Button 타고 들어온 경우
    if content in FIND_BUTTONS:
        if content == FIND_BY_HBL:
            user_hbl_queries = user.packagequery_set.filter(
                type='HBL',
                created_at__gte=timezone.now() - timezone.timedelta(days=7)
            )
            user.context = {
                'state': 'FIND_BY_HBL',
            }
            user.save()
            if user_hbl_queries.count():
                return JsonResponse({
                    'keyboard': {
                        'type': 'buttons',
                        'buttons': list(user_hbl_queries.values_list('tracking_number', flat=True)) + [NEW_INPUT]
                    },
                    'message': {
                        'text': '최근 1주일 내 조회하신 값들이 있습니다. 아래 중 선택하시거나, 혹은 새 값을 입력해주세요.'
                    }
                })
            return JsonResponse({
                'type': 'text',
                'message': {
                    'text': QUERY_BY_HBL
                }
            })
        # elif content == FIND_BY_MBL:
        #     pass
        # elif content == FIND_BY_CRG:
        #     pass

    # DB에서 Context 가져와 응답하는 경우
    if user.context['state'] == 'FIND_BY_HBL':
        if content == NEW_INPUT:
            return JsonResponse({
                'type': 'text',
                'message': {
                    'text': QUERY_BY_HBL
                }
            })
        try:
            pq, created = PackageQuery.objects.get_or_create(
                user=user,
                type='HBL',
                tracking_number=content,
            )
            result = find_by_hbl(content)
            user.context['state'] = 'idle'
            user.save()
            return JsonResponse({
                'message': {
                    'text': HBL_MESSAGE_TEMPLATE.format(**result),
                },
                'keyboard': DEFAULT_KEYBOARD,
            })
        except IndexError as e:
            print(e)
            return JsonResponse({
                'message': {
                    'text': '잘못된 HBL 번호이거나 아직 통관이 시작되지 않았습니다. 확인후 다시 적어주세요.',
                },
                'keyboard': DEFAULT_KEYBOARD,
            })
