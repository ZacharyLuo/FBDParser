
from ._global import _r, length, bisize, fontname, color
from ._frames import background

"======================================字符控制类====================================="

# 字体
font = rf'''
    # 双向字号
    (?P<zh>{_r(bisize)})?
    # 字体名
    (?P<zt>{_r(fontname)})?
'''

class TextPatterns:
    # 汉体注解（HT）
    # 民体注解（MT）
    HT_infix = MT_infix = rf'''
        {font}  # 字号、字体
        (?:\#|《  # 外挂字体
            (?P<wz>.*?)  # 外挂字体名
            (?P<wc>B)?  # 外挂字体粗体
            (?P<wx>I)?》  # 外挂字体斜体
            (?P<tz>\!?)  # 只对同类文字才起作用
        )?
    '''

    # 数字字体注解（ST）
    ST_infix = rf'''(?:
        {font}|  # 字号、字体
        (?P<bt>[\+\-])  # 字体随上级字体变化开关
    )'''

    # WT（外文字体注解）
    WT_infix = rf'''(?:
        {HT_infix}|  # 字体注解（同HT）
        (?P<bt>[\+\-])  # 字体随上级字体变化开关
    )'''

    # 长扁字注解（CB）
    CB_infix = r'''(?:
        (?P<cb>[CB])  # 长/扁字
        (?P<cs>[1-7]|%(?:\d{1,2}|1\d\d|200))  # 长扁参数
    )?'''

    # 粗细注解（CX）
    CX_infix = r'(?P<js>-?[1-4])?'  # 级数，负数表示笔划变细

    # 大写字母风格注解（DF）
    DF_infix = r'''
        (?P<gs>  # 使用大写字母格式
            D|  # 使用全部大写字母格式
            X)?  # 使用小型大写字母格式
        (?P<ln>!)?  # 只对当前流内的字母有效
    '''

    # 繁简注解（FJ）
    FJ_infix = r'(?P<fj>[FJ])?'  # 繁体/简体状态

    # 勾边注解（GB）
    GB_prefix = rf'''
        (?P<kd>[1-2]?\d)?  # 勾边宽度
        (?P<wk>W)?  # 不要边框的勾边字
        (?P<yz>Y)?  # 表示为阴字，即字为白色，边框为白色，勾边为黑色
        (?:(?P<bs>{_r(color)})B)?  # 边框色
        (?:(?P<gs>{_r(color)})G)?  # 勾边色
    '''
    GB_infix = rf'{GB_prefix}(?:,(?P<zs>\d+))?'  # 字数

    # 紧排注解（JP）
    JP_infix = r'''
        (?P<jp>\+?(?:[1-2]?\d|3[0-2]))?  # 紧排系数，+：表示松排，将字间距离拉开
        (?P<zj>!)?  # 分数自动紧排
    '''

    # 计数注解（JS）
    JS_obj = r'''(?:;  # 计数对象
        (?:《(?P<bm>.+?)》)  # 计数别名
        (?:\:P(?P<sx>\d)  # 计数开始序号，默认开始序号为1
            \+(?P<jg>\d))?  # 序号增加间隔，默认为每次增加1
    )'''
    JS_infix = rf'''
        (?P<fs>[SH])?  # 用数字/汉字方式
        (?P<lj>[DX])?  # 计数对象用数字/点连接
        (?P<dx>{_r(JS_obj)}{{1,3}})  # 计数对象
    '''

    # 空心注解（KX）
    KX_prefix = rf'''
        (?P<ww>[1-2]?\d|3[01])?  # 网纹编号
        (?P<wk>W)?  # 不要边框的空心字
    '''
    KX_infix = rf'{KX_prefix}(?:,(?P<zs>\d+))?'  # 字数

    # 立体注解（LT）
    LT_prefix = rf'''
        (?P<kd>[0-7])?  # 阴影宽度
        (?P<ys>{_r(color)})?  # 阴影颜色
        (?P<wk>W)?  # 不要边框的立体字
        (?P<yz>Y)?  # 表示为阴字，即字为白色，阴影为黑色
        (?P<fw>  # 缺省：阴影显示在字的右下方
            YS|  # 阴影显示在字的右上方
            ZS|  # 阴影显示在字的左上方
            ZX)?  # 阴影显示在字的左下方
    '''
    LT_infix = r'{LT_prefix}(?:,(?P<zs>\d+))?'  # 字数

    # 禁排注解（PJ）
    PJ_infix = r'''
        (?:S:(?P<hs>.*?))?  # 行首禁排字符
        (?:;M:(?P<hm>.*?))?  # 行末禁排字符
    '''

    # 倾斜注解（QX）
    QX_prefix = r'''
        (?P<zy>[ZY])  # 向左/右倾斜
        (?P<xd>[1-9]|1[0-5])  # 倾斜度
        (?P<zx>\#)?  # 按字符中心线倾斜
    '''

    # 日文注解（RW）
    RW_infix = r'(?P<jr>O)?'  # 使用日文旧字形

    # 角标大小设置注解（SS）
    SS_infix = r'(?P<jb>[1-9]|10)?'  # 上下角标的字号级别

    # 文种注解（WZ）
    WZ_infix = r'''(?P<wz>
        E|  # 英文
        R|  # 俄文
        M|  # 新蒙文
        Z  # 壮文
    )'''

    # 旋转注解（XZ）
    XZ_prefix = r'''(?:
        (?P<jd>[1-9]\d|[1-9]|[1-2]\d\d|3[0-5]\d|360)  # 旋转度
        (?P<zx>\#)?|  # 按中心旋转
        (?P<zz>Z)?  # 竖排时，符号向左旋转90°
        (?P<zh>H)?  # 竖排时旋转汉字标点
        (?P<zw>W)?  # 竖排时旋转外文标点
    )'''

    # 阴阳字注解（YY）
    YY_prefix = ''

    # 拼音注解（PY）
    PY_prefix = rf'''
        (?P<zh>{_r(bisize)})?  # 拼音字号（注意：先横向后纵向）
        (?P<ys>{_r(color)})?  # 颜色
        (?:K(?P<jj>{_r(length)}))?  # 拼音与拼音之间的距离
        (?:G(?P<dj>{_r(length)}))?  # 拼音与汉字之间的距离
        (?P<pf>
            S|  # 横排时拼音排在汉字之上，竖排时注音右转排在汉字之右
            L|  # 拼音直立排在汉字之右
            X)?  # 横排时拼音排在汉字之下，竖排时拼音右转排在汉字之左（缺省）
        (?P<dq>
            N|  # 横排时汉字靠左边排，竖排时汉字靠上排
            M|  # 汉字居中排（缺省）
            R)?  # 横排时汉字靠右边排，竖排时汉字靠下排
        (?P<jx>Z)?  # 在拼音和汉字之间画一正线
    '''

    # 注音注解（ZY）
    ZY_prefix = rf'''
        (?P<zh>{_r(bisize)})?  # 注音字号（注意：先横向后纵向）
        (?P<ys>{_r(color)})?  # 颜色
        (?:K(?P<dj>{_r(length)}))?  # 注音与汉字之间的距离
        (?P<pf>[SLX])?  # 注音相对汉字位置（同PY）
    '''

    # 着重注解（ZZ）
    ZZ_prefix = rf'''(?:
        (?P<fh>  # 着重符，缺省表示使用着重点
            Z|  # 正线
            F|  # 反线
            D|  # 点线
            S|  # 双线
            Q|  # 曲线
            =|  # 双曲线
            L|  # 三连点
            。!?|  # 加圈，用"句号"
            !   # 在外文和数字下加着重点
        )?
        (?P<hs>\#)?  # 着重线、着重点（或圈）加在一行的上面
        (?:,(?P<jj>-?{_r(length)}))?  # 着重符与正文之间的距离
        |(?P<cm>A\d{{5}})  # 聪明码
        |(?:{background})?  # 底纹说明
    )'''
    ZZ_infix = rf'(?P<zs>\d+){ZZ_prefix}'  # 字数
