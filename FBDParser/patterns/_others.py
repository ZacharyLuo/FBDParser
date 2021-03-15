
"======================================其他注解======================================="

class OtherPatterns:
    # 不排注解（BP）
    # 纯文字注解（CW）
    BP_prefix = CW_prefix = ''

    # 风格注解（FG）
    FG_infix = r'''
        (?P<fg>[SN])?  # 大样为S10/NPS格式
        (?P<ln>!)?  # 只对当前流内的文字有效
    '''

    # 外挂字体别名定义注解（KD）
    KD_infix = r'''
        《(?P<bm>.*?)》  # 外挂字体别名
        《(?P<zm>.*?)》  # 外挂字体字面名
    '''

    # 书版注解（SB）
    SB_infix = r'(?P<wj>[^,]+?(?:,[^,]+?){,39})'  # 文件名

    # 条码提取注解（TM）
    TM_prefix = r'''(?P<ys>  # 公文要素
        CW|  # 成文日期
        FW|  # 发文单位
        QH|  # 文号与期号
        BT|  # 文件标题
        ZS|  # 主送单位
        RQ  # 条码制作日期
    )?'''

    # 自定义注解（ZD）
    ZD_infix = r'''
        (?P<mc>[0-9A-Za-z]{1,6})\(  # 定义名
        (?P<yx>D)?  # 自定义采用有序号形式
    '''

    # 自定义文件名注解（ZM）
    ZM_infix = r'(?P<zm>.+)'