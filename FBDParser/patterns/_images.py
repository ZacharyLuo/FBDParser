
from ._global import _r, anchor, lines, length, fontset, color

"========================================图片图注类=========================================="

class ImagePatterns:
    # 插入注解（CR）
    CR_infix = rf'''
        (?P<wj>.+?)  # 文件名
        {anchor}  # 位置、排法
        (?P<hy>\#)?  # 文件可后移
        (?P<w2>;W)?  # 指定所要插入的文件是由Wits 2.1生成的
    '''

    # 图字注解（TZ）
    TZ_prefix = rf'''
        (?:S(?P<sk>-?{_r(lines)})?)?  # 上边空
        (?:;X(?P<xk>-?{_r(lines)})?)?  # 下边空
        (?:;Z(?P<zk>-?{_r(length)})?)?  # 左边空
        (?:;Y(?P<yk>-?{_r(length)})?)?  # 右边空
    '''

    image = rf'''
        (?P<qr>,@)?  # 图片嵌入大样文件中
        (?:,(?P<wg>{_r(lines)})  # 占位高度
            (?:。(?P<wk>{_r(length)}))?  # 占位宽度
        )?
        (?:;
            (?:
                %(?P<gb>\d+(?:\.\d+)?)  # 高度放缩比例
                %(?P<kb>\d+(?:\.\d+)?)  # 宽度放缩比例
            |E
                (?P<tg>{_r(lines)})  # 图片高度
                (?:。(?P<tk>{_r(length)}))?  # 图片宽度
            )
        )?
        {TZ_prefix.replace(r'(?:S', r'(?:;S')}  # 四边空
    '''

    # 插入EPS注解（PS）
    PS_infix = rf'''
        (?P<wj>.+?)  # 文件名
        {image}  # 尺寸、边空
        {anchor}  # 位置、排法
        (?P<hy>\#)?  # 文件可后移
        (?P<dz>%)?  # 图片不挖空，叠字
        (?:;(?P<xz>\d|[1-2]?\d\d|3[0-5]\d|360))?  # 按顺时针方向绕中旋转的度数
        (?P<hd>,HD)?  # 指定为灰度图片
    '''

    # 图片注解（TP）
    TP_infix = rf'''
        (?P<wj>.+?)  # 文件名
        {image}  # 尺寸、边空
        {anchor}  # 位置、排法
        (?P<hy>\#)?  # 文件可后移
        (?P<dz>%)?  # 图片不挖空，叠字
        (?P<yt>H)?  # 图片用阴图
        (?P<tx>,TX(?:[0-8]\d\d\d)?)?  # 在向量图形中，封闭部分填底纹
        (?P<hd>,HD)?  # 指定为灰度图片
    '''

    # 图文注解（TW）
    TW_infix = rf'''
        {fontset}  # 字号、字体
        (?P<ys>{_r(color)})?  # 颜色
        ,(?P<wz> # 图说在图片的位置，缺省为B
            B|  # 图片说明在图片的下边
            L|  # 图片说明在图片在左边
            R)  # 图片说明在图片在右边
        (?:&(?P<dq>  # 图说与图片的对齐方式
            Z|  # 左/上对齐
            C|  # 居中
            Y)  # 右/下对齐
        )?
        ,(?P<gd>{_r(lines)})  # 图说所占高度
        (?P<sp>!)?  # 图片说明竖排
    '''

    # 图说注解（TS）
    TS_prefix = rf'''
        (?P<gd>{_r(lines)})?  # 图说所占高度
        (?P<wz>[ZY])?  # 图说在图片的位置
        (?P<dq>[LMR])?  # 图说与图片的对齐方式
        (?P<dz>%)?  # 图说不挖空，叠字
        (?P<sp>!)?  # 图片说明竖排
    '''

    # 插入随文图片注解（XC）
    XC_infix = rf'''
        (?P<wj>.+?)  # 文件名
        {image + ';?'}  # 尺寸、边空
        (?P<dq>  # 基线位置
            ,SQ|  # 上齐
            ,XQ|  # 下齐
            ,JZ)?  # 居中
        (?:
            (?:
                (?P<yt>H)?  # 图片用阴图
                (?P<tx>,TX(?:[0-8]\d\d\d)?)?  # 在向量图形中，封闭部分填底纹
            )|(?P<cr>;C  # 插入CR文件
                (?P<w2>W)?  # 指定所要插入的文件是由Wits 2.1生成的
            )|(?P<ps>;P  # 插入EPS文件
                (?P<xz>\d|[1-2]?\d\d|3[0-5]\d|360)?  # 按顺时针方向绕中旋转的度数
            )
        )?
        (?P<hd>,HD)?  # 指定为灰度图片
    '''