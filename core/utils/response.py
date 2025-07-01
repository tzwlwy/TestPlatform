from rest_framework.response import Response

'''
code	含义	建议使用场景
20000	请求成功	所有成功响应
40001	参数缺失或错误	缺少 user_id、格式错误等
40401	用户未连接	指定用户不存在或无连接
50000	服务内部错误	非预期异常等
'''


def api_response(code=20000, message="Success", data=None, http_status=200):
    return Response({
        "code": code,
        "message": message,
        "data": data or {}
    }, status=http_status)
